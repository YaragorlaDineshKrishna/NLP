class FSM:
    def __init__(self):
        self.current_state = 'start'

    def transition(self, input_symbol):
        transitions = {
            'start': {'consonant': 'plural', 'vowel': 'plural_y'},
            'plural': {'y': 'ies', 'default': 's'},
            'plural_y': {'default': 's'}
        }

        if input_symbol in transitions[self.current_state]:
            self.current_state = transitions[self.current_state][input_symbol]
        else:
            self.current_state = transitions[self.current_state]['default']

    def pluralize(self, noun):
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        if noun[-1] in vowels:
            self.transition('vowel')
        else:
            self.transition('consonant')

        if noun[-1] == 'y':
            noun = noun[:-1]  # Remove the 'y' from the noun if present
        return noun + self.current_state


def test_pluralizer():
    pluralizer = FSM()
    nouns = ['cat', 'dog', 'fox', 'city', 'baby', 'boy']
    for noun in nouns:
        print(f"Singular: {noun}, Plural: {pluralizer.pluralize(noun)}")


test_pluralizer()
