import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

test_data = pd.read_excel("training.xlsx")
test_data.head()
print test_data.shape

feature_cols = ['word_count', 'sentence_count', 'noun_count', 'adjective_count', 'verb_count', 'adverb_count', 'spell_error', 'read_ease', 'word_bag']
X = test_data[feature_cols]
y = test_data.total_score

clf = svm.SVC()
clf.fit(X,y)

test_data = pd.read_excel("testing.xlsx")
test_data.head()
print test_data.shape

feature_cols_test = ['word_count', 'sentence_count', 'noun_count', 'adjective_count', 'verb_count', 'adverb_count', 'spell_error', 'read_ease', 'word_bag']
X_test = test_data[feature_cols_test]
prediction = clf.predict(X_test)

import openpyxl
wb = openpyxl.load_workbook('testing.xlsx')
ws = wb.get_sheet_by_name('testing_set')
for i in range(2, 591):
	score = round(prediction[i - 2])
	ws.cell(row = i, column = 6).value = round(score)
wb.save('testing.xlsx')