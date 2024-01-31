import nltk
from collections import defaultdict
import random

# Sample text for training
training_text = "The quick brown fox jumps over the lazy dog . " \
                "The dog barks loudly . " \
                "The cat sleeps peacefully ."

# Tokenize the training text
tokens = nltk.word_tokenize(training_text)

# Perform part-of-speech tagging on the training text
tagged_tokens = nltk.pos_tag(tokens)

# Create a frequency distribution of words and their corresponding tags
word_tag_freq = defaultdict(lambda: defaultdict(int))
for word, tag in tagged_tokens:
    word_tag_freq[word][tag] += 1

# Function to assign a POS tag to a word based on frequencies
def assign_pos_tag(word):
    if word in word_tag_freq:
        tag_freq = word_tag_freq[word]
        total_freq = sum(tag_freq.values())
        # Generate a random number between 0 and the total frequency
        rand_num = random.randint(1, total_freq)
        cumulative_freq = 0
        # Iterate over tag frequencies and choose the tag based on random number
        for tag, freq in tag_freq.items():
            cumulative_freq += freq
            if rand_num <= cumulative_freq:
                return tag
    # If word not found or unexpected, return default tag 'NN' (noun)
    return 'NN'

# Test the POS tagging algorithm on a sample sentence
test_sentence = "The quick brown fox jumps over the lazy dog ."
test_tokens = nltk.word_tokenize(test_sentence)
tagged_test_tokens = [(word, assign_pos_tag(word)) for word in test_tokens]
print("Tagged sentence:")
print(tagged_test_tokens)
