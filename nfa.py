state_counter = 0

class State:
    def __init__(self):
        global state_counter

        self.name = f"q{state_counter}"
        state_counter += 1

        self.transitions = {}
        self.epsilon = []

class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept