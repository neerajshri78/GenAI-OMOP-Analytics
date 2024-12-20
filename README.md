# GenAI-OMOP-Analytics

**RAG Documents for Azure AI Search Index**
1. OMOP_Table_Column_Details.docx
2. OMOP_SQL_Queries.docx

Please see the screenshots from Azure AI below on how to create a search index using this dataset.

**Python code files**
1. OMOP_Text_to_SQL.py - This code utilizes chat completions API from Open AI for the model hosted in Azure, search index , system message and prompt among other parameters are passed as parameters.
2. OMOP_Text_to_SQL_frontend.py - This code provides the same SQL accuracy as above code just that it utilizes langchain API and streamlit for an interface. Its meant for learning langchain and how to build UI using streamlit.
3. OMOP_Text_to_SQL_DBInsigts.py - This is an extension of the OMOP_Text_to_SQL_frontend.py as it automatically connects to a MySQL database like SInglestore and executes the query and provides the output in the steamlit based UI. 

**OMOP (Observational Medical Outcome Partnership) Database Test data**
 https://github.com/OHDSI/EunomiaDatasets/tree/main/datasets/GiBleed
 
**OMOP DB Table creation script**
[OMOP_DDL_MYSQL.sql - This is the OMOP Database table screation script (](https://github.com/OHDSI/CommonDataModel/tree/v5.4.0/inst/ddl/5.4) 

**Azure Open AI – Text to SQL Using Search Index -  RAG Framework**

https://github.com/user-attachments/assets/a8c7fd0d-a247-4083-9762-cd19911e9c00

**Azure AI End to Ens Setup**

**Step 1 - Create Azure AI Service**

![image](https://github.com/user-attachments/assets/a811e7f5-3a02-449b-9405-576e9401b9cf)

 ![image](https://github.com/user-attachments/assets/fd69e7d2-d323-4565-bf1e-92b4c0e1d4aa)

 ![image](https://github.com/user-attachments/assets/8a1d511c-1891-42b0-91e8-c4517448b961)

![image](https://github.com/user-attachments/assets/2028e336-6324-46d1-b9a9-fbbcbc4d440c)

![image](https://github.com/user-attachments/assets/a433437f-d37e-4d98-ab6d-4ad1dbe04935)

**Step 2 - Create Azure AI Hub**
![image](https://github.com/user-attachments/assets/f5be014c-c160-4e7c-a7c5-61c47f7b6c81)

![image](https://github.com/user-attachments/assets/8367d2bf-35dd-415e-8159-a103bb5d686b)

**Step 3 - Launch AI Studio**
![image](https://github.com/user-attachments/assets/5f63b2e4-faff-4154-939a-41739f06255c)

**Step 4 - Create a New Project**
![image](https://github.com/user-attachments/assets/2b5e3525-7728-4bae-a4dd-3024e6a4aad3)


![image](https://github.com/user-attachments/assets/f685474f-e886-47e5-8597-51b3c0f01d9c)

![image](https://github.com/user-attachments/assets/d45b56ee-762d-4f68-a7b0-dd0583fe7379)

**Step 5 - Deploy GPT-4o Model**
![image](https://github.com/user-attachments/assets/e0bc2442-074b-4594-9877-656f19e3d14d)
![image](https://github.com/user-attachments/assets/e26f9571-d3e5-49cd-ac06-5d5c6ce45cab)

**Step 6 - Model deployment confirmation & API End Point**
![image](https://github.com/user-attachments/assets/26d950b7-d1c2-4da9-9440-ef163d9bd79b)

**Step 7 - Apply RAG – Bring your own Data**
![image](https://github.com/user-attachments/assets/863b2fb0-6517-4e0b-818c-d6b29ee93bff)

**Select Upload Files and Upload the word documents - OMOP_Table_Descriptions.docx & OMOP_SQL_Queries
**
OMOP_Table_Descriptions.docx - This document contains the OMOP table and column information
OMOP_SQL_Queries - This document containts the sample SQL Queries that will be used to provide additional context to the model

![image](https://github.com/user-attachments/assets/fb11d9a4-4331-4980-9a5f-4b48ee690e67)

![image](https://github.com/user-attachments/assets/863ed285-76e6-48ef-8c8d-52774cd9abdb)

![image](https://github.com/user-attachments/assets/602c2f84-8853-4b6c-85c3-0852c3bcaeb9)

Add the Index you have created and ensure to uncheck - Limit Responses to your data.
If unchecked then the LLM will merely work as a glorified search and will only provide SQLs that are part of the context
![image](https://github.com/user-attachments/assets/a13363f0-3700-4ad7-bf98-673af2abab3d)

**Step 8 - Your NLP to SQL Gen AI Application is ready**

Please make sure to provide a system message that will dictate the behaviour of the application
For example : "You are an AI assistant that helps people find generate SQL Queries from their prompts"
![image](https://github.com/user-attachments/assets/82e1b914-5289-4529-a312-c7b064b511af)

![image](https://github.com/user-attachments/assets/fdc87905-8fec-4dda-b2c7-886a45a14a33)

























