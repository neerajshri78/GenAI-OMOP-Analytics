import streamlit as st
import os
from openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.retrievers import AzureCognitiveSearchRetriever
from langchain.schema import SystemMessage, HumanMessage

# Azure and OpenAI API setup (you can keep these credentials or use environment variables for security)
endpoint = os.getenv("ENDPOINT_URL", "https://myailearninghu0090068575.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-omop-analytics")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://aisearchserviceforlearning.search.windows.net/")
search_key = os.getenv("SEARCH_KEY", "oBA2nFjRVhi5wqAapbYUyxbQ2XBg1bUI8LftiLBKksAzSeBfqmuh")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "399a4dd33302441dadf3408e4df3b279")
service_name = "aisearchserviceforlearning"

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

# Initialize the retriever for cognitive search
retriever = AzureCognitiveSearchRetriever(
    service_name=service_name,
    api_key=search_key,
    index_name="omopindex1",
)

# Initialize the AzureChatOpenAI model
llm = AzureChatOpenAI(
    azure_endpoint=endpoint,  # Use `azure_endpoint` instead of `openai_api_base`
    openai_api_version="2024-05-01-preview",
    deployment_name=deployment,
    openai_api_key=subscription_key,
    openai_api_type="azure",
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
)

# Streamlit UI layout
st.title("Natural Language to SQL Query Generator")
st.sidebar.header("Settings")

# Ask user for input
st.header("Ask a Question")
question = st.text_input("Enter your question here:")

if st.button("Generate SQL Query"):
    if question:
        # Use the retriever to get relevant documents based on the user's question
        documents = retriever.get_relevant_documents(question)

        # Check if documents are retrieved
        if not documents:
            st.error("No relevant documents found.")
        else:
            # Combine the documents into context
            context = "\n".join([doc.page_content for doc in documents])

            # Prepare the messages for the language model
            messages = [
                SystemMessage(content="You are an AI assistant that helps people find information."),
                HumanMessage(content=f"Based on the following documents, can you provide a SQL query for: {question}\n\n{context}"),
            ]

            # Get the response from the language model
            response = llm(messages)

            # Display the response (SQL query)
            st.subheader("Generated SQL Query:")
            st.code(response.content)
    else:
        st.error("Please enter a question.")
