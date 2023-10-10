import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linedin_lookup_agent
from langchain.llms.bedrock import Bedrock


def get_llm():
    bedrock_llm = Bedrock(model_id="anthropic.claude-v2",
                          model_kwargs={"temperature": 0.1, "max_tokens_to_sample": 4096})
    return bedrock_llm


def ice_break_with(name: str):
    linkedin_profile_url = linedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    summary_template = """
        Given the LinkedIN information {information} about a person from, I wish to create the following:
            1. A short Summary
            2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = get_llm()
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(information=linkedin_data)
    return result


def main():
    
    st.title('Building Bonds: The Power of Ice-Breakers 💼✨')
    st.write('An app that uses Amazon Bedrock and LangChain to create summaries based on their social media profile. 🚀')

    st.sidebar.header("🔎 Enter the person's details")
    name = st.sidebar.text_input("Name (e.g., 'Andy Jassy Amazon'):")

    if st.sidebar.button('Get Summary'):
        with st.spinner('Fetching LinkedIn data and creating summary... 🔄'):
            result = ice_break_with(name)
        st.subheader(f'Summary and couple of interesting facts 📝')
        st.write(result)
        st.success('Summary generated successfully! 👍')

        st.markdown(
            "<h3 style='text-align: center; font-size: 20px;'> To know more about Amazon Bedrock, visit <a href='https://aws.amazon.com/bedrock/' target='_blank'>here</a> </h3>",
            unsafe_allow_html=True
        )
    # Styling the Streamlit page
    st.markdown("""
        <style>
            body {
                color: #4f4f4f;
                background-color: #F5F5F5;
            }
            .stButton>button {
                color: #4f4f4f;
                background-color: #FFD700;
                border-radius: 30px;
                padding: 10px 20px;
                font-size: 1.2em;
            }
        </style>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
