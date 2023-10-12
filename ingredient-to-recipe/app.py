import os
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from transformers import pipeline
import streamlit as st
from langchain.llms.bedrock import Bedrock

PAGE_CONFIG = {"page_title":"Image to Recipe", "page_icon":":chef:", "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)
st.markdown("""
    <style>
        body {
            background-color: #fafafa;
            color: #333;
        }
        h1, h2 {
            color: #ff6347;
        }
        .fileUploader .btn {
            background-color: #ff6347;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

def get_llm():
    bedrock_llm = Bedrock(model_id="anthropic.claude-v2",
                          model_kwargs={"temperature": 0.7, "max_tokens_to_sample": 4096})
    return bedrock_llm

def image_to_text(url):
    with st.spinner('Processing image...'):
        pipe = pipeline(
            "image-to-text",
            model="Salesforce/blip-image-captioning-large",
            max_new_tokens=1000,
        )
        text = pipe(url)[0]["generated_text"]
    return text

def generate_recipe(ingredients):
    template = """
    You are a extremely knowledgeable nutritionist, bodybuilder and chef who also knows
                everything one needs to know about the best quick, healthy recipes. 
                You know all there is to know about healthy foods, healthy recipes that keep 
                people lean and help them build muscles, and lose stubborn fat.
                
                You've also trained many top performers athletes in body building, and in extremely 
                amazing physique. 
                
                You understand how to help people who don't have much time and or 
                ingredients to make meals fast depending on what they can find in the kitchen. 
                Your job is to assist users with questions related to finding the best recipes and 
                cooking instructions depending on the following variables:
                0/ {ingredients}
                
                When finding the best recipes and instructions to cook,
                you'll answer with confidence and to the point.
                Keep in mind the time constraint of 5-10 minutes when coming up
                with recipes and instructions as well as the recipe.
                
                If the {ingredients} are less than 3, feel free to add a few more
                as long as they will compliment the healthy meal.
                
            
                Make sure to format your answer as follows:
                - The name of the meal as bold title (new line)
                - Best for recipe category (bold)
                    
                - Preparation Time (header)
                    
                - Difficulty (bold):
                    Easy
                - Ingredients (bold)
                    List all ingredients 
                - Kitchen tools needed (bold)
                    List kitchen tools needed
                - Instructions (bold)
                    List all instructions to put the meal together
                - Macros (bold): 
                    Total calories
                    List each ingredient calories
                    List all macros 
                    
                    Please make sure to be brief and to the point.  
                    Make the instructions easy to follow and step-by-step.
    """

    with st.spinner('Making the recipe for you...'):
        prompt = PromptTemplate(template=template, input_variables=["ingredients"])
        llm = get_llm()
        recipe_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
        recipe = recipe_chain.run(ingredients)

    return recipe

def main():

    st.markdown("<h1 style='text-align: center; color: red;'>🍲 Recipe Generator 🍲 </h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; font-size: 24px; color: black'>Powered by <span style='color: orange;'>Amazon Bedrock</span></h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="display: flex; justify-content: center;">
            <a href="https://d1nd1o4zkls5mq.cloudfront.net/img1.jpeg" target="_blank">
                <button style="margin-right: 10px; color: white; background-color: #007BFF; border: none; border-radius: 2px; padding: 10px 15px; transition: background-color 0.3s;">
                    Download Sample Image 1
                </button>
            </a>
            <a href="https://d1nd1o4zkls5mq.cloudfront.net/img2.jpeg" target="_blank">
                <button style="color: white; background-color: #007BFF; border: none; border-radius: 2px; padding: 10px 15px; transition: background-color 0.3s;">
                    Download Sample Image 2
                </button>
            </a>
        </div>
        <style>
            button:hover {
                background-color: #0056b3;
            }
        </style>
    """, unsafe_allow_html=True)
    
    upload_file = st.file_uploader("Choose an image:", type=["jpg", "png"], accept_multiple_files=False)

    if upload_file is not None:
        file_bytes = upload_file.getvalue()
        with open(upload_file.name, "wb") as file:
            file.write(file_bytes)

        st.image(
            upload_file,
            caption="The uploaded image",
            use_column_width=True,
            width=250
        )

        st.markdown("### 🥗 Ingredients from Image")
        ingredients = image_to_text(upload_file.name)
        with st.expander("Ingredients 👀"):
            st.write(ingredients.capitalize())

        st.markdown("### 📋 Recipe")
        recipe = generate_recipe(ingredients=ingredients)
        with st.expander("Cooking Instructions 👀"):
            st.write(recipe)

        st.markdown(
            "<h3 style='text-align: center; font-size: 30px;'> To know more about Amazon Bedrock, visit <a href='https://aws.amazon.com/bedrock/' target='_blank'>here</a> </h3>",
            unsafe_allow_html=True
        )
        os.remove(upload_file.name)

if __name__ == "__main__":
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HUGGINFACE_HUB_API_TOKEN = os.getenv("HUGGINFACE_HUB_API_TOKEN")
    
    main()
