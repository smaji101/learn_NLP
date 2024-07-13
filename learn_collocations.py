from nltk import FreqDist
from nltk.book import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

text8.collocations()

lemmatized_words = [lemmatizer.lemmatize(word) for word in text8]
new_text = Text(lemmatized_words)

new_text.collocations()