import streamlit as st
import os
import singlestoredb as s2
import pandas as pd
from openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.retrievers import AzureCognitiveSearchRetriever
from langchain.schema import SystemMessage, HumanMessage

# Azure and OpenAI API setup (you can keep these credentials or use environment variables for security)
endpoint = os.getenv("ENDPOINT_URL", "https://myailearninghu0090068575.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-omop-analytics")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://aisearchserviceforlearning.search.windows.net/")
search_key = os.getenv("SEARCH_KEY", "Your Search API Key")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "Your Open API Key")
service_name = "aisearchserviceforlearning"

# SingleStore database connection setup
singlestore_connection_string = os.getenv(
    "SINGLESTORE_CONNECTION_STRING", "user:password@host:port/<Schema Name>"
)

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
    index_name="omopindexnew",
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
st.markdown("<h1 style='color: blue;'>Health Analytics - Natural Language to SQL Query and DB Insights</h1>", unsafe_allow_html=True)

# Ask user for input
st.header("Ask a Question")
question = st.text_input("Enter your question here:")

st.markdown("<style>.stButton>button {background-color: green; color: white;}</style>", unsafe_allow_html=True)

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
                HumanMessage(content=f"Based on the following documents, provide only the SQL query for: {question}\n\n{context}"),
            ]

            # Get the response from the language model
            response = llm(messages)

            # Extract and clean the response (SQL query)
            sql_query = response.content.strip().split('```sql')[1].split('```')[0].strip() if '```sql' in response.content else response.content.strip()

            # Display the response (SQL query)
            st.subheader("Generated SQL Query:")
            st.code(sql_query)

            # Execute the SQL query in SingleStore
            try:
                # Establish the connection
                conn = s2.connect(singlestore_connection_string)
                cur = conn.cursor()

                # Check if the query is a valid SQL statement
                if sql_query.lower().startswith("select"):
                    # Execute the generated SQL query
                    cur.execute(sql_query)
                    rows = cur.fetchall()
                    columns = [desc[0] for desc in cur.description]

                    # Display the results in a tabular format
                    st.subheader("Query Results:")
                    if rows:
                        df = pd.DataFrame(rows, columns=columns)
                        st.dataframe(df)
                    else:
                        st.write("No results returned.")
                else:
                    st.error("The generated query is not a valid SELECT statement.")

                # Close the connection
                cur.close()
                conn.close()
            except Exception as e:
                st.error(f"An error occurred while executing the SQL query: {str(e)}")
    else:
        st.error("Please enter a question.")
