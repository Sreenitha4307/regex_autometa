def match_string(nfa, string):
    current_states = epsilon_closure([nfa.start])

    for char in string:
        next_states = []

        for state in current_states:
            if char in state.transitions:
                next_states.extend(state.transitions[char])

        current_states = epsilon_closure(next_states)

    return nfa.accept in current_states

def epsilon_closure(states):
    stack = states[:]
    closure = set(states)

    while stack:
        state = stack.pop()

        for next_state in state.epsilon:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return list(closure)