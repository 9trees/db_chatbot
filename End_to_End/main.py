from connect_to_db import connectToDigitalOcean, connectToSqliteDB
import pandas as pd
from T5SQLConnector import T5SQLConnector
from SQLQueryParser import SQLQueryParser
from recommendation import RecommendationModule
from questionParser import QuestionParser
from utils import measure
import dummylog
from datetime import datetime


# video
class DBChatBot:
    def __init__(self):
        self.logger = dummylog.DummyLog(log_name=datetime.now().strftime('%d-%m-%Y-%H-%M.log'))
        self.T5SQLConnector = T5SQLConnector()
        self.dbConnection = connectToSqliteDB()
        self.sqlParser = SQLQueryParser()
        self.recommender = RecommendationModule()
        self.questionParser = QuestionParser()

    @measure
    def askMeAnything(self, question):
        # cachedQuestion = self.recommender.suggestTheQuestion(question.lower(), needType='cache')
        # if cachedQuestion:
        #     cleanQuery = cachedQuestion
        # else:
        self.logger.logger.info('Question Asked                   ==> ' + question)
        question = self.questionParser.checkAlternateNames(question)
        self.logger.logger.info('Modifed Question by descriptions ==> ' + question)
        sqlQuery = self.T5SQLConnector.runModel(question)
        cleanQuery = self.sqlParser.parseQuery(sqlQuery)
        try:
            dataFrame = pd.read_sql(cleanQuery, con=self.dbConnection)
            if len(dataFrame) > 0:
                columnName = list(dataFrame.columns)[0]
                if len(dataFrame) == 1:
                    print("\033[1;34m", dataFrame.iloc[0][columnName])
                    self.logger.logger.info('Answer                           ==> ' + str(dataFrame.iloc[0][columnName]))
                else:
                    self.logger.logger.info('Answer                           ==> \n' + str(dataFrame))
                    print("\033[1;34m", dataFrame)
        except:
            recommendedQuestion = self.recommender.suggestTheQuestion(question.lower(), needType='recommendedQuestion')
            if recommendedQuestion:
                userInput = input('==> are you looking for this question below ? (y or n)\n ==> ' + recommendedQuestion)
                if userInput == 'y':
                    sqlQuery = self.T5SQLConnector.runModel(recommendedQuestion)
                    cleanQuery = self.sqlParser.parseQuery(sqlQuery)
                    dataFrame = pd.read_sql(cleanQuery, con=connectToSqliteDB())
                    if len(dataFrame) > 0:
                        columnName = list(dataFrame.columns)[0]
                        if len(dataFrame) == 1:
                            print("\033[34m", str(dataFrame.iloc[0][columnName]))
                        else:
                            print("\033[1;34m", dataFrame)
            else:
                print("==> Sorry I didn't understand your question")


chatbot = DBChatBot()
# video
# chatbot.askMeAnything('what is the maxiumum value of I_Y?')
# chatbot.askMeAnything('show me the minimum frequency?')
# chatbot.askMeAnything('count timestamp with manufacture name with KEL')
# chatbot.askMeAnything('show the timestamp with manufacturename as KEL')
# chatbot.askMeAnything('list all V_R with Chennai Region')
# chatbot.askMeAnything('show me all the timestamp')
# chatbot.askMeAnything('how many DTs are of kel make')
# chatbot.askMeAnything('how many DTs are of BDI make')
# chatbot.askMeAnything('How many Transformers in my area have new alerts today')
# chatbot.askMeAnything('how many transformers having 300 load ')
# chatbot.askMeAnything('list all the alerts')
# chatbot.askMeAnything('list all the alerts which are pending')
# chatbot.askMeAnything('list all the  Dt for alerts status which are pending')
# chatbot.askMeAnything('list all the DT from Nungampakkam area')
# chatbot.askMeAnything('list all the DT')
# chatbot.askMeAnything('total count of V_R')
# chatbot.askMeAnything('how many transformers having load 300KV')
# chatbot.askMeAnything('How many DTs have been manufactured between the years 1995 to 1999')
# chatbot.askMeAnything('How many DTs have been manufactured on 1995')
# chatbot.askMeAnything('show me all the data')
# chatbot.askMeAnything('what are the types of make available')
# chatbot.askMeAnything('how many types of alerts available')
# chatbot.askMeAnything('total count the frequency with 49')
# chatbot.askMeAnything('total count wcurret with 49')
# chatbot.askMeAnything('get timestamp with V_R = 239')
# chatbot.askMeAnything('get I_R with V_R 231')
chatbot.askMeAnything('list all r phase volt with Chennai Region')
