# **Unified AI Q&A: Harnessing `pgvector`, Amazon Aurora & Amazon Bedrock 📚🦜** 

In the rapid stride of generative AI, crafting sophisticated Q&A bots for specialized tasks has become paramount. However, broad-spectrum LLMs often fall short in niche domains. There's a growing need for AI systems that tap into external databases for improved accuracy, steering clear of "hallucinations."

Enter **Retrieval Augmented Generation (RAG)**—a fusion of data retrieval and text generation. RAG offers the luxury of adaptability, bypassing the tediousness of full-scale model overhauls.

This repository demystifies the union of pgvector with Amazon Aurora PostgreSQL and the prowess of Titan LLMs, brought to life by Amazon Bedrock, under the RAG paradigm. Experience RAG's adaptability in extracting content from a myriad of sources using LangChain connectors and its knack for context-aware prompt enrichment. Additionally, discover the benefits of cataloging chat histories, which not only evolves your FAQ repository but also slashes expenses by reducing LLM callbacks. A hallmark of this toolkit is its dexterity in engaging with an array of document types—from PDFs and videos to slideshows—making it a versatile asset in diverse informational landscapes.

![Preview](data_search.gif)

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
    virtualenv data-search-env
    ```

4. Activate the environment:
    ```bash
    source data-search-env/bin/activate 
    ```

### **3. Installing Dependencies**

With your virtual environment active, install the necessary packages:

```bash
pip install -r requirements.txt
```

This command installs all dependencies from the `requirements.txt` file into your `data-search-env` environment.

### **4. Usage**

To launch the application:

1. Ensure the dependencies are installed and your `.env` file has the Aurora PostgreSQL DB details.

2. Install the `pgvector` extension on your Aurora PostgreSQL DB cluster:
   ```sql
   CREATE EXTENSION vector;
   ```

3. Update the `app.py` file and modify the code with your S3 bucket name 
    ```python
    # Change the bucket name with your bucket name
    response = s3_client.list_objects_v2(Bucket='aurora-genai-2023', Prefix='documentEmbeddings/') 
    ```
4. Launch the application using Streamlit:
   ```bash
   data-search-env/bin/python -m streamlit run app.py 
   ```

5. Your default web browser will open, showcasing the application interface.

6. Follow the on-screen instructions to load your data and start asking questions.
