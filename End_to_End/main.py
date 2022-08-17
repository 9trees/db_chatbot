from connect_to_db import connectToDigitalOcean
import pandas as pd
from T5SQLConnector import T5SQLConnector
from SQLQueryParser import SQLQueryParser
from recommendation import RecommendationModule


# video
class DBChatBot:
    def __init__(self):
        self.T5SQLConnector = T5SQLConnector()
        self.dbConnection = connectToDigitalOcean()
        self.sqlParser = SQLQueryParser()
        self.recommender = RecommendationModule()

    def askMeAnything(self, question):
        sqlQuery = self.T5SQLConnector.runModel(question)
        cleanQuery = self.sqlParser.parseQuery(sqlQuery)
        try:
            dataFrame = pd.read_sql(cleanQuery, con=connectToDigitalOcean())
            if len(dataFrame) > 0:
                columnName = list(dataFrame.columns)[0]
                if len(dataFrame) == 1:
                    print(dataFrame.iloc[0][columnName])
                else:
                    print(dataFrame)
        except Exception as e:
            recommendedQuestion = self.recommender.suggestTheQuestion(question)
            if recommendedQuestion:
                userInput = input('==> are you looking for this question below ? (y or n)\n ==> ' + recommendedQuestion)
                if userInput == 'y':
                    sqlQuery = self.T5SQLConnector.runModel(recommendedQuestion)
                    cleanQuery = self.sqlParser.parseQuery(sqlQuery)
                    dataFrame = pd.read_sql(cleanQuery, con=connectToDigitalOcean())
                    if len(dataFrame) > 0:
                        columnName = list(dataFrame.columns)[0]
                        if len(dataFrame) == 1:
                            print(dataFrame.iloc[0][columnName])
                        else:
                            print(dataFrame)
            else:
                print("==> Sorry I didn't understand your question")


chatbot = DBChatBot()
# video

# chatbot.askMeAnything('how many DTs are of Siemens make?')
# chatbot.askMeAnything('how many DTs are of BDI make?')
# chatbot.askMeAnything('How many Transformers in my area have new alerts today?')
# chatbot.askMeAnything('how many transformers having 300 load ?')
# chatbot.askMeAnything('list all the alerts?')
# chatbot.askMeAnything('list all the alerts which are pending?')
# chatbot.askMeAnything('list all the  Dt for alerts status which are pending?')
# chatbot.askMeAnything('list all the DT from Nungampakkam area?')
# chatbot.askMeAnything('list all the DT?')
# chatbot.askMeAnything('total count of alerts?')
chatbot.askMeAnything('how many transformers having load 300KV?')