# Building Bonds: The Power of Ice-Breakers

![Application Banner](/llm-rag-vectordb-python/building-bonds/boundbuilding.gif)

Welcome to **Building Bonds**, a Streamlit application that harnesses the strengths of Amazon Bedrock and LangChain. Make your introductions more memorable! Enter a name, and let our application search for their LinkedIn profile, then provide you with a concise summary and ice-breaking facts about that person.

## Features

1. **Instant LinkedIn Search**: Just provide a name, and the application will try to locate their LinkedIn profile from the internet.
2. **Automated Summary**: With the capabilities of Amazon Bedrock and LangChain, receive a detailed overview of the person's career and accomplishments.
3. **Ice-Breaker Facts**: Start your conversation with a bang! Learn unique and engaging facts related to the individual.

## How It Works

The magic behind **Building Bonds**:

- **Amazon Bedrock**: Empowers our system to deep dive into data and bring out meaningful insights.
- **LangChain**: Assists with linguistic processing, allowing the app to draw a clear and engaging summary from LinkedIn details.

## Getting Started

### **1. Pre-requisites** 

- Clone the repository to your local machine.
- Create a `.env` file in the project directory using `env.example` as a reference. Populate the `.env` file with your Proxycurl and Serpa API Key details:

    ```bash
    PROXYCURL_API_KEY=<YOUR API KEY>
    SERPAPI_API_KEY=<YOUR API KEY>
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
    virtualenv bb-env
    ```

4. Activate the environment:
    ```bash
    source bb-env/bin/activate 
    ```

### **3. Installing Dependencies**

With your virtual environment active, install the necessary packages:

```bash
pip install -r requirements.txt
```

This command installs all dependencies from the `requirements.txt` file into your `rs-env` environment.

### **4. Usage**

Launch the application using Streamlit:

   ```bash
   streamlit run app.py
   ```
