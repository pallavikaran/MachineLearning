import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

train_data = pd.read_excel("training.xlsx")
train_data.head()

feature_cols = ['word_count', 'sentence_count', 'noun_count', 'adjective_count', 'verb_count', 'adverb_count', 'spell_error', 'read_ease', 'word_4', 'word_6']
X = train_data[feature_cols]
y = train_data.total_score

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X, y)

import re
import nltk
from nltk import word_tokenize, pos_tag

f = file('sample.txt', 'r')
essay = f.read()
essay = str(essay)
print essay
letters_only = re.sub("[^a-zA-Z]", " ", essay)
essay = letters_only.lower()

word_count = 0
word_count = essay.count(" ")
word_count = word_count + 1

sentence_count = 0
sentence_count = essay.count(".")

noun_count = 0
x = nltk.word_tokenize(essay)
y = nltk.pos_tag(x)
nouns = [word for word, pos in y if pos == 'NN']
noun_count = len(nouns)

adjectives = [word for word, pos in y if pos == 'JJ']
adjective_count = len(adjectives)

verbs = [word for word, pos in y if pos == 'VB']
verb_count = len(verbs)

adverbs = [word for word, pos in y if pos == 'RB']
adverb_count = len(adverbs)

import enchant
dictionary = enchant.Dict("en_US")
spell_error = 0
for word in essay.split():
	if dictionary.check(word) == 0:
		spell_error = spell_error + 1

import textstat
from textstat.textstat import textstat
read_ease = textstat.flesch_reading_ease(essay)

word_5 = 0
word_4 = 0
for word in essay.split():
	if len(word) >= 5:
		word_5 = word_5 + 1
	if len(word) <= 4:
		word_4 = word_4 + 1

prediction = lm.predict([word_count, sentence_count, noun_count, adjective_count, verb_count, adverb_count, spell_error, read_ease, word_4, word_5])

print "Computer assigned score : %d" % round(prediction)