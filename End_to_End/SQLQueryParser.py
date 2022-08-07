from utils import configs, logicalReplacements
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
        self.replaceComparisonStrings()
        self.replaceColumnNames()
        self.replaceTableName()
        self.keywordFormatter()
        self.SQLFormatter()
        return self.processedQuery

    def rightAndLeftStrip(self):
        self.processedQuery = self.processedQuery.replace("<pad> ", '').replace("</s>", '')

    def replaceTableName(self):
        tableName = configs['TableName']
        self.processedQuery = self.processedQuery.replace(" TABLE ", " " + tableName + " ")

    def findColumns(self):
        # for tempToken in sqlparse.parse(self.processedQuery)[0].tokens:
        #     if type(tempToken) == sqlparse.sql.Identifier:
        #         self.columnNames.append(tempToken.value)
        #     elif tempToken.is_group and tempToken.tokens[0].value.startswith('WHERE'):
        #         for tempTokenGroup in tempToken.tokens:
        #             if type(tempTokenGroup) == sqlparse.sql.Identifier:
        #                 self.columnNames.append(tempTokenGroup.value)
        #             elif type(tempTokenGroup) == sqlparse.sql.Comparison:
        #                 if type(tempTokenGroup.tokens[0]) == sqlparse.sql.Identifier:
        #                     self.columnNames.append(tempTokenGroup.tokens[0].value)

        sqlStatement = sqlparse.format(self.processedQuery, reindent=True,
                                       keyword_case='upper', comma_first=True, identifier_case='lower')

        for words in sqlStatement.replace('\n', ' ').split('=')[0].split(' '):
            if words.islower():
                self.columnNames.append(words)

        self.columnNames = list(set(self.columnNames))

    def replaceColumnNames(self):

        replaceList = []
        for column in self.columnNames:
            replaceList.append(self.fuzzyMatcher.cosineSimilarity(column))

        for i in replaceList:
            self.processedQuery = self.processedQuery.replace(list(i.keys())[0], list(i.values())[0])

        for word, initial in logicalReplacements.items():
            self.processedQuery = re.sub(r'\b' + word + r'\b', initial, self.processedQuery.upper())

    def replaceComparisonStrings(self):
        sqlStatement = sqlparse.format(self.processedQuery,
                                       keyword_case='upper', comma_first=True)

        comparisonStrings = []
        for words in sqlStatement.split('= ')[1].split(' '):
            if not words.isdigit():
                comparisonStrings.append(words)

        for words in comparisonStrings:
            self.processedQuery = self.processedQuery.replace(words,"'"+words+"'")

    def SQLFormatter(self):
        self.processedQuery = sqlparse.format(self.processedQuery, comma_first=True)

    def keywordFormatter(self):
        if ' COUNT ' in self.processedQuery:
            word = self.processedQuery.split(' COUNT ')[1].split(' ')[0]
            self.processedQuery = self.processedQuery.replace(word,"("+word+")")





# a = SQLQueryParser()
# g = a.parseQuery('<pad> SELECT COUNT DT FROM table WHERE Manufacturer = Siemens</s>')
