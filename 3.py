import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


sentence = "The quick brown foxes are jumping over the lazy dogs"


tokens = word_tokenize(sentence)


pos_tags = nltk.pos_tag(tokens)


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(word) for word in tokens]
lemmatized_words = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in pos_tags]

print("Original Sentence:", sentence)
print("\nStemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)
