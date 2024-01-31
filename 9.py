import re

rules = [
    (r'\b(?:is|are|am)\b', 'VERB'),  
    (r'\b(?:\w+ed)\b', 'VERB'), 
    (r'\b(?:\w+ing)\b', 'VERB'),     
    (r'\b(?:\w+ly)\b', 'ADV'),      
    (r'\b(?:\w+est)\b', 'ADJ'),      
    (r'\b(?:\w+er)\b', 'ADJ'),       
    (r'\b(?:\w+\'s)\b', 'NOUN'),     
    (r'\b(?:\d+\.\d+|\d+)\b', 'NUM'),
    (r'\b(?:a|an|the)\b', 'DET'),   
    (r'\b(?:\w+s)\b', 'NOUN'),      
    (r'\b(?:\w+)\b', 'NOUN'),        
]

def pos_tag(sentence):
    tagged_sentence = []
    for word in sentence.split():
      
        for pattern, tag in rules:
            if re.match(pattern, word):
                tagged_sentence.append((word, tag))
                break
        else:
           
            tagged_sentence.append((word, 'NOUN'))
    return tagged_sentence

sentence = "He is running quickly."
tagged_sentence = pos_tag(sentence)
print("Tagged sentence:")
print(tagged_sentence)
