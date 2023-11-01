# **Résumé Screening App using Amazon Bedrock and Amazon Aurora (`pgvector`)** 

Build a streamlined Streamlit application to effectively screen Résumés based on job descriptions. This guide walks you through the process of setting up and running the application.

![Preview](Resume-Screener.gif)

## **Features** 

- **Streamlit**: For a smooth web application interface.
- **Langchain**: Integrated for advanced functionalities.
- **AWS Services**: Harness the power of Amazon's cloud services.
    - **Amazon Bedrock**: A fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon with a single API, along with a broad set of capabilities you need to build generative AI applications, simplifying development while maintaining privacy and security
    - **Amazon Aurora**: Utilized as a vector database with `pgvector`.

## **Getting Started** 

### **1. Pre-requisites** 

- Clone the repository to your local machine.
- Create a `.env` file in the project directory using `env.example` as a reference. Populate the `.env` file with your Aurora PostgreSQL DB cluster details:

    ```bash
    PGVECTOR_DRIVER='psycopg2'
    PGVECTOR_USER='<<Username>>'
    PGVECTOR_PASSWORD='<<Password>>'
    PGVECTOR_HOST='<<Aurora DB cluster host>>'
    PGVECTOR_PORT=5432
    PGVECTOR_DATABASE='<<DBName>>'
    ```

### **2. Setting Up a Virtual Environment** 

Use `virtualenv` to create an isolated Python environment:

1. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```

2. Navigate to the directory where you cloned the repository.
    
3. Initialize the virtual environment:
    ```bash
    virtualenv rs-env
    ```

4. Activate the environment:
    ```bash
    source rs-env/bin/activate 
    ```

### **3. Installing Dependencies**

With your virtual environment active, install the necessary packages:

```bash
pip install -r requirements.txt
```

This command installs all dependencies from the `requirements.txt` file into your `rs-env` environment.

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

5. Follow the on-screen instructions to load your CSV data ([sample data](https://d1nd1o4zkls5mq.cloudfront.net/sample_resumes.zip)) and the desired job description ([sample job description](https://d1nd1o4zkls5mq.cloudfront.net/sample_job_description.txt)).
