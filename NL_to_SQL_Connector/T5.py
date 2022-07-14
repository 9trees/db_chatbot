from transformers import AutoModelWithLMHead, AutoTokenizer
import tqdm
import pandas as pd
import json

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-wikiSQL")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-wikiSQL")


def get_sql(query):
    input_text = "translate English to SQL: %s </s>" % query
    features = tokenizer([input_text], return_tensors='pt')

    output = model.generate(input_ids=features['input_ids'],
                            attention_mask=features['attention_mask'])

    return tokenizer.decode(output[0])


with open('input_queries.txt') as f:
    lines = f.readlines()

outputJSON = {}
for query in tqdm.tqdm(lines):
    query = query.replace('\n', '')
    outputJSON[query] = get_sql(query)

with open('SQL_Query_output.json', 'w') as f:
    json.dump(outputJSON, f)

outputString = ''
for i, j in outputJSON.items():
    outputString += "input: " + i + '\n' + '==> Output SQL: ' + j + '\n\n'

with open('SQL_Query_output.txt', 'w') as f:
    f.write(outputString)
