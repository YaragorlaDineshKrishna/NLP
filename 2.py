class StateMachine:
    def _init_(self):
        self.current_state = 'q0'  # Initial state

    def process_input(self, input_str):
        for char in input_str:
            if self.current_state == 'q0':
                if char == 'a':
                    self.current_state = 'q1'
                else:
                    self.current_state = 'q0'
            elif self.current_state == 'q1':
                if char == 'b':
                    self.current_state = 'q2'
                elif char == 'a':
                    self.current_state = 'q1'
                else:
                    self.current_state = 'q0'
            elif self.current_state == 'q2':
                # Accepting state, no transitions allowed
                return True

        # Check if the final state is 'q2'
        return self.current_state == 'q2'


def main():
    # Example usage
    automaton = StateMachine()

    # Strings to test
    test_strings = ['aab', 'abc', 'abab', 'aaaab', 'ab']

    for test_str in test_strings:
        result = automaton.process_input(test_str)
        if result:
            print(f"Accepted: '{test_str}'")
        else:
            print(f"Rejected: '{test_str}'")


if _name_ == "_main_":
    main()
