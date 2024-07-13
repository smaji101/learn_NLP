from nltk import FreqDist
from nltk.book import *
from nltk.corpus import stopwords

frequency_distribution = FreqDist(text8)
print(frequency_distribution)
frequency_distribution.most_common(20)

stop_words = set(stopwords.words("english"))
meaningful_words = [
    word for word in text8 if word.casefold() not in stop_words
]

frequency_distribution = FreqDist(meaningful_words)
frequency_distribution.plot(20, cumulative=True)