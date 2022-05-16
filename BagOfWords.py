# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:23:10 2022

@author: Malay Thakur
"""

import nltk

para = """
Everything we express (either verbally or in written) carries huge amounts of information.
The topic we choose, our tone, our selection of words, everything adds some type of information
that can be interpreted and value extracted from it. In theory, we can understand and even predict
human behaviour using that information.
But there is a problem: one person may generate hundreds or thousands of words in a declaration,
each sentence with its corresponding complexity. If you want to scale and analyze several hundreds,
thousands or millions of people or declarations in a given geography, then the situation is
unmanageable.
Data generated from conversations, declarations or even tweets are examples of unstructured data.
Unstructured data doesn’t fit neatly into the traditional row and column structure of relational
databases, and represent the vast majority of data available in the actual world. It is messy
and hard to manipulate. Nevertheless, thanks to the advances in disciplines like machine learning 
a big revolution is going on regarding this topic. Nowadays it is no longer about trying to 
interpret a text or speech based on its keywords (the old fashioned mechanical way), but about 
understanding the meaning behind those words (the cognitive way). This way it is possible to 
detect figures of speech like irony, or even perform sentiment analysis.
Natural Language Processing or NLP is a field of Artificial Intelligence that gives the machines 
the ability to read, understand and derive meaning from human languages.
It is a discipline that focuses on the interaction between data science and human language,
and is scaling to lots of industries. Today NLP is booming thanks to the huge improvements in the
access to data and the increase in computational power, which are allowing practitioners to 
achieve meaningful results in areas like healthcare, media, finance and human resources, 
among others.
"""

#cleaning the texts
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet = WordNetLemmatizer()

sentences = nltk.sent_tokenize(para)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-z]' , ' ', sentences[i]) 
    review = review.lower() 
    review = review.split() 
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))] 
    review = ' '.join(review)
    corpus.append(review)
    

from sklearn.feature_extraction.text import CountVectorizer #importing 
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()

"""
for i in range(len(sentences)):
    review = re.sub('[^a-zA-z]' , ' ' , sentences[i])  #removes , . ? ! spaces , replacing every character other than comma , fullstop other than letters a-z to A-Z
    review = review.lower() #returns lowerstring
    review = review.split() #list of words
    review = [ps.stem(word) for each word in review if not word in set(stopwords.words('english'))] #list compreshension #stopwords - igonore words like -> the, i,so,
    review = ' '.join(review)
    corpus.append(review)
    

"""
