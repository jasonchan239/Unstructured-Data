from sentence_transformers import SentenceTransformer
from numpy import dot, sqrt
from numpy.linalg import norm
from math import sqrt
import json


def get_tweets():
    with open('tweets-utf-8.json', encoding = "utf8") as f:
        tweets = [json.loads(line)['text'] for line in f]
    return tweets

def sort_by_sim(query_embedding, document_embeddings, documents):
    similarList = []
    for i in range(len(documents)):
        denominator = sqrt(dot(query_embedding, query_embedding)) * sqrt(
            dot(document_embeddings[i], document_embeddings[i]))
        if denominator == 0:
            similarity = 0
        else:
            similarity = dot(
                query_embedding, document_embeddings[i]) / denominator
        similarList.append((similarity, documents[i]))

    return sorted(similarList, key = lambda list: list[0], reverse=True)

def glove_top25(query, documents):
    model = SentenceTransformer('sentence-transformers/average_word_embeddings_glove.840B.300d')
    return sort_by_sim(model.encode(query), model.encode(documents), documents)[:25]

def minilm_top25(query, documents):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return sort_by_sim(model.encode(query), model.encode(documents), documents)[:25]

## Test Code
tweets = get_tweets()

print("**************GLOVE*****************")
for p in glove_top25("I am looking for a job.", tweets): print(p)

print("**************MINILM*****************")
for p in minilm_top25("I am looking for a job.", tweets): print(p)
