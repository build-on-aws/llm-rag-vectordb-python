# **Data Analysis Tool using Amazon Bedrock** 

Build a streamlined Streamlit application to analize your CSV data. This guide walks you through the process of setting up and running the application.

![Preview](/llm-rag-vectordb-python/data-analysis-tool/da.gif)

## **Features** 

- **Streamlit**: For a smooth web application interface.
- **Langchain**: Integrated for advanced functionalities.
- **AWS Services**: Harness the power of Amazon's cloud services.
    - **Amazon Bedrock**: A fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon with a single API, along with a broad set of capabilities you need to build generative AI applications, simplifying development while maintaining privacy and security

## **Getting Started** 

### **1. Setting Up a Virtual Environment** 

Use `virtualenv` to create an isolated Python environment:

1. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```

2. Navigate to the directory where you cloned the repository.
    
3. Initialize the virtual environment:
    ```bash
    virtualenv da-env
    ```

4. Activate the environment:
    ```bash
    source da-env/bin/activate 
    ```

### **3. Installing Dependencies**

With your virtual environment active, install the necessary packages:

```bash
pip install -r requirements.txt
```

This command installs all dependencies from the `requirements.txt` file into your `da-env` environment.

### **4. Usage**

To launch the application:

1. Ensure the dependencies are installed and your `.env` file has the Aurora PostgreSQL DB details.

2. Install the `pgvector` extension on your Aurora PostgreSQL DB cluster:
   ```sql
   CREATE EXTENSION vector;
   ```

3. Launch the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

4. Your default web browser will open, showcasing the application interface.

5. Follow the on-screen instructions to load your CSV data ([sample data](https://d1nd1o4zkls5mq.cloudfront.net/employees.csv)) 