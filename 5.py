import nltk
from nltk.stem import PorterStemmer

porter_stemmer = PorterStemmer()

words = ["running", "easily", "consolingly", "happily", "cats", "dogs", "programming", "jumps"]

for word in words:
    stemmed_word = porter_stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")
