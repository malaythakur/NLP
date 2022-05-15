# -*- coding: utf-8 -*-
"""
Malay Thakur

AIM : lemmatization

"""
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

para = """
The Python programing language provides a wide range of tools and libraries for attacking specific NLP tasks.
Many of these are found in the Natural Language Toolkit, or NLTK, an open source collection of libraries, programs,
and education resources for building NLP programs.
The NLTK includes libraries for many of the NLP tasks listed above, plus libraries for subtasks, such as sentence
parsing, word segmentation, stemming and lemmatization (methods of trimming words down to their roots), and 
tokenization (for breaking phrases, sentences, paragraphs and passages into tokens that help the computer 
better understand the text). It also includes libraries for implementing capabilities such as semantic reasoning,
the ability to reach logical conclusions based on facts extracted from text.
"""

sentences = nltk.sent_tokenize(para)

lemmatizer = WordNetLemmatizer() #here lemmatize is an object of class WorldNetLemmatizer()

#lemmatize
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
    
    
