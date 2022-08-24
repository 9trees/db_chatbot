import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd


class RecommendationModule:
    def __init__(self):
        self.NLP2SQLPreLoadedData = pd.read_csv(r"dependency_files\NLP_SQL_Preloaded_data.csv")
        self.NLP2SQLPreLoadedData.Question = self.NLP2SQLPreLoadedData.Question.apply( lambda x: x.lower())
        self.questionsList = list(self.NLP2SQLPreLoadedData.Question)
        self.NLP2SQLPreLoadedDataJSON = {}
        for row in self.NLP2SQLPreLoadedData.itertuples():
            self.NLP2SQLPreLoadedDataJSON[row.Question] = row.Sql
        self.tokenizedQuestion = [word_tokenize(i) for i in self.questionsList]
        self.sw = stopwords.words('english')
        self.tokenizedQuestionSet = [{w for w in i if not w in self.sw} for i in self.tokenizedQuestion]

    def suggestTheQuestion(self, question, needType='cache'):
        # tokenization
        X_list = word_tokenize(question)

        # remove stop words from the string
        X_set = {w for w in X_list if not w in self.sw}

        similarityScore = {}
        for Y_set in range(len(self.questionsList)):
            l1 = []
            l2 = []
            # form a set containing keywords of both strings
            rvector = X_set.union(self.tokenizedQuestionSet[Y_set])
            for w in rvector:
                if w in X_set:
                    l1.append(1)  # create a vector
                else:
                    l1.append(0)
                if w in self.tokenizedQuestionSet[Y_set]:
                    l2.append(1)
                else:
                    l2.append(0)

            c = 0
            # cosine formula
            for i in range(len(rvector)):
                c += l1[i] * l2[i]

            cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
            similarityScore.update({self.questionsList[Y_set]: cosine})

        if needType == 'cache':
            if max(similarityScore.values()) > 0.78:
                # print(similarityScore)
                return self.NLP2SQLPreLoadedDataJSON[max(similarityScore.items(), key=lambda k: k[1])[0]]
            else:
                pass
        else:
            if max(similarityScore.values()) > 0.65:
                # print(similarityScore)
                return max(similarityScore.items(), key=lambda k: k[1])[0]
            else:
                pass

# a = RecommendationModule()
# b = a.suggestTheQuestion('how many transformers having load 300KV?')
