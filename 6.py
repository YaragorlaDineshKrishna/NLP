import random

# Sample text for training the bigram model
text = "I love natural language processing. It's fascinating."

# Tokenize the text into words
words = text.split()

# Function to generate a bigram model from the given text
def generate_bigram_model(text):
    words = text.split()
    bigrams = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in bigrams:
            bigrams[current_word].append(next_word)
        else:
            bigrams[current_word] = [next_word]
    return bigrams

# Generate bigram model from the sample text
bigram_model = generate_bigram_model(text)

# Function to generate text using the bigram model
def generate_text(bigram_model, starting_word, num_words=10):
    current_word = starting_word
    generated_text = [current_word]
    for _ in range(num_words):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(generated_text)

# Generate text using the bigram model
starting_word = random.choice(list(bigram_model.keys()))
generated_text = generate_text(bigram_model, starting_word, num_words=10)
print("Generated Text:", generated_text)
