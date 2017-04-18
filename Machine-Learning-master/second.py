# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 19:53:11 2015

@author: ANISH
"""
from __future__ import division
#from nltk.corpus import stopwords 
from textstat.textstat import textstat
"""from openpyxl import load_workbook
ws=load_workbook("MyTester.xlsx")
print(ws.get_sheet_names())"""
#import enchant
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn
#df = pd.read_excel("training_set_rel3 (1).xls")
df = pd.read_excel("MyTester.xlsx")
df.head()
c=0
c1=0
d=0
e=0
w=0
#prints the whole Excel file's data
#print(df)

me=[]
wo=0
fr=0
#word count
print("word count is")
for index in range(len(df)):
     c=0
     c1=0
     s=0
     p=df.essay[index]
     for i in range(len(p)):
         if p[i]==" ":
           c=c+1
         if p[i]==".":
           s=s+1
     print(c+1)
     wo=c+1
     fr=pow(wo,0.25)
     print("fourth root of number of words in the essay")
     print(fr)
     print(s)
     print("Number of words divided by Number of sentences")
     print((wo)/s)
     print("")
     df["Words"] = c
     df.head()
     me.append(c)
   

#sentence count
f=[]
print("sentence count is")
for index in range(len(df)):
    c=0
    d=0
    p=df.essay[index]
    for i in range(len(p)):
         c=c+1
         if p[i]==".":
           d=d+1
    print(d)
    f.append(d)
    print(c)
    print("number of characters by number of sentences")
    print(c/d)
    print("")
    df["sentences"] = d
    df.head()
    me.append(d)

    
"""#number of words greater than 6
print("number of words greater than 6 in the essay's")
for index in range(len(df)):
    e=0
    r=df.essay[index]
    for word in r.split():
        if len(word)>=6:
            e=e+1
    print(e)"""
    
#number of words greater than 6 divided by the number of word tokens
print("number of words greater than 6 in the essay divided by the number of words")
for index in range(len(df)):
    t=0
    e=0
    r=df.essay[index]
    for word in r.split():
        t=t+1
        if len(word)>=6:
            e=e+1
    print(t)
    print(e)    
    print(t/e)
    print("")
    
    
#number of words less than 4 divided by the number of word tokens
print("number of words less than 4 in the essay divided by the number of words")
for index in range(len(df)):
    t1=0
    q=0
    r=df.essay[index]
    for word in r.split():
        t1=t1+1
        if len(word)<=4:
            q=q+1
    print(t1)
    print(q)    
    print(t1/q)
    print("")       
"""   
#number of words less than 4
print("number of words less than 4 in the essay's")
for index in range(len(df)):
    w=0
    r=df.essay[index]
    for word in r.split():
        if len(word)<=4:
            w=w+1
    print(w)"""

#finding the Lemma's for each word in each essay

"""syn = wn.synsets('cookbook')[0]
lemmas = syn.lemmas()
print(len(lemmas))
print(lemmas[0].name)
print(lemmas[1].name)"""
"""for word in r.split():
    syn = wn.synsets(word)
    lemmas = syn.lemmas()"""
#number of words   
"""p=df.essay[2]
for i in range(len(p)):
   if p[i]==" ":
       c=c+1
print(c+1)
"""
#lemma continue
from sets import Set
for index in range(len(df)):
    t2=0
    r=df.essay[index]    
    count_lemma_set_for_essay=[] 
    for words in r.split():
         t2=t2+1
         lemma_set=Set() 
         for word in words: 
             for synset in wn.synsets(word): 
                for lemma in synset.lemmas(): 
                     lemma_set.add(lemma) 
    #print(lemma_set)
    print(t2)
    print(len(lemma_set))
    print("Number of Lemmas divided by Number of word tokens")
    print(len(lemma_set)/t2)
    print("")
    count_lemma_set_for_essay.append(len(lemma_set))     
    #print(len(count_lemma_set_for_essay))
    
#useless
# Print the information
"""for synset in wn.synsets:
        print "-" * 10
        print "Name:", synset.name
        print "Lexical Type:", synset.lexname
        print "Lemmas:", synset.lemma_names
        print "Definition:", synset.definition
        for example in synset.examples:
            print "Example:", example"""
            
z=[]
po=0            
#Number of Non-initial Capital character words divided by number of sentences           
for index in range(len(df)):
    t=0
    l=0
    r=df.essay[index]
    for word in r.split():
        l=l+1
        y=word[0]
        if y.isupper():
            t=t+1
    print(t)
    print(l)
    po=l-t
    print("Number of Non-initial Capital character words")
    print(po)
    z.append(po)
    print("")
ncs=[]
print("Number of Non-initial Capital character words divided by number of sentences")
for index in range(len(df)):
    ncs.append(z[index]/f[index])
print("This is it")
print(ncs)
print("s")
print(f)
print("ncw")
print(z)
p1=0
nouns=0
downcased=0
"""print("Trying grammer for a text")
for index in range(len(df)):
     p=df.essay[index]
     p1=nltk.word_tokenize(p)
     p2=nltk.pos_tag(p1)
     #print(" ")
     #try:
     for word,pos in p2:
             #word = word.strip()
             #pos=pos.strip()
             if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
                 nouns = word
                 downcased = [x.lower() for x in nouns]
     #except ValueError:
             #print('Ignoring: malformed line: "{}"'.format(word))
             #print('Ignoring: malformed line: "{}"'.format(pos))
     print(downcased)"""

#print("Number of spelling mistakes in each essay")
"""g=enchant.Dict("en_US")
for index in range(len(df)):
    g1=0
    r=df.essay[index]
    for word in r.split():
        if g.check(word)== 1:
            g1=g1+1
    print(g1)
    print("")"""
    
#all={1: 'CC', 2: 'CD', 3: 'DT', 4: 'EX', 5: 'FW', 6: 'IN', 7: 'JJ', 8: 'JJR', 9: 'JJS', 10: 'LS', 11: 'MD', 12: 'NN', 13: 'NNS', 14: 'NNP', 15: 'NNPS', 16: 'PDT', 17: 'POS', 18: 'PRP', 19: 'PRP$', 20: 'RB', 21: 'RBR', 22: 'RBS', 23: 'RP', 24: 'SYM', 25: 'TO', 26: 'UH', 27: 'VB', 28: 'VBD', 29: 'VBG', 30: 'VBN', 31: 'VBP', 32: 'VBZ', 33: 'WDT', 34: 'WP', 35: 'WP$', 36: 'WRB', 'NN': 12, 'FW': 5, 'PRP': 18, 'RB': 20, 'NNS': 13, 'NNP': 14, 'PRP$': 19, 'WRB': 36, 'CC': 1, 'PDT': 16, 'VBN': 30, 'WP$': 35, 'JJS': 9, 'JJR': 8, 'SYM': 24, 'VBP': 31, 'WDT': 33, 'JJ': 7, 'VBG': 29, 'WP': 34, 'VBZ': 32, 'DT': 3, 'POS': 17, 'TO': 25, 'LS': 10, 'VB': 27, 'RBS': 22, 'RBR': 21, 'EX': 4, 'IN': 6, 'RP': 23, 'CD': 2, 'VBD': 28, 'MD': 11, 'NNPS': 15, 'UH': 26,  '.':37 , 37:'.' , ':':38, 38:':','-NONE-':39,39:'-NONE-' , ',':40, 40:','}
#ui=[]
print("grammer for the essay's")
for index in range(len(df)):
     p=df.essay[index]
     p1=nltk.word_tokenize(p.lower())
     p2=nltk.pos_tag(p1)
     counts=Counter(tag for p1,tag in p2)
     print(counts)
     total = sum(counts.values())
     print(dict((word, float(count)/total) for word,count in counts.items()))
     print("")
print("readability/complexity")     
for index in range(len(df)):
    r=df.essay[index]
    print(textstat.syllable_count(r))    
    print(textstat.readability_consensus(r))
    print("")
    #print(textstat.flesch_reading_ease(r))
    #print(textstat.flesch_kincaid_grade(r))
    
    
"""for index in range(len(df)):
    r=df.essay[index]     
    for words in r.split():
        words1 = [w1 for w1 in words if not w1 in stopwords.words("english")]
        print(words1)"""
        
#Example
print("normalizing values")
ranger = interp1d([1,512],[1,10])
print(ranger(256))

print("Bag of Words for the first two essay's for 50 features")
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 50)
r=df.essay[0]
r1=df.essay[1]
asp = []
asp.append(r)
asp.append(r1)
train_data_features = vectorizer.fit_transform(asp)
train_data_features = train_data_features.toarray()
print train_data_features.shape
vocab=0
vocab = vectorizer.get_feature_names()                           
print vocab
