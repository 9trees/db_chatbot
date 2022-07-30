from utils import configs
import sqlparse

class SQLQueryParser:

    def __init__(self):
        self.parsedTokens = None
        self.processedQuery = None
        self.resultColumns = None
        self.resultClause = None
        self.conditionalColumns = None
        self.conditionalClause = None

    def parseQuery(self, query):
        self.processedQuery = query
        self.rightAndLeftStrip()
        self.replaceTableName()
        self.findResultColumn()
        self.parsedTokens = sqlparse.parse(self.processedQuery)[0].tokens
        pass

    def rightAndLeftStrip(self):
        self.processedQuery = self.processedQuery.replace("<pad> ", '').replace("</s>", '')

    def replaceTableName(self):
        tableName = configs['TableName']
        self.processedQuery = self.processedQuery.replace(" table ", " " + tableName + " ")

    def findResultColumn(self):
       findGroups =  [i for i in self.parsedTokens if i.is_group]


    def findConditionalColumns(self):
        regex = re.compile('|'.join(re.escape(x) for x in self.conditionalClauseList))
        SQLResultClause = re.findall(regex, self.processedQuery)[0]
        columns = self.processedQuery.split('WHERE ')[-1].split('FROM')[0].split(SQLResultClause)[-1].split(',')
        self.resultColumns = [i.lstrip().rstrip() for i in columns]


a = "<pad> SELECT COUNT DT FROM table WHERE Manufacturer = Siemens</s>"

d = SQLQueryParser()
d.parseQuery(a)