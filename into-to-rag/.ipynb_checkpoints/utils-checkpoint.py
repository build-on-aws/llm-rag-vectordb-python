import os
import re
import boto3
import tempfile
import time
from pytube import YouTube
from urllib.request import urlopen
from botocore.exceptions import NoCredentialsError, ClientError
from tqdm import tqdm

def transcribe_video(s3_bucket_name, youtube_video_url):
    if not os.path.exists("transcription.txt"):
        youtube = YouTube(youtube_video_url)
        audio = youtube.streams.get_audio_only()
        audio_file_name = audio.default_filename

        with tempfile.TemporaryDirectory() as tmpdir:
            audio_file_path = audio.download(output_path=tmpdir)

            s3_client = boto3.client('s3')
            try:
                s3_client.upload_file(audio_file_path, s3_bucket_name, audio_file_name)
                print("Uploaded audio to S3.")
            except ClientError as e:
                print(f"Failed to upload audio to S3: {e}")
                return

            job_name = re.sub(r'[^0-9a-zA-Z._-]+', '', audio_file_name)[:200] + str(int(time.time()))
            transcribe_client = boto3.client('transcribe')
            media_uri = f"s3://{s3_bucket_name}/{audio_file_name}"
            
            # Start the transcription job.
            try:
                transcribe_client.start_transcription_job(
                    TranscriptionJobName=job_name,
                    Media={'MediaFileUri': media_uri},
                    MediaFormat='mp4',
                    LanguageCode='en-US'
                )
                print(f"Started transcription job: {job_name}")
            except ClientError as e:
                print(f"Failed to start transcription job: {e}")
                return

            with tqdm(total=100, desc="Transcribing", unit="%", leave=True) as pbar:
                while True:
                    try:
                        status = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
                    except ClientError as e:
                        print(f"Error checking job status: {e}")
                        pbar.close()
                        return

                    job_status = status['TranscriptionJob']['TranscriptionJobStatus']
                    if job_status == 'COMPLETED':
                        pbar.update(100 - pbar.n)  # Complete the progress bar
                        break
                    elif job_status == 'FAILED':
                        pbar.close()
                        print("Transcription job failed.")
                        return
                    else:
                        pbar.set_postfix_str(f"Current status: {job_status}")
                        time.sleep(15)  # Sleep for 15 seconds before checking again

            # Job completed successfully
            transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
            try:
                response = urlopen(transcript_file_uri)
                transcription = response.read().decode('utf-8')

                with open("transcription.txt", "w") as file:
                    file.write(transcription)
                print("Transcription completed and saved.")
            except Exception as e:
                print(f"Failed to download or save transcription: {e}")
    else:
        print("Transcription file already exists.")
