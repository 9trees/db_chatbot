from connect_to_db import connectToDigitalOcean
import pandas as pd
from T5SQLConnector import T5SQLConnector
from SQLQueryParser import SQLQueryParser
#video
class DBChatBot:
    def __init__(self):
        self.T5SQLConnector = T5SQLConnector()
        self.dbConnection = connectToDigitalOcean()
        self.sqlParser = SQLQueryParser()

    def askMeAnything(self, question):
        sqlQuery = self.T5SQLConnector.runModel(question)
        cleanQuery = self.sqlParser.parseQuery(sqlQuery)
        dataFrame = pd.read_sql(cleanQuery, con=connectToDigitalOcean())
        columnName = list(dataFrame.columns)[0]
        if len(dataFrame) == 1:
            print(dataFrame.iloc[0][columnName])
        else:
            print(dataFrame)


chatbot = DBChatBot()
#video

# chatbot.askMeAnything('how many DTs are of Siemens make?')
# chatbot.askMeAnything('how many DTs are of BDI make?')
# chatbot.askMeAnything('How many Transformers in my area have new alerts today?')
# chatbot.askMeAnything('How many DTs have been manufactured between the years 1995 to 1999?')
# chatbot.askMeAnything('how many transformers having 300 load ?')
# chatbot.askMeAnything('list all the alerts?')
# chatbot.askMeAnything('list all the alerts which are pending?')
chatbot.askMeAnything('list all the  Dt for alerts which are pending?')
