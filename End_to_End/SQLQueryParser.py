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
        self.values = []

    def parseQuery(self, query):
        self.processedQuery = query
        print("Query: " ,self.processedQuery)
        self.rightAndLeftStrip()
        print("Query strip: ", self.processedQuery)
        self.replaceComparisonStrings()
        print("Query replace Comparison Strings: ", self.processedQuery)
        self.keywordFormatter()
        print("Query keyword Formatter: ", self.processedQuery)
        self.findColumns()
        self.replaceColumnNames()
        print("Query replaced columns: ", self.processedQuery)
        self.replaceTableName()
        print("Query replaced table names: ", self.processedQuery)
        self.SQLFormatter()
        print("Final Query: ", self.processedQuery)
        return self.processedQuery

    def rightAndLeftStrip(self):
        self.processedQuery = self.processedQuery.replace("<pad> ", '').replace("</s>", '')

    def replaceTableName(self):
        tableName = configs['TableName']
        self.processedQuery = self.processedQuery.replace("TABLE", " " + tableName + " ")

    def findColumns(self):
        tokenizedQuery = sqlparse.parse(self.processedQuery)[0].tokens
        for parent in tokenizedQuery:
            if type(parent) == sqlparse.sql.Identifier and parent.is_group:
                self.columnNames.append(parent.value)
            elif parent.is_group:
                for child in parent.tokens:
                    if type(child) == sqlparse.sql.Identifier and child.is_group:
                        self.columnNames.append(child.value)
                    elif not child.value.startswith('WHERE') and child.is_keyword and \
                            child.value not in ['AND','OR','BETWEEN','IS','NULL', 'TO']:
                        self.columnNames.append(child.value)
                    elif type(child) == sqlparse.sql.Comparison:
                        for comChild in child.tokens:
                            if type(comChild) == sqlparse.sql.Identifier and comChild.is_group:
                                self.columnNames.append(comChild.value)
                            elif comChild.ttype == sqlparse.tokens.Token.Literal.String.Single:
                                self.values.append(comChild.value.replace("'", ''))
                    elif child.ttype == sqlparse.tokens.Token.Literal.Number.Integer:
                        self.values.append(child.value)

        # remove empty string from the list
        if '' in self.columnNames:
            self.columnNames.remove('')

        self.columnNames = [i for i in self.columnNames if i.upper() not in ['AND','OR','BETWEEN','IS','NULL', 'TO']]
        # print(self.columnNames)

    def replaceColumnNames(self):
        replaceList = []
        for column in self.columnNames:
            replaceList.append(self.fuzzyMatcher.cosineSimilarity(column))

        for i in replaceList:
            self.processedQuery = self.processedQuery.replace(list(i.keys())[0], list(i.values())[0])

        for word, initial in logicalReplacements.items():
            self.processedQuery = re.sub(r'\b' + word + r'\b', initial, self.processedQuery.upper())

    def replaceComparisonStrings(self):
        if '=' in self.processedQuery:
            sqlStatement = sqlparse.format(self.processedQuery,
                                           keyword_case='upper', comma_first=True)

            comparisonStrings = []
            for words in sqlStatement.split('= ')[1].split(' '):
                if not words.isdigit():
                    comparisonStrings.append(words)

            for words in comparisonStrings:
                self.processedQuery = self.processedQuery.replace(words, "'" + words + "'")

    def SQLFormatter(self):
        self.processedQuery = sqlparse.format(self.processedQuery, comma_first=True)

    def keywordFormatter(self):
        if ' COUNT ' in self.processedQuery:
            word = self.processedQuery.split(' COUNT ')[1].split(' ')[0]
            self.processedQuery = self.processedQuery.replace(word, "(" + word + ")")

        if ' = ' in self.processedQuery and ' to ' in self.processedQuery:
            self.processedQuery = self.processedQuery.replace('=', "BETWEEN").replace(' to ', ' AND ')


# a = SQLQueryParser()
# query = '<pad> SELECT COUNT DTs FROM table WHERE kW = 500kVA</s>'
# g = a.parseQuery(query)
