# from langchain.llms import Bedrock
from langchain.llms import Bedrock

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd

# Set page config
st.set_page_config(
    page_title="CSV Analyzer", 
    page_icon="🔍",
    layout="centered", 
    initial_sidebar_state="collapsed",
)

def get_bedrock_llm():

    llm = Bedrock(
        model_id="amazon.titan-tg1-large",
        # credentials_profile_name="default",
        model_kwargs={
            "maxTokenCount": 4096,
            "stopSequences": [],
            "temperature": 0,
            "topP": 1,
        }
    )
    
    return llm

def query_agent(data, query):
    formatted_query = f'Human: {query}'
    df = pd.read_csv(data)
    llm = get_bedrock_llm()    
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agent.run(formatted_query)
    # return agent.run(formatted_query, handle_parsing_errors=True)

def main():
    st.title("🔍 Your daily CSV Data Analyzer")
    st.markdown("<h3 style='color: teal;'>Upload your CSV:</h3>", unsafe_allow_html=True)
    data = st.file_uploader("", type="csv", accept_multiple_files=False, key="csv")

    if data:
        preview_button = st.button("Preview Data")
        if preview_button:
            df_preview = pd.read_csv(data)
            st.dataframe(df_preview.head())  # Showing top rows of the dataframe

    st.markdown("<h3 style='color: teal;'>Type your query:</h3>", unsafe_allow_html=True)
    query = st.text_area("", key="query")

    analyze_button = st.button("Generate Response")
    if analyze_button:
        if data:
            with st.spinner("Analyzing..."):
                answer = query_agent(data, query)
            st.markdown(f"<p style='font-size: 18px; color: purple;'>{answer}</p>", unsafe_allow_html=True)
        else:
            st.error("Please upload a CSV file first.")

if __name__ == '__main__':
    load_dotenv()  
    main()
