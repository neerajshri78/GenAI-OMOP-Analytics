# GenAI-OMOP-Analytics

**Azure Open AI – Text to SQL Using Search Index -  RAG Framework**

![image](https://github.com/user-attachments/assets/a811e7f5-3a02-449b-9405-576e9401b9cf)

 

 

 


 
Create Azure AI Hub
 

 

 

Launch AI Studio

 





 

Create a New Project

 


 

Deploy GPT-4o Model

 


 

Model deployment confirmation
 






Apply RAG – Bring your own Data

 

 




 

 




 

 

 


 


 



 	

{
  "data_sources": [
    {
      "type": "azure_search",
      "parameters": {
        "filter": null,
        "endpoint": "'$search_endpoint'",
        "index_name": "omopindex",
        "semantic_configuration": "azureml-default",
        "authentication": {
          "type": "api_key",
          "key": "oBA2nFjRVhi5wqAapbYUyxbQ2XBg1bUI8LftiLBKksAzSeBfqmuh"
        },
        "embedding_dependency": {
          "type": "endpoint",
          "endpoint": "https://myailearninghu0090068575.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-07-01-preview",
          "authentication": {
            "type": "api_key",
            "key": "399a4dd33302441dadf3408e4df3b279"
          }
        },
        "query_type": "vector_simple_hybrid",
        "in_scope": false,
        "role_information": "You are an AI assistant that helps people find information.",
        "strictness": 3,
        "top_n_documents": 5,
        "key": "'$search_key'",
        "indexName": "'$search_index'"
      }
    }
  ],
  "messages": [
    {
      "role": "system",
      "content": "You are an AI assistant that helps people find information."
    },
    {
      "role": "user",
      "content": "Provide counts of Male and Female patients with over 50 years of age and have been diagnosed with Acute bacterial sinusitis"
    },
    {
      "role": "assistant",
      "content": "To provide the counts of male and female patients over 50 years of age who have been diagnosed with Acute bacterial sinusitis, you can use the following SQL query:\n\n```sql\nSELECT\n    gender_concept.concept_name AS gender_name,\n    COUNT(*)\nFROM\n    condition_occurrence co,\n    concept c,\n    person p,\n    concept gender_concept\nWHERE\n    co.condition_concept_id = c.concept_id\n    AND co.person_id = p.person_id\n    AND p.gender_concept_id = gender_concept.concept_id\n    AND gender_concept.concept_class_id = 'Gender'\n    AND TIMESTAMPDIFF(YEAR, p.birth_datetime, CURDATE()) > 50\n    AND c.concept_name like '%Acute bacterial sinusitis%'\nGROUP BY gender_concept.concept_name;\n```\n\nThis query will return the counts of male and female patients who are over 50 years old and have been diagnosed with Acute bacterial sinusitis [doc1]."
    },
    {
      "role": "user",
      "content": "Provide counts of Female patients with over 20 years of age and have been diagnosed with Type 2 Diabetes and were admitted in the hospital recently"
    },
    {
      "role": "assistant",
      "content": "To provide the counts of female patients over 20 years of age who have been diagnosed with Type 2 Diabetes and were admitted to the hospital recently, you can use the following SQL query:\n\n```sql\nSELECT\n    COUNT(*) AS female_patient_count\nFROM\n    condition_occurrence co\n    JOIN concept c ON co.condition_concept_id = c.concept_id\n    JOIN person p ON co.person_id = p.person_id\n    JOIN visit_occurrence vo ON co.visit_occurrence_id = vo.visit_occurrence_id\n    JOIN concept gender_concept ON p.gender_concept_id = gender_concept.concept_id\nWHERE\n    c.concept_name LIKE '%Type 2 Diabetes%'\n    AND gender_concept.concept_name = 'Female'\n    AND TIMESTAMPDIFF(YEAR, p.birth_datetime, CURDATE()) > 20\n    AND vo.visit_start_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)\n    AND vo.visit_concept_id IN (\n        SELECT concept_id\n        FROM concept\n        WHERE concept_class_id = 'Visit'\n        AND concept_name = 'Inpatient Visit'\n    );\n```\n\nThis query performs the following steps:\n\n1. Joins the `condition_occurrence`, `concept`, `person`, `visit_occurrence`, and `concept` tables.\n2. Filters for female patients diagnosed with Type 2 Diabetes.\n3. Ensures patients are over 20 years of age.\n4. Checks if the hospital admission occurred recently (within the last year).\n5. Ensures the visit is classified as an inpatient visit.\n\nThis should give you the count of female patients with the specified criteria [doc1]."
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800,
  "stop": null,
  "stream": true,
  "past_messages": 10,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "azureSearchEndpoint": "https://undefined.search.windows.net",
  "azureSearchKey": "***"
}






