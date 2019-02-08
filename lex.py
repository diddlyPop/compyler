"""
lex - creates tokens from keywords, identifiers, operators, numbers, and brackets through parsing
"""
from enum import IntEnum, Enum
import keyword


class Token:

    def __init__(self, t_lexeme, t_type):
        self.lexeme = t_lexeme                     # value of token
        self.token_type = t_type      # type of token (keyword, number, etc.)


class State(IntEnum):
    IN = 0,
    S1 = 1,
    S2 = 2,
    S3 = 3,
    S4 = 4,
    S5 = 5,
    S6 = 6,
    TR = 7


class Transition(Enum):
    LETTER = 0,
    DIGIT = 1,
    DOT = 2,
    SPACE = 3,
    UNKNOWN = -1


class Lexer:
    def traverse_file_for_tokens(self, file_name):  # open user specified file, parse through files and create Token
        this_state = State.IN.value                   # first state and first prev state are 0
        prev_state = State.IN.value
        lexeme = ""
        with open(file_name) as fileobj:
            for line in fileobj:            # increment through each line in file
                for ch in line:             # to increment character by character, VERIFIED character recognition
                    transition = self.determine_transition(ch)              # transition is type of the next ch
                    this_state = self.state_table[this_state][transition]   # set new state based on trans and cur state
                    if this_state == State.TR.value:                              # if reached a terminating state
                        token_type = self.determine_type(prev_state)        # type depends on prev state
                        if token_type != "Unknown":                     # if type of token is not unknown
                            if token_type == "Identifier":                  # check for identifier to find keywords
                                if keyword.iskeyword(lexeme):
                                    token_type = "Keyword"
                            self.token_list.append(Token(lexeme, token_type))   # add token to token_list[]
                            this_state = State.IN.value                            # set state back to initial
                            lexeme = ""                                         # reset lexeme and token_type
                            token_type = ""
                    else:
                        if not ch.isspace():                                    # if not TR state or a space, add to val
                            lexeme += ch                                        # add current character
                    prev_state = this_state                                     # set prev state to the state just used

    def determine_transition(self, current_character):                          # depending on value of ch,
        trans_type = -1                                                         # type may be Unknown (-1)
        if current_character.isalpha():                                         # or a letter
            trans_type = 0
        if current_character.isdigit():                                         # or a digit
            trans_type = 1
        if current_character is ".":                                            # or a dot
            trans_type = 2
        if current_character is " ":
            trans_type = 3
        return trans_type   # VERIFIED returns int

    def determine_type(self, prev_state):
        token_type = "Unknown"
        if prev_state == State.S5 or prev_state == State.S6:
            token_type = "Real"
        if prev_state == State.S4 or prev_state == State.S1 or prev_state == State.S2 or prev_state == State.S3:
            token_type = "Identifier"
        if prev_state == State.S2:
            token_type = "Integer"
        return token_type

    def __init__(self):
        self.token_list = []
        self.state_table = [[1, 2, 7, 7],
                            [3, 4, 7, 7],   # accepted
                            [7, 2, 5, 7],   # accepted
                            [3, 4, 7, 7],   # accepted
                            [3, 4, 7, 7],   # accepted
                            [7, 6, 7, 7],
                            [7, 6, 7, 7],
                            [7, 7, 7, 7]]
        self.traverse_file_for_tokens("program.txt")

    def __str__(self):
        result = "Tokens:" + str(len(self.token_list)) + '\n'
        for x in range(len(self.token_list)):
            result += str(self.token_list[x].lexeme) + ", " + self.token_list[x].token_type + '\n'
        return result


if __name__ == "__main__":
    newLexer = Lexer()
    print(newLexer)

