# DB Chat Bot connected to the Database and integrated with the NLP2SQL model

## 1. Objective and Scope 
- The customer-to-database connection is hard to bypass without SQL knowledge to run the queries and infer the data 
- In order to solve that, we need to establish a connecting adopter which can act as a chatbot which can get the insights or data from the database to the user front end with natural language queries.  
- The major blocker is building an ML model that can convert NLP to SQL queries with concrete accuracy 
- We came up with a multilayer python modelling which can take a use of pretrained NLP2SQL model and validate the SQL queries by post-processing and validating the NLP by preprocessing methodologies. 
