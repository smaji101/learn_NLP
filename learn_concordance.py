
from nltk.book import *

text8.concordance("man")

print(text8.dispersion_plot(
     ["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"]
 ))

text2.dispersion_plot(["Allenham", "Whitwell", "Cleveland", "Combe"])