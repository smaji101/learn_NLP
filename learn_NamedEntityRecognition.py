# With named entity recognition, we can find the named entities in  texts and
# also determine what kind of named entity they are.

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

lotr_quote = "It's a dangerous business, Frodo, going out your door."

words_in_lotr_quote = word_tokenize(lotr_quote)
print (words_in_lotr_quote)

lotr_pos_tags = pos_tag(words_in_lotr_quote)
print(lotr_pos_tags)

tree = ne_chunk(lotr_pos_tags)
print(tree)