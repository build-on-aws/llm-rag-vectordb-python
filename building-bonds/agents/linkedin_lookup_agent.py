from tools.tools import get_profile_url
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.llms.bedrock import Bedrock
from langchain.agents import initialize_agent, Tool, AgentType
import re 




def get_llm():

    bedrock_llm = Bedrock(model_id="anthropic.claude-v2",
                           model_kwargs={"temperature": 0.1,"max_tokens_to_sample": 4096})

    return bedrock_llm

def lookup(name: str) -> str:
    load_dotenv()

    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                  Your answer should contain only a URL of the LinkedIN profile"""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        ),
    ]
    llm = get_llm()
    agent_chain = initialize_agent(tools_for_agent, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    # Get the LLM's output
    try:
        linkedin_username = agent_chain.run(handle_parsing_errors=True, input=prompt_template.format_prompt(name_of_person=name))

    except ValueError as e:
        print("Error while parsing LLM output:", e)
        return None
    
    return linkedin_username
