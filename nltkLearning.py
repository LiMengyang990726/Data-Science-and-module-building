import os
import pandas as pd
import numpy as np
import time

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns

import nltk
from nltk.text import Text
import csv
nltk.download()

# ==============================================================================
#
# For glassdoor job descriptions
#
# ==============================================================================

params = {'figure.figsize': (18,12),
            'axes.titlesize': 20}
plt.rcParams.update(params)

jobs_df = pd.read_csv('./Glassdoor_Jobs_Data.csv', encoding = "ISO-8859-1")
jobs_df.head()
job_dscrpt = jobs_df["Job Description"]
job_dscrpt.shape

# filter NULL
job_dscrpt_fileter = job_dscrpt.dropna()
job_dscrpt_fileter.shape
job_dscrpt_fileter.reset_index()

# filter those only have white space
job_dscrpt_fileter_Series = pd.Series(job_dscrpt_fileter)
for i, v in job_dscrpt_fileter_Series.items():
    temp = v.strip()
    if not temp:
        job_dscrpt_fileter_Series.drop(i,inplace = True) # This will drop 221 empty lines
job_dscrpt_fileter_Series.reset_index()

# filter the text and left only with the meaningful English word
tokens = []
stopwords = nltk.corpus.stopwords.words('english')
for i, v in job_dscrpt_fileter_Series.items():# have checked v is in the data type of string
    token = nltk.word_tokenize(v)
    for x in token:
        if x not in stopwords and x.isalpha():
            tags = nltk.pos_tag(token)
            adj_tags = [t for t in tags if t[1] == "ADJ"]
            tokens.append(adj_tags)


# filter according to part-of-speech and left only the ADJ and NOUN

# find the most frequent used word
fdist = nltk.FreqDist(tokens)
fdist.plot(50, cumulative=True,title="50 most commonly used words")

# ==============================================================================
#
# For learning purpose
#
# ==============================================================================
alice = Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))

# Get to know about the data
len(alice) # give number of tokens
len(set(alice)) # give number of unique tokens
alice.count('Alice') # count number of occurence of a certain word
alice.concordance('Alice') # shows where the word appears in the Text

# Visualizing
alice.dispersion_plot(["Alice", "Rabbit", "Hatter", "Queen"]) # gives a graph of the occurence of the list of word in parallel
fdist = nltk.FreqDist(alice) # plot the frequency distribution graph
