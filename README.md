# DB Chat Bot connected to the Database and integrated with the NLP2SQL model

## 1. Objective and Scope 
- The customer-to-database connection is hard to bypass without SQL knowledge to run the queries and infer the data 
- In order to solve that, we need to establish a connecting adopter which can act as a chatbot which can get the insights or data from the database to the user front end with natural language queries.  
- The major blocker is building an ML model that can convert NLP to SQL queries with concrete accuracy 
- We came up with a multilayer python modelling which can take a use of pretrained NLP2SQL model and validate the SQL queries by post-processing and validating the NLP by preprocessing methodologies. 


## 2. DB Chatbot Diagram
<img width="1035" alt="Screenshot 2022-12-13 at 22 39 18" src="https://user-images.githubusercontent.com/8901901/207460122-328e521a-ce20-4466-a49f-8fc4e664a8c8.png">



## 3. How to run the Module
