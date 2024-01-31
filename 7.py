import nltk

# Download the required NLTK data
nltk.download('C://Users//ramak//AppData//Roaming//nltk_data') 

# Define the text to be tagged
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform part-of-speech tagging on the tokens
tagged_tokens = nltk.pos_tag(tokens)

# Print the tagged tokens
print(tagged_tokens)
