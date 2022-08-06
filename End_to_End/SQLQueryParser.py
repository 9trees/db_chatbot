from utils import configs
from FuzzyMatcher import FuzzyMatch
import sqlparse
import re


class SQLQueryParser:

    def __init__(self):
        self.fuzzyMatcher = FuzzyMatch()
        self.parsedTokens = None
        self.processedQuery = None
        self.columnNames = []

    def parseQuery(self, query):
        self.processedQuery = query
        self.rightAndLeftStrip()
        self.findColumns()
        self.replaceTableName()
        self.replaceColumnNames()
        return self.processedQuery

    def rightAndLeftStrip(self):
        self.processedQuery = self.processedQuery.replace("<pad> ", '').replace("</s>", '')

    def replaceTableName(self):
        tableName = configs['TableName']
        self.processedQuery = self.processedQuery.replace(" table ", " " + tableName + " ")

    def findColumns(self):
        for tempToken in sqlparse.parse(self.processedQuery)[0].tokens:
            if type(tempToken) == sqlparse.sql.Identifier:
                self.columnNames.append(tempToken.value)
            elif tempToken.is_group and tempToken.tokens[0].value.startswith('WHERE'):
                for tempTokenGroup in tempToken.tokens:
                    if type(tempTokenGroup) == sqlparse.sql.Identifier:
                        self.columnNames.append(tempTokenGroup.value)
                    elif type(tempTokenGroup) == sqlparse.sql.Comparison:
                        if type(tempTokenGroup.tokens[0]) == sqlparse.sql.Identifier:
                            self.columnNames.append(tempTokenGroup.tokens[0].value)

        self.columnNames = list(set(self.columnNames))

    def replaceColumnNames(self):

        replaceList = []
        for column in self.columnNames:
            replaceList.append(self.fuzzyMatcher.cosineSimilarity(column))

        print(replaceList)

        for i in replaceList:
            self.processedQuery = self.processedQuery.replace(list(i.keys())[0], list(i.values())[0])


a = SQLQueryParser()
g = a.parseQuery('<pad> SELECT COUNT DT FROM table WHERE Manufacturer = Siemens</s>')
