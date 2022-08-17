import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class RecommendationModule:
    def __init__(self):
        self.questionsList = ['how many DTs are of Siemens make?', 'how many DTs are of BDI make?',
                              'How many DTs have been manufactured between the years 1995 to 1999?',
                              'how many transformers having 300 load ?',
                              'list all the alerts which are pending?',
                              'list all the Alerts?',
                              'list all the alerts which are pending?',
                              'list all the  Dt for alerts status which are pending?',
                              'list all the DT from Nungampakkam area?',
                              'list all the DT?',
                              'total count of alerts?'
                              ]
        self.tokenizedQuestion = [word_tokenize(i) for i in self.questionsList]
        self.sw = stopwords.words('english')
        self.tokenizedQuestionSet = [{w for w in i if not w in self.sw} for i in self.tokenizedQuestion]

    def suggestTheQuestion(self, question):
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

        if max(similarityScore.values()) > 0.6:
            # print(similarityScore)
            return max(similarityScore.items(), key = lambda k : k[1])[0]
        else:
            pass


# a = RecommendationModule()
# b = a.suggestTheQuestion('how many transformers having load 300KV?')
