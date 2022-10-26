from transformers import AutoModelWithLMHead, AutoTokenizer


class T5SQLConnector:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-wikiSQL")
        self.model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-wikiSQL")
        pass

    def runModel(self, query):
        input_text = "translate English to SQL: %s </s>" % query
        features = self.tokenizer([input_text], return_tensors='pt')

        output = self.model.generate(input_ids=features['input_ids'],
                                     attention_mask=features['attention_mask'])

        return self.tokenizer.decode(output[0])


#
a = T5SQLConnector()
print(a.runModel('show the alerts with manufacture names KEL?'))
