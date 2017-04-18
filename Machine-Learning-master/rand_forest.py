import pandas as pd
import numpy as np

train_data = pd.read_excel("training.xlsx")
train_data.head()
feature_cols = ['word_count', 'sentence_count', 'noun_count', 'adjective_count', 'verb_count', 'adverb_count', 'spell_error', 'read_ease', 'word_bag', 'word_4', 'word_6', 'non_caps']
X = train_data[feature_cols]
y = train_data.total_score

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1500, n_jobs=-1)
rf.fit(X, y)

test_data = pd.read_excel("testing.xlsx")
test_data.head()

feature_cols_test = ['word_count', 'sentence_count', 'noun_count', 'adjective_count', 'verb_count', 'adverb_count', 'spell_error', 'read_ease', 'word_bag', 'word_4', 'word_6', 'non_caps']
X_test = test_data[feature_cols_test]
prediction = rf.predict(X_test)

import openpyxl
wb = openpyxl.load_workbook('testing.xlsx')
ws = wb.get_sheet_by_name('testing_set')
for i in range(2, 591):
	score = round(prediction[i - 2])
	ws.cell(row = i, column = 6).value = round(score)
wb.save('testing.xlsx')