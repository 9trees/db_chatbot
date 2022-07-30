import re
import glob
from ftfy import fix_text
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from collections import Counter

from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("glove.6B.50d.txt")

import string

import nltk
from nltk.corpus import stopwords

abbreviation = set(
    ['e.g', '6', 'inc.', 'inc', '4', 'u.s', 'jr', '3', 'u.s.a', 'ph', 'sr', 'i.e', '8', '7', '2', '1', '9', 'b.a',
     'etc.)', 'b.s', 'ph.d', 'etc', 'B.S', '5', '(e.g', '(i.e'])

bullet_set = set(['*', '-', '\u2022', '\u2023', '\u25e6', '\u2043', '\u204c', '\u204d', '\u2219'])

stopWords = stopwords.words('english')

punctuation_set = set(string.punctuation)
stopChar = set(list(bullet_set) + list(punctuation_set))
stopCharStr = "".join(stopChar)

translator = str.maketrans(stopCharStr, ' ' * len(stopCharStr))

adverse_media_vocab = ['DT_ID',
                       'AREA',
                       'ALERT',
                       'RATED_CAPACITY',
                       'TIME_STAMP',
                       'LOAD_DATA',
                       'ALERT_STATUS',
                       'ENERGY',
                       'MAKE',
                       'MANUFACTURE_YEAR']

adverse_media_vocab = [i.replace('_', ' ').lower() for i in adverse_media_vocab]

adverse_media_mtx = np.zeros((len(adverse_media_vocab), 50))
for i, vv in enumerate(adverse_media_vocab):
    adverse_media_mtx[i] = np.mean([model[v] for v in vv.split() if (v in model)], axis=0)


def clean_text_tokenizer(text):
    text = fix_text(text)
    text = text.encode("ascii", errors="ignore").decode()
    text = text.lower()
    text = "".join([i if ord(i) < 128 else ' ' for i in text])
    text = text.translate(translator)
    text = re.sub(" +", " ", text).strip()
    return [tok for tok in text.split() if (tok not in stopWords and tok in model)]


tokens = list()
for text in ['Years manufactured DT']:
    tokens += clean_text_tokenizer(text)
token_count_dict = dict(Counter(tokens))
unique_tokens = list(token_count_dict)

unique_tokens_mtx = np.array([model[t] for t in unique_tokens])

scores = cosine_similarity(unique_tokens_mtx, adverse_media_mtx)

s_l = list()
w_l = list()
similarityScore = {}
for token, idx, ss in zip(unique_tokens, scores.argmax(axis=1), scores.max(axis=1)):
    if (ss >= 0.7):
        print(
            f"Token: {token} --> Count: {token_count_dict[token]} --> Similar: {adverse_media_vocab[idx]} --> Score: {round(ss * 100, 2)}")
        s_l.append(ss)
        w_l.append(token_count_dict[token])
        similarityScore.update({token: adverse_media_vocab[idx]})

final_score = round(np.average(s_l, weights=w_l) * 100, 2)
