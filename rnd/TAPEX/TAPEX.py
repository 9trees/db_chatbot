from transformers import TapexTokenizer, BartForConditionalGeneration
import pandas as pd
import sqlite3

def connectToSqliteDB():
    return sqlite3.connect(r"C:\Tamil\temp\db_chatbot\django_connecter\pythonsqlite.db")

tokenizer = TapexTokenizer.from_pretrained("microsoft/tapex-large-sql-execution")
model = BartForConditionalGeneration.from_pretrained("microsoft/tapex-large-sql-execution")

data = {
    "year": [1896, 1900, 1904, 2004, 2008, 2012],
    "city": ["athens", "paris", "st. louis", "athens", "beijing", "london"]
}
# table = pd.DataFrame.from_dict(data)
table = pd.read_sql("select * from polls_events", con=connectToSqliteDB())


# tapex accepts uncased input since it is pre-trained on the uncased corpus
query = "list all the mainids"
encoding = tokenizer(table=table, query=query, return_tensors="pt")

outputs = model.generate(**encoding)

print(tokenizer.batch_decode(outputs, skip_special_tokens=True))