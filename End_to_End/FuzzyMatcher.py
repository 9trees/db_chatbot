import re
from ftfy import fix_text
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from gensim.models import KeyedVectors
import string
from nltk.corpus import stopwords
from utils import bullet_set, sqlColumns


class FuzzyMatch:

    def __init__(self):
        self.model = KeyedVectors.load_word2vec_format("glove.6B.50d.txt")
        self.stopWords = stopwords.words('english')
        punctuation_set = set(string.punctuation)
        stopChar = set(list(bullet_set) + list(punctuation_set))
        stopCharStr = "".join(stopChar)
        self.translator = str.maketrans(stopCharStr, ' ' * len(stopCharStr))
        self.sqlColumnsProcessed = [i.replace('_', ' ').lower() for i in sqlColumns]
        self.sqlColumnsMatrix = np.zeros((len(self.sqlColumnsProcessed), 50))
        for i, vv in enumerate(self.sqlColumnsProcessed):
            self.sqlColumnsMatrix[i] = np.mean([self.model[v] for v in vv.split() if (v in self.model)], axis=0)

    def runSQLQueryCorrector(self, query):

        pass

    def cosineSimilarity(self, inputText):
        tokens = list()
        for text in [inputText]:
            tokens += self.clean_text_tokenizer(text)

        token_count_dict = dict(Counter(tokens))
        unique_tokens = list(token_count_dict)
        unique_tokens_mtx = np.array([self.model[t] for t in unique_tokens])

        scores = cosine_similarity(unique_tokens_mtx, self.sqlColumnsMatrix)

        similarityScore = {}
        for token, idx, ss in zip(unique_tokens, scores.argmax(axis=1), scores.max(axis=1)):
            if ss >= 0.7:
                similarityScore.update({token: self.sqlColumnsProcessed[idx]})

        return similarityScore

    def clean_text_tokenizer(self, text):
        text = fix_text(text)
        text = text.encode("ascii", errors="ignore").decode()
        text = text.lower()
        text = "".join([i if ord(i) < 128 else ' ' for i in text])
        text = text.translate(self.translator)
        text = re.sub(" +", " ", text).strip()
        return [tok for tok in text.split() if (tok not in self.stopWords and tok in self.model)]
