import pandas as pd


class QuestionParser:

    def __init__(self):
        self.processedQuestion = None
        self.alternateNamesJson = {}
        self.csvPath = r'dependency_files/column_descriptions.csv'
        self.getColumnNames()

    def checkAlternateNames(self, question):
        question = question.lower()
        self.processedQuestion = question.lower()

        replaceNames = {}
        for key, value in self.alternateNamesJson.items():
            if key in question:
                replaceNames.update({key: value})
                question = question.replace(key, '')

        for key, value in replaceNames.items():
            self.processedQuestion = self.processedQuestion.replace(key, value)

        return self.processedQuestion

    def getColumnNames(self):
        dataframe = pd.read_csv(self.csvPath).fillna('')

        for index, row in dataframe.iterrows():
            if not row['names'] == '':
                names = [i.lstrip().rstrip().replace('-', ' ').lower() for i in row['names'].split(',')]
                for name in names:
                    self.alternateNamesJson.update({name: row['column']})

        self.alternateNamesJson = dict(sorted(self.alternateNamesJson.items(), reverse=True, key=lambda x: len(x[0])))


# q = QuestionParser()
# print(q.checkAlternateNames('count timestamp with manufacture name with KEL'))