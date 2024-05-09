import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.schema import Document
from langchain_community.llms import Bedrock
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from langchain.chains.summarize import load_summarize_chain
import os
import uuid

# Load environment variables at the start
load_dotenv()

# Initialize session state variable to track unique user sessions
if 'unique_id' not in st.session_state:
    st.session_state['unique_id'] = ''

# Function to extract text from a PDF file using PyPDF2
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    text = text.replace('\x00', '')  # Remove null characters often found in PDF text extractions
    return text

# Function to create Document objects from PDF files uploaded by the user
def create_docs(user_pdf_list, unique_id):
    docs = []
    for filename in user_pdf_list:
        chunks = get_pdf_text(filename)
        # Create Document objects, adding metadata for each file
        docs.append(Document(
            page_content=chunks,
            metadata={"name": filename.name,
                      "id": filename.file_id,
                      "type": filename.type,
                      "size": filename.size,
                      "unique_id": unique_id},
        ))
    return docs

# Function to create a vector store for document searching
def get_vectorstore(text_chunks):
    embeddings = BedrockEmbeddings()
    # Create a PGVector object to manage document embeddings and vector-based search
    docsearch = PGVector.from_documents(documents=text_chunks, 
                                        embedding=embeddings, 
                                        collection_name=COLLECTION_NAME,
                                        connection_string=CONNECTION_STRING
                                        )

    return docsearch

# Function to find documents similar to a job description
def similar_docs(vectorstore, job_description, document_count, unique_id):
    # Perform a similarity search based on the job description and user-specific context
    similar_docs = vectorstore.similarity_search_with_score(job_description, 
                                                            int(document_count),
                                                            {"unique_id": unique_id})
    return similar_docs

# Function to get a summarized version of the current document
def get_summary(current_doc, selected_llm):
    llm = get_bedrock_llm(selected_llm)
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.run([current_doc])
    return summary

# Function to select a specific LLM based on user input
def get_bedrock_llm(selected_llm):
    print(f"[INFO] Selected LLM is : {selected_llm}")
    if selected_llm in ['anthropic.claude-v2', 'anthropic.claude-v1', 'anthropic.claude-instant-v1']:
        llm = Bedrock(model_id=selected_llm)
    elif selected_llm in ['amazon.titan-tg1-large', 'amazon.titan-text-express-v1', 'amazon.titan-text-lite-v1']:
        llm = Bedrock(model_id=selected_llm,
                      model_kwargs={"maxTokenCount": 4096, "stopSequences": [], "temperature": 0, "topP": 1})
    else:
        raise ValueError(f"Unsupported LLM: {selected_llm}")
    return llm

# Main function that setups the Streamlit UI
def main():
    st.set_page_config(page_title="Resume Screening Assistance")
    st.markdown("<h1 style='text-align: center;'>Resume Screening Assistance</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: orange;'>Powered by Amazon Bedrock</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 30px;'>💁 I can help you in the Resume screening process 💁 </h3>", unsafe_allow_html=True)
    st.markdown("#### 📄 Job Description")
    st.markdown("""<a href="https://d1nd1o4zkls5mq.cloudfront.net/sample_job_description.txt" target="_blank"><button style="color: white; background-color: #FF4B4B; border: none; border-radius: 4px; padding: 10px 15px;">Download Sample Job Description</button></a>""", unsafe_allow_html=True)
    job_description = st.text_area("Please paste the job description here", key="1")
    st.markdown("#### 📥 Upload Resumes")
    st.markdown("""<a href="https://d1nd1o4zkls5mq.cloudfront.net/sample_resumes.zip" target="_blank"><button style="color: white; background-color: #FF4B4B; border: none; border-radius: 4px; padding: 10px 15px;">Download Sample Resumes</button></a>""", unsafe_allow_html=True)
    document_count = st.text_input("Enter the number of resumes you want to screen", key="2")
    pdf = st.file_uploader("Upload resumes here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)
    st.markdown("#### 🤖 Select the LLM")
    llm_options = ['anthropic.claude-v2', 'anthropic.claude-instant-v1', 'amazon.titan-tg1-large', 'amazon.titan-text-express-v1', 'amazon.titan-text-lite-v1']
    selected_llm = st.radio("Choose an LLM", options=llm_options)
    submit = st.button("Help me with the analysis")
    if submit:
        with st.spinner('Wait for it...'):
            st.session_state['unique_id'] = uuid.uuid4().hex
            final_docs_list = create_docs(pdf, st.session_state['unique_id'])
            st.write("*Resumes uploaded* :" + str(len(final_docs_list)))
            vectorstore = get_vectorstore(final_docs_list)
            relevant_docs = similar_docs(vectorstore, job_description, document_count, unique_id=st.session_state['unique_id'])
            st.write(":heavy_minus_sign:" * 30)
            for item in range(len(relevant_docs)):
                st.subheader(f"👉 {item + 1}")
                st.write("**File** : " + relevant_docs[item][0].metadata['name'])
                with st.expander('Show me 👀'):
                    st.info("**Match Score** : " + str(relevant_docs[item][1]))
                    summary = get_summary(relevant_docs[item][0], selected_llm=selected_llm)
                    st.write("**Summary** : " + summary)
        st.success("Hope I was able to save your time❤️")
        st.markdown("<h3 style='text-align: center; font-size: 30px;'> To know more about Amazon Bedrock, visit <a href='https://aws.amazon.com/bedrock/' target='_blank'>here</a> </h3>", unsafe_allow_html=True)

if __name__ == '__main__':
    # Construct the connection string from environment variables
    COLLECTION_NAME ='resume-embeddings-index'
    CONNECTION_STRING = PGVector.connection_string_from_db_params(
        driver=os.getenv("PGVECTOR_DRIVER"),
        user=os.getenv("PGVECTOR_USER"),
        password=os.getenv("PGVECTOR_PASSWORD"),
        host=os.getenv("PGVECTOR_HOST"),
        port=os.getenv("PGVECTOR_PORT"),
        database=os.getenv("PGVECTOR_DATABASE"),
    )
    main()
