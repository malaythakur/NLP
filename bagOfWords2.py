# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:09:39 2022

@author: Malay Thakur
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:23:10 2022

@author: Malay Thakur
"""

import nltk

para = """
I am Malay Thakur.
I am learning Natural language processing (NLP).
It is fun and worth learning NLP.
I want to make my carrer in AI and ML and NLP.
AI and ML is my field of interest.
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


Notes:
    see the difference between (ln 40)
    ps.stem(word) and wordnet.Lemmatize(word) -> wordnet.Lemmatize gives more meaninigfull words in
    comparision to stemming.
    
for i in range(len(sentences)):
    review = re.sub('[^a-zA-z]' , ' ' , sentences[i])  #removes , . ? ! spaces , replacing every character other than comma , fullstop other than letters a-z to A-Z
    review = review.lower() #returns lowerstring
    review = review.split() #list of words
    review = [ps.stem(word) for each word in review if not word in set(stopwords.words('english'))] #list compreshension #stopwords - igonore words like -> the, i,so,
    review = ' '.join(review)
    corpus.append(review)
    

"""
