from graphviz import Digraph

visited = set()

def draw_nfa(nfa):
    global visited
    visited = set()

    dot = Digraph()
    dot.attr(rankdir='LR')

    traverse(nfa.start, dot)

    dot.attr('node', shape='doublecircle')
    dot.node(nfa.accept.name)

    dot.render('nfa_output', format='png', view=True)

def traverse(state, dot):
    if state.name in visited:
        return

    visited.add(state.name)

    dot.node(state.name)

    for symbol, states in state.transitions.items():
        for next_state in states:
            dot.edge(state.name, next_state.name, label=symbol)
            traverse(next_state, dot)

    for next_state in state.epsilon:
        dot.edge(state.name, next_state.name, label='ε')
        traverse(next_state, dot)