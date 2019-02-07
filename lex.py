"""
lex - creates tokens from keywords, identifiers, operators, numbers, and brackets through parsing
"""
from enum import Enum


class Token:

    def __init__(self, t_lexeme, t_type):
        self.lexeme = t_lexeme                     # value of token
        self.token_type = t_type      # type of token (keyword, number, etc.)

class State(Enum):
    IN = 0,
    S1 = 1,
    S2 = 2,
    S3 = 3,
    S4 = 4,
    S5 = 5,
    S6 = 6,
    TR = 3


class Transition(Enum):
    LETTER = 0,
    DIGIT = 1,
    DOT = 2,
    UNKNOWN = -1


class Lexer:
    def traverse_file_for_tokens(self, file_name):  # open user specified file, parse through files and create Token
        this_state = 0
        prev_state = 0
        lexeme = ""
        with open(file_name) as fileobj:
            for line in fileobj:
                for ch in line:             # to increment character by character
                    transition = self.determine_transition(ch)
                    this_state = self.state_table[this_state][transition]
                    if this_state is State.TR:
                        token_type = self.determine_type(prev_state)
                        if token_type is not "Unknown":
                            if token_type is "Identifier":
                                if lexeme.iskeyword():
                                    token_type = "Keyword"
                            self.token_list.append(Token(lexeme, token_type))
                            this_state = State.IN
                            lexeme = ""
                            token_type = ""
                    else:
                        if not ch.isspace():
                            lexeme += ch
                    prev_state = this_state



    def determine_transition(self, current_character):
        trans_type = -1
        if current_character.isalpha():
            trans_type = 0
        if current_character.isdigit():
            trans_type = 1
        if current_character is ".":
            trans_type = 2
        return trans_type

    def determine_type(self, prev_state):
        # TODO

    def __init__(self):
        self.token_list = []
        self.state_table = [ [1, 2, 7],
                             [3, 4, 7],
                             [7, 2, 5],
                             [3, 4, 7],
                             [3, 4, 7],
                             [7, 6, 7],
                             [7, 6, 7],
                             [7, 7, 7]  ]
        self.traverse_file_for_tokens(input("Enter File Name: "))

    def __str__(self):
        result = "Tokens:" + '\n'
        for x in range(len(self.token_list)):
            result += str(self.token_list[x].value) + ", " + self.token_list[x].token_type
        return result


if __name__ == "__main__":
    newLexer = Lexer()
    print(newLexer)

