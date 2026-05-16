from nfa import State, NFA

def symbol_nfa(symbol):
    start = State()
    accept = State()

    start.transitions[symbol] = [accept]

    return NFA(start, accept)

def concat_nfa(nfa1, nfa2):
    nfa1.accept.epsilon.append(nfa2.start)
    return NFA(nfa1.start, nfa2.accept)

def kleene_star(nfa):
    start = State()
    accept = State()

    start.epsilon.append(nfa.start)
    start.epsilon.append(accept)

    nfa.accept.epsilon.append(nfa.start)
    nfa.accept.epsilon.append(accept)

    return NFA(start, accept)

def regex_to_nfa(regex):
    stack = []

    i = 0

    while i < len(regex):
        char = regex[i]

        if char.isalpha():

            nfa = symbol_nfa(char)

            if i + 1 < len(regex) and regex[i + 1] == '*':
                nfa = kleene_star(nfa)
                i += 1

            if stack:
                prev = stack.pop()
                nfa = concat_nfa(prev, nfa)

            stack.append(nfa)

        i += 1

    return stack.pop()