from nltk.tokenize import word_tokenize
from nltk import pos_tag

#text to tag
quote = "Over the past few years, I’ve moved away from following primarily recipe blogs to spending my time enjoying other types of lifestyle blogs, and it has been awesome."

#tokenize
words_in_sagan_quote = word_tokenize(quote)
print(words_in_sagan_quote)

#parts of speech tagging
pos_tag_list=pos_tag(words_in_sagan_quote)
print(pos_tag_list)