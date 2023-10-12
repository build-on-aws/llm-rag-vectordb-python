# **Instant Recipe Generator using Amazon Bedrock** 

Build a streamlined Streamlit application to generate recipe given an image of all the ingradients. This guide walks you through the process of setting up and running the application.

![Preview](/llm-rag-vectordb-python/ingredient-to-recipe/rec.gif)

## **Features** 

- **Streamlit**: For a smooth web application interface.
- **Langchain**: Integrated for advanced functionalities.
- **Hugging Face**: Renowned for state-of-the-art natural language processing tools.
- **Amazon Bedrock**: A fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon with a single API, along with a broad set of capabilities you need to build generative AI applications, simplifying development while maintaining privacy and security.

## **Getting Started** 

### **1. Pre-requisites** 

- Clone the repository to your local machine.
- Create a `.env` file in the project directory using `env.example` as a reference.

### **2. Setting Up a Virtual Environment** 

Use `virtualenv` to create an isolated Python environment:

1. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```

2. Navigate to the directory where you cloned the repository.
    
3. Initialize the virtual environment:
    ```bash
    virtualenv res-env
    ```

4. Activate the environment:
    ```bash
    source res-env/bin/activate 
    ```

### **3. Installing Dependencies**

With your virtual environment active, install the necessary packages:

```bash
pip install -r requirements.txt
```

This command installs all dependencies from the `requirements.txt` file into your `res-env` environment.

### **4. Usage**

To launch the application:

1. Ensure the dependencies are installed and your `.env` file is updated.

2. Launch the application using Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Your default web browser will open, showcasing the application interface.

5. Follow the on-screen instructions to load your image of ingradients ([sample image data](https://d1nd1o4zkls5mq.cloudfront.net/img2.jpeg)) 