# Amazon Bedrock knowledge base notebooks and code samples 

This repository contains the code used in the blog posts:

- [Web to Wisdom: Transforming Web Content with Amazon Bedrock for Knowledge Bases](https://community.aws/content/2j7MGeRCVUMb00EXlqIi1jk3lUa/web-to-wisdom-transforming-web-content-with-amazon-bedrock-knowledge-bases). 
- [A Developer’s Guide to Advanced Chunking and Parsing with Amazon Bedrock](https://community.aws/content/2jU5zpqh4cal0Lm47MBdRmKLLJ5/a-developer-s-guide-to-advanced-chunking-and-parsing-with-amazon-bedrock)

The blogs explore how to integrate web URL data with Amazon Bedrock to enhance Retrieval-Augmented Generation (RAG) applications and advanced techniques to optimize your data retrieval with Knowledge Bases for Amazon Bedrock's using parsing, chunking and metadata customization.

This repository contains Jupyter notebooks used in these blogs. 

## Overview

The blog post and the accompanying code demonstrate how to:

1. Create a vector store using Amazon OpenSearch Serverless (OSS).
2. Create a Knowledge Base (KB) with Amazon Bedrock.
3. Integrate web URLs as data sources for the KB with advanced chunking and parsing techniques.
4. Use the RetrieveAndGenerate and Retrieve APIs to fetch and generate responses from the KB.

## File Structure

- `KB_Bedrock_Web_URL.ipynb`: Jupyter Notebook containing all the code and steps describing Web URL data srouce with Knowledge Bases for Amazon Bedrock. [Blog](https://community.aws/content/2j7MGeRCVUMb00EXlqIi1jk3lUa/web-to-wisdom-transforming-web-content-with-amazon-bedrock-knowledge-bases)

[![Watch the video](https://img.youtube.com/vi/TIvHx81J1zI/maxresdefault.jpg)](https://www.youtube.com/watch?v=TIvHx81J1zI)

- `KB_Bedrock_Accuracy_Improvement.ipynb` : Jupyter Notebook containing all the code and steps describing accuracy improvement for Knowledge Bases for Amazon Bedrock [Blog](https://community.aws/content/2jU5zpqh4cal0Lm47MBdRmKLLJ5/a-developer-s-guide-to-advanced-chunking-and-parsing-with-amazon-bedrock)

[![Watch the video](https://img.youtube.com/vi/CFyFN0DuO5o/maxresdefault.jpg)](https://www.youtube.com/watch?v=CFyFN0DuO5o)
## Features Demonstrated

1. **Create the Vector Store**:
    - Follow the steps to create OSS policies and collections. 
    - Initialize the OpenSearch client and create the vector index.

2. **Create the Knowledge Base**:
    - Set up the configuration for OpenSearch Serverless, chunking strategy, web URL, and embedding model.
    - Create the Knowledge Base using the configurations.

3. **Create a Web URL/S3 Data Source**: 
    - Associate the created KB with a web URL/S3 data source. [KB_Bedrock_Web_URL.ipynb](./KB_Bedrock_Web_URL.ipynb)
    - Configure the performance improvement features, like chunking. [Accuracy_Improvement.ipynb](./KB_Bedrock_Accuracy_Improvement.ipynb)

4. **Data Sync**:
    - Start the data sync to fetch, preprocess, chunk, and store the S3/web data in the vector store.

5. **Test the Knowledge Base**:
    - Use the RetrieveAndGenerate API to test the KB and generate responses.
    - Use the Retrieve API to fetch relevant context.

## Prerequisites

- AWS account with access to Amazon Bedrock
- Enabled access to required models in region (Anthropic Claude 3 Sonnet and Haiku)
- Python 3.x
- Jupyter Notebook
- Required Python libraries: `boto3`, `opensearch-py` and `retrying`

## Setup

1. Clone this repository
2. Install the required Python libraries
3. Set up your AWS credentials
4. Open the notebooks in Jupyter and follow the instructions within

## Usage

Each notebook contains step-by-step instructions for creating, interacting with, and cleaning up the Bedrock Agents. They include explanations of the code and concepts, making them suitable for both learning and experimentation.

## Important Notes

- These notebooks use features that may be in preview at the time of creation. Check the current status of Amazon Bedrock features before use.
- Remember to run the cleanup cells at the end of each notebook to remove created resources and avoid unnecessary charges.

## Disclaimer

The code in this repository is for demonstration purposes. Ensure you understand the AWS pricing for Bedrock and related services before running these notebooks in your own environment.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.