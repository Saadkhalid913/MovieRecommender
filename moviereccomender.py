# -*- coding: utf-8 -*-
"""MovieReccomender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cYKrKMLTekxYTFj5fDhY6OERL7HBZQGC
"""

import tensorflow as tf
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("/content/mpst_full_data.csv").iloc[ :5000  , 1:4].values

# retrieval fuction 
def getMovieAtIndex(i):
  return data[i, [0]][0]

def getIndexOfMovie(title):
  return np.where(data[ : , [0]] == title)[0][0]

print(getIndexOfMovie("I Know What You Did Last Summer"))

# combining all important columns into a single vector 
def combine(arr):
  features = []
  for i in range(len(arr)):
    features.append(arr[i][0] + " " + arr[i][1] + " " + arr[i][2])
  return np.array(features) 

features = combine(data)

# tokenization 

cm = CountVectorizer()
tokens = cm.fit_transform(features)

cs = cosine_similarity(tokens)

title = input("Write the movie you want to find similar movies for ")
index = getIndexOfMovie(title)

Movie_Similarities = []
for i in range(len(cs)):
  Movie_Similarities.append((getMovieAtIndex(i), cs[index][i] * 100))
Movie_Similarities = sorted(Movie_Similarities, key=lambda x:x[1], reverse=True)

with open("rec.txt", "a") as f:
  for i in range(len(cs)):
    f.write(f"{Movie_Similarities[i][0]}: {Movie_Similarities[i][1]}%\n")