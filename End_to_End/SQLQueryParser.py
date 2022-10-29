from utils import configs, logicalReplacements, getTheColumns
from FuzzyMatcher import FuzzyMatch
import sqlparse
import re
import itertools
import dummylog


class SQLQueryParser:

    def __init__(self):
        self.logger = dummylog.DummyLog()
        self.fuzzyMatcher = FuzzyMatch()
        self.columnsFromTables = getTheColumns()
        self.parsedTokens = None
        self.processedQuery = None
        self.columnNames = []
        self.values = []
        self.correctColumns = []

    def parseQuery(self, query):
        self.processedQuery = query
        self.logger.logger.info("NLP2SQL model output Query ==>" + self.processedQuery)
        self.rightAndLeftStrip()
        self.replaceComparisonStrings()
        self.logger.logger.info("Query replace Comparison Strings ==>" + self.processedQuery)
        self.findColumns()
        self.logger.logger.info("Columns found ==>" + str(self.columnNames))
        self.replaceColumnNames()
        self.logger.logger.info("Query replaced columns ==>" + self.processedQuery)
        self.replaceTableName()
        self.logger.logger.info("Query replaced table names ==>" + self.processedQuery)
        self.relationalDataBaseConnector()
        self.logger.logger.info("Query replaced with relational tables ==>" + self.processedQuery)
        self.keywordFormatter()
        self.logger.logger.info("Query keyword Formatter ==>" + self.processedQuery)
        self.SQLFormatter()
        self.logger.logger.info("Final Query ==>" + self.processedQuery)
        self.clearVariables()
        return self.processedQuery

    def rightAndLeftStrip(self):
        self.processedQuery = self.processedQuery.replace("<pad> ", '').replace("</s>", '')

    def replaceTableName(self):
        tableName = configs['TableName']
        self.processedQuery = self.processedQuery.replace("table", " " + tableName + " ")

    def findColumns(self):
        tokenizedQuery = sqlparse.parse(self.processedQuery)[0].tokens
        for parent in tokenizedQuery:
            if not parent.is_whitespace:  # excluding the white space tokens
                if not parent.is_group and parent.ttype == sqlparse.tokens.Name.Builtin:
                    self.columnNames.append(parent.value)
                if type(parent) == sqlparse.sql.Identifier and parent.is_group:
                    self.columnNames.append(parent.value)
                elif parent.is_group:
                    for child in parent.tokens:
                        if type(child) == sqlparse.sql.Identifier and child.is_group:
                            self.columnNames.append(child.value)
                        elif not child.value.startswith('WHERE') and child.is_keyword and \
                                child.value not in ['AND', 'OR', 'BETWEEN', 'IS', 'NULL', 'TO']:
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

        self.columnNames = [i for i in self.columnNames if
                            i.upper() not in ['AND', 'OR', 'BETWEEN', 'IS', 'NULL', 'TO']]
        # print(self.columnNames)

    def replaceColumnNames(self):
        replaceList = []
        # for column in self.columnNames:
        #     replaceList.append(self.fuzzyMatcher.cosineSimilarity(column))
        for column in self.columnNames:
            matchValue = self.fuzzyMatcher.fuzzywuzzy(column)
            if matchValue:
                replaceList.append(matchValue)
            else:
                self.correctColumns.append(column)

        print(replaceList)
        if replaceList:
            for i in replaceList:
                self.correctColumns.append(list(i.values())[0])
                self.processedQuery = self.processedQuery.replace(list(i.keys())[0], list(i.values())[0])

        for word, initial in logicalReplacements.items():
            self.processedQuery = re.sub(r'\b' + word + r'\b', initial, self.processedQuery)

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

        if ' MAX ' in self.processedQuery:
            word = self.processedQuery.split(' MAX ')[1].split(' ')[0]
            self.processedQuery = self.processedQuery.replace(word, "(" + word + ")")

        if ' MIN ' in self.processedQuery:
            word = self.processedQuery.split(' MIN ')[1].split(' ')[0]
            self.processedQuery = self.processedQuery.replace(word, "(" + word + ")")

        if ' = ' in self.processedQuery and ' to ' in self.processedQuery:
            self.processedQuery = self.processedQuery.replace('=', "BETWEEN").replace(' to ', ' AND ')

    def relationalDataBaseConnector(self):
        columnAndTableDict = self.findIfMultipleTablesInvolved()
        print(columnAndTableDict)
        if columnAndTableDict:
            for key, value in columnAndTableDict.items():
                self.processedQuery = self.processedQuery.replace(key,
                                                                  value + '.' + key)  # changing V_R to polls_events.V_R

            self.processedQuery = self.processedQuery.split('WHERE')[0] + " INNER JOIN polls_transformer ON " \
                                                                          "polls_events.mainId_id=polls_transformer" \
                                                                          ".Transformer_number WHERE " \
                                  + self.processedQuery.split('WHERE')[1]

    def findIfMultipleTablesInvolved(self):
        columnAndTableDict = {}
        for i in self.correctColumns:
            for key, value in self.columnsFromTables.items():
                if i in value:
                    columnAndTableDict[i] = key

        if len(set(columnAndTableDict.values())) > 1:
            return columnAndTableDict
        else:
            return False

    def clearVariables(self):
        self.parsedTokens = None
        self.columnNames = []
        self.values = []
        self.correctColumns = []

# a = SQLQueryParser()
# query = '<pad> SELECT COUNT DTs FROM table WHERE kW = 500kVA</s>'
# g = a.parseQuery(query)
