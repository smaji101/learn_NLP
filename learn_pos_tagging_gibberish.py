from nltk.tokenize import word_tokenize
from nltk import pos_tag

#gibberish text to tag
quote = "this that undispriz'd count and lose bourn no take and, by a bare bodk"

#tokenize
words_in_sagan_quote = word_tokenize(quote)
print(words_in_sagan_quote)

#parts of speech tagging
pos_tag_list=pos_tag(words_in_sagan_quote)
print(pos_tag_list)