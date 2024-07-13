from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
worf_quote = "Sir, I protest. I am not a merry man!"

#tokenize worf_quote by word and store the resulting list in words_in_quote
words_in_quote = word_tokenize(worf_quote)
print(words_in_quote)

#creat a set of stop words in "english"
stop_words = set(stopwords.words("english"))

#create an empty list to hold
filtered_list = []

#iterate over words_in_quote, ignore whether the letters in word were uppercase or lowercase and filter
for word in words_in_quote:
    if word.casefold() not in stop_words:
       filtered_list.append(word)

print(filtered_list)