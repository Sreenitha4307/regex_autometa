from regex_parser import regex_to_nfa
from dfa import match_string
from visualizer import draw_nfa

regex = input("Enter regex: ")

nfa = regex_to_nfa(regex)

draw_nfa(nfa)

while True:
    string = input("Enter string to test: ")

    if match_string(nfa, string):
        print("Accepted")
    else:
        print("Rejected")