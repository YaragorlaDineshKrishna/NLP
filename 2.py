class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, next_state):
        self.transitions[symbol] = next_state

class Automaton:
    def __init__(self):
        self.start_state = State("start")
        self.end_state = State("end")
        self.current_state = self.start_state
        self.start_state.add_transition('a', self.end_state)
        self.end_state.add_transition('b', self.end_state)

    def process_symbol(self, symbol):
        if symbol in self.current_state.transitions:
            self.current_state = self.current_state.transitions[symbol]
        else:
            self.reset()

    def reset(self):
        self.current_state = self.start_state

    def is_accepted(self):
        return self.current_state == self.end_state

def test_automaton():
    automaton = Automaton()
    test_strings = ['ab', 'aab', 'abb', 'ba', 'b']
    for test_string in test_strings:
        for symbol in test_string:
            automaton.process_symbol(symbol)
        if automaton.is_accepted():
            print(f"'{test_string}' is accepted")
        else:
            print(f"'{test_string}' is not accepted")
        automaton.reset()

test_automaton()
