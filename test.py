from regex_parser import regex_to_nfa
from dfa import match_string

regex = "ab*"

nfa = regex_to_nfa(regex)

tests = ["a", "ab", "abb", "abbb", "b"]

for s in tests:
    if match_string(nfa, s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")