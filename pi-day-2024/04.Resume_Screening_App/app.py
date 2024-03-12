import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock
from langchain.schema import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.vectorstores.pgvector import PGVector

import os
import uuid

# Creating session variables
if 'unique_id' not in st.session_state:
    st.session_state['unique_id'] =''
    
# Extract Information from PDF file
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    text = text.replace('\x00', '')  # Remove null characters
    
    return text

def create_docs(user_pdf_list, unique_id):
    docs=[]
    for filename in user_pdf_list:
        
        chunks=get_pdf_text(filename)

        #Adding items to our list - Adding data & its metadata
        docs.append(Document(
            page_content=chunks,
            metadata={"name": filename.name,
                      "id":filename.id,
                      "type=":filename.type,
                      "size":filename.size,
                      "unique_id":unique_id},
        ))

    return docs
    
def get_vectorstore(text_chunks):

    embeddings = BedrockEmbeddings()
    
    docsearch = PGVector.from_documents(documents=text_chunks, 
                                       embedding=embeddings, 
                                       collection_name='resume-embeddings-index',
                                       connection_string=CONNECTION_STRING)

    return docsearch 

def similar_docs(vectorstore, job_description, document_count, unique_id):
    
    similar_docs = vectorstore.similarity_search_with_score(job_description, 
                                                            int(document_count),
                                                            {"unique_id":unique_id})
    
    return similar_docs
    
# Helps us get the summary of a document
def get_summary(current_doc, selected_llm):

    llm = get_bedrock_llm(selected_llm)
    
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run([current_doc])

    return summary

def get_bedrock_llm(selected_llm):
    print(f"[INFO] Selected LLM is : {selected_llm}")
    if selected_llm in ['anthropic.claude-v2', 'anthropic.claude-v1', 'anthropic.claude-instant-v1']:
        llm = Bedrock(model_id=selected_llm, model_kwargs={'max_tokens_to_sample': 4096})

    elif selected_llm in ['amazon.titan-tg1-large', 'amazon.titan-text-express-v1', 'amazon.titan-text-lite-v1']:
        llm = Bedrock(
            model_id=selected_llm,
            model_kwargs={
                "maxTokenCount": 4096,
                "stopSequences": [],
                "temperature": 0,
                "topP": 1,
            }
        )
    else:
        raise ValueError(f"Unsupported LLM: {selected_llm}")

    return llm

def main():

    st.set_page_config(page_title="Resume Screening Assistance")

    # Centering the title using HTML in st.markdown
    st.markdown("<h1 style='text-align: center;'>Resume Screening Assistance</h1>", unsafe_allow_html=True)

    # Centering and coloring the subtitle using HTML in st.markdown
    st.markdown("<h2 style='text-align: center; color: orange;'>Powered by Amazon Bedrock</h2>", unsafe_allow_html=True)

    # You may choose any color for the subtitle by replacing 'blue' with your preferred color.

    # If you prefer a different color for the subheader:
    st.markdown("<h3 style='text-align: center; font-size: 30px;'>💁 I can help you in the Resume screening process 💁 </h3>", unsafe_allow_html=True)

    st.markdown("#### 📄 Job Description")
    
    # Adding the hyperlink button
    st.markdown("""
        <a href="https://d1nd1o4zkls5mq.cloudfront.net/sample_job_description.txt" target="_blank">
            <button style="color: white; background-color: #FF4B4B; border: none; border-radius: 4px; padding: 10px 15px;">
                Download Sample Job Description
            </button>
        </a>
    """, unsafe_allow_html=True)
    
    job_description = st.text_area("Please paste the job description here",key="1")
    
    st.markdown("#### 📥 Upload Resumes")

    # Adding the hyperlink button
    st.markdown("""
        <a href="https://d1nd1o4zkls5mq.cloudfront.net/sample_resumes.zip" target="_blank">
            <button style="color: white; background-color: #FF4B4B; border: none; border-radius: 4px; padding: 10px 15px;">
                Download Sample Resumes
            </button>
        </a>
    """, unsafe_allow_html=True)
    
    document_count = st.text_input("Enter the number of resumes you want to screen",key="2")
    
    pdf = st.file_uploader("Upload resumes here, only PDF files allowed", type=["pdf"],accept_multiple_files=True)
    
    # Add LLM selection UI
    st.markdown("#### 🤖 Select the LLM")
    llm_options = [
        'anthropic.claude-v2', 
        'anthropic.claude-instant-v1',
        'amazon.titan-tg1-large', 
        'amazon.titan-text-express-v1', 
        'amazon.titan-text-lite-v1'
    ]
    
    selected_llm = st.radio("Choose an LLM", options=llm_options)

    submit=st.button("Help me with the analysis")


    if submit:
        with st.spinner('Wait for it...'):

            #Creating a unique ID, so that we can use to query and get only the user uploaded documents from Aurora vector store
            st.session_state['unique_id']=uuid.uuid4().hex

            #Create a documents list out of all the user uploaded pdf files
            final_docs_list=create_docs(pdf,st.session_state['unique_id'])

            #Displaying the count of resumes that have been uploaded
            st.write("*Resumes uploaded* :"+str(len(final_docs_list)))

            #Push data to Aurora 
            vectorstore = get_vectorstore(final_docs_list)

            #Fecth relavant documents from Aurora
            relavant_docs=similar_docs(vectorstore, job_description, document_count,unique_id=st.session_state['unique_id'])
            
            #Introducing a line separator
            st.write(":heavy_minus_sign:" * 30)
            
            #For each item in relavant docs - we are displaying some info of it on the UI
            for item in range(len(relavant_docs)):
                st.subheader("👉 "+str(item+1))

                #Displaying Filepath
                st.write("**File** : "+relavant_docs[item][0].metadata['name'])

                #Introducing Expander feature
                with st.expander('Show me 👀'): 
                    st.info("**Match Score** : "+str(relavant_docs[item][1]))
                    #st.write("***"+relavant_docs[item][0].page_content)
                    
                    #Gets the summary of the current item using 'get_summary' function that we have created which uses LLM & Langchain chain
                    # summary = get_summary(relavant_docs[item][0])
                    summary = get_summary(relavant_docs[item][0], selected_llm=selected_llm)

                    st.write("**Summary** : "+summary)           
        
        st.success("Hope I was able to save your time❤️")
        st.markdown(
            "<h3 style='text-align: center; font-size: 30px;'> To know more about Amazon Bedrock, visit <a href='https://aws.amazon.com/bedrock/' target='_blank'>here</a> </h3>",
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    load_dotenv()
    
    CONNECTION_STRING = PGVector.connection_string_from_db_params(                                                  
        driver = os.environ.get("PGVECTOR_DRIVER"),
        user = os.environ.get("PGVECTOR_USER"),                                      
        password = os.environ.get("PGVECTOR_PASSWORD"),                                  
        host = os.environ.get("PGVECTOR_HOST"),                                            
        port = os.environ.get("PGVECTOR_PORT"),                                          
        database = os.environ.get("PGVECTOR_DATABASE")                                       
)  

    main()