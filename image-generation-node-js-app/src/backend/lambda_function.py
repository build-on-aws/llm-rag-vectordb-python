import boto3
import uuid
import base64
import io
import json
import boto3
import os
from PIL import Image

s3 = boto3.resource('s3', region_name='us-east-1')
bucket_name = os.environ['OUT_S3_BUCKET_NAME']

s3_client = boto3.client('s3', region_name='us-east-1')
session = boto3.Session()


def get_bedrock_llm():
    bedrock_client = session.client(service_name="bedrock-runtime")
    
    return bedrock_client

def query_endpoint_bedrock(prompt, style_preset):
    bedrock_client = get_bedrock_llm()

    negative_prompts = [
        "poorly rendered",
        "poor background details",
        "poorly drawn mountains",
        "disfigured mountain features",
    ]
    
    request = json.dumps({
                            "text_prompts": (
                                [{"text": prompt, "weight": 1.0}]
                                + [{"text": negprompt, "weight": -1.0} for negprompt in negative_prompts]
                            ),
                            "cfg_scale": 5,
                            "seed": 5450,
                            "steps": 70,
                            "style_preset": style_preset,
                        })
        
    modelId = "stability.stable-diffusion-xl"

    response = bedrock_client.invoke_model(body=request, modelId=modelId)
    
    return response

def parse_response(query_response):
    response_body = json.loads(query_response.get("body").read())
    
    base_64_img_str = response_body["artifacts"][0].get("base64")
    
    return base_64_img_str

def upload_image(base_64_img_str, prmpt):
    
    # Decode your image
    image_data = io.BytesIO(base64.decodebytes(bytes(base_64_img_str, "utf-8")))
    image = Image.open(image_data)

    # Prepare the image for upload to S3
    buffered_image = io.BytesIO()
    image.save(buffered_image, format="PNG")

    image_name = prmpt+str(uuid.uuid4())+'.png'

    buffered_image.seek(0)
    s3.Object(bucket_name, image_name).put(
       Body=buffered_image, ContentType='image/png')
    return s3_client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket_name, 'Key': image_name}, ExpiresIn=1000)


def lambda_handler(event, context):
    print("Received event: "+json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    text = data['data']
    style_preset= data['style_preset']
    # print(text)
    response = query_endpoint_bedrock(text, style_preset)
    base_64_img_str = parse_response(response)
    
    # Display hallucinated image
    url = upload_image(base_64_img_str, text)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': url
    }


event = {
  "data": "Samosa",
  "style_preset": "photographic"
}
print(lambda_handler(event, context=None))
