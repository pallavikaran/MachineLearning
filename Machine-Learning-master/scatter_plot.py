import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

data = pd.read_excel("training.xlsx")
data.head()
print data.shape

a1 = data.word_count
b1 = data.total_score
plt.subplot(3, 1, 1)
plt.scatter(b1, a1)
plt.title('Scatter Plot For Different Features')
plt.ylabel('Word Count')

a2 = data.sentence_count
b2 = data.total_score
plt.subplot(3, 1, 2)
plt.scatter(b2, a2)
plt.ylabel('Sentence Count')

a7 = data.spell_error
b7 = data.total_score
plt.subplot(3, 1, 3)
plt.scatter(b7, a7)
plt.ylabel('Spell Error Count')

plt.xlabel('Score')
plt.show()