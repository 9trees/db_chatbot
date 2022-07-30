from connect_to_db import connectToDigitalOcean
import pandas as pd
from T5SQLConnector import T5SQLConnector


class DBChatBot:

    def __init__(self):
        self.T5SQLConnector = T5SQLConnector()
        self.dbConnection = connectToDigitalOcean()

    def askMeAnything(self,question):
        sqlQuery = self.T5SQLConnector.runModel(question)

        dataFrame = pd.read_sql(sqlQuery, con=connectToDigitalOcean())

