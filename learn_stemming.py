from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#create a stemmer
stemmer = PorterStemmer()

#create a string to stem
string_for_stemming = ("The crew of the USS Discovery discovered many discoveries. "
                       "Discovering is what explorers do")

#separate all the words
words = word_tokenize(string_for_stemming)

#tokenizedlist of words
print(words)

stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)