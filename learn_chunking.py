from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser

lotr_quote = "It's a dangerous business, Frodo, going out your door."

words_in_lotr_quote = word_tokenize(lotr_quote)
print (words_in_lotr_quote)

lotr_pos_tags = pos_tag(words_in_lotr_quote)
print(lotr_pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammar)
print(chunk_parser)

tree = chunk_parser.parse(lotr_pos_tags)
print(tree)

text8.concordance("man")