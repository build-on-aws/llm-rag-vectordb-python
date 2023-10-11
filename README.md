<style>
.center-text h1 {
  transition: color 0.5s;
}

.center-text h1:hover {
  color: blue;
}
</style>

<p align="center" class="center-text">
  <h1>☁️🐍 **Getting Started with Amazon Bedrock, RAG, and Vector database in Python**</h1>
</p>


In this repository, you'll find sample applications and tutorials that showcase the power of **Amazon Bedrock with Python**. These resources are designed to help Python developers understand how to harness **Amazon Bedrock** in building generative AI-enabled applications. You'll also discover how to integrate Bedrock with vector databases using `RAG (Retrieval-augmented generation)`, and services like Amazon Aurora, RDS, and OpenSearch. Additionally, get insights into using `langchain` and `streamlit` to create applications that demonstrate your experiments effectively.

### <span style="color:purple">Integrated Fullstack Showcase: Harnessing Stable Diffusion AI using Amazon Bedrock</span>

This application utilize the Stable Diffusion AI model using Amazon Bedrock. 

[Check out the live demo here](https://main.d1zbstr6nltjhw.amplifyapp.com/)

![](image-generation-node-js-app/img/img-gen.gif)

**Key Features**:
- Integrates seamlessly with Lambda, API Gateway, Bedrock and Amplify
- End to end application is deployed using Serverless stack.

📖 [Detailed Guide & Setup](image-generation-node-js-app//README.md)

### <span style="color:purple">Resume Screening App using Amazon Bedrock and Amazon Aurora (`pgvector`)</span>

This application streamlines the resume screening process based on specific job descriptions. 

![Resume Screening Preview](resume-screening-app/Resume-Screener.gif)

**Key Features**:
- Integrates seamlessly with Streamlit for an intuitive web-based user interface.
- Utilizes Amazon Bedrock and Aurora, ensuring efficient and scalable backend operations.

📖 [Detailed Guide & Setup](resume-screening-app/README.md)

### <span style="color:purple">Building Bonds: Harnessing Ice-Breakers for Introductions</span>

Transform your introductory sessions with this application. Input a name, and watch as the app fetches the LinkedIn profile of the person, providing a succinct summary and engaging ice-breaker facts. 

![Building Bonds Preview](building-bonds/boundbuilding.gif)

**Key Features**:
- Retrieve LinkedIn profiles instantly using just a name.
- Generate automated career summaries and ice-breaking facts powered by Amazon Bedrock and LangChain.

📖 [Detailed Guide & Setup](building-bonds/README.md)

### <span style="color:purple">Data Analysis Tool using Amazon Bedrock</span>

Build a streamlined Streamlit application to analyze your CSV data. This guide walks you through the process of setting up and running the application.

![Preview](data-analysis-tool/da.gif)

**Key Features**:
- Streamlit: For a smooth web application interface.
- Langchain: Integrated for advanced functionalities.
- AWS Services: Harness the power of Amazon's cloud services, especially Amazon Bedrock.

📖 [Detailed Guide & Setup](data-analysis-tool/README.md)

## **Getting Started** 

1. Clone this repository to your local machine.

2. Move to the specific project directory for detailed setup instructions:
    - For **Resume Screening App**: Follow the [README guide](resume-screening-app/README.md).
    - For **Building Bonds**: Check out the [README guide](building-bonds/README.md).
    - For **Stable Diffusion AI App**: Check out the [README guide](image-generation-node-js-app/README.md).
    - For **Data Analysis Tool**: Follow the [README guide](llm-rag-vectordb-python/data-analysis-tool/README.md).

3. For each project, ensure you set up a virtual environment, populate the `.env` files, and install the necessary dependencies. Details are available in the respective READMEs.

4. Launch your desired Streamlit application and explore!

## **Security**

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## **License**

This library is licensed under the MIT-0 License. See the LICENSE file.

