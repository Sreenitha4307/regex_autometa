# NFA Diagram Visualization

This document describes the NFA (Non-deterministic Finite Automaton) structure shown in the diagram.

## States and Transitions

The NFA contains multiple state layers with epsilon (ε) transitions and character transitions:

### Layer 1 (q2)
- Start state: q2
- Epsilon transition to q0
- Epsilon transition to q3

### Layer 2 (q0, q1, q3)
- q0: Accepts 'a', transitions to q1
- q1: Character transition, epsilon to q3
- q3: Epsilon transition to q5 and q4

### Layer 3 (q4, q5, q7)
- q4: Accepts 'b', transitions to q5
- q5: Epsilon transition to q7
- q7: Epsilon transition to q10

### Layer 4 (q8, q10, q11)
- q8: Accepts 'c', transitions to q9
- q10: Epsilon transition to q8 and q11
- q9: Epsilon transition to q11
- q11: Final accept state

## Pattern Description

This NFA appears to represent a regex pattern matching strings with:
- 'a' followed by any number of 'b's, followed by 'c'
- Pattern: `ab*c`

## Usage

The generated NFA can be used with the `match_string()` function from `dfa.py` to test if input strings match the pattern.

Example test cases:
- "ac" → Accepted
- "abc" → Accepted
- "abbc" → Accepted
- "abbbc" → Accepted
