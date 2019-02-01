"""
lex - creates tokens from keywords, identifiers, operators, numbers, and brackets through parsing
"""


class Tokenizer:

    def __init__(self, value):
        self.value = value                      # value of token
        self.token_type = self.get_type()       # type of token (keyword, number, etc.)

    def check_number(self):
        correct_type = False
        possible_values = [1, 2, 3]
        if self.value in possible_values:
            correct_type = True
        return correct_type

    def check_bracket(self):                    # can this be reduced to a single check in get_type()?
        correct_type = False                    # if self.value in possible_brackets[]
        possible_values = ['[', ']', '{', '}']  # need to figure out where to put that possible_brackets list
        if self.value in possible_values:
            correct_type = True
        return correct_type

    def get_type(self):                         # determines type of token
        if self.check_number():
            return "Integer"
        if self.check_keyword():
            return "Keyword"
        if self.check_indentifier():
            return "Identifier"
        if self.check_operator():
            return "Operator"
        return "Incompatible"


class Lexer:

    def traverse_file_for_tokens(self, file_name):  # open user specified file, parse through files and send to Tokenizer
        open(file=file_name)
        self.token_list.append(Tokenizer(2))

    def __init__(self):
        self.token_list = []
        self.traverse_file_for_tokens(input("Enter File Name: "))

    def __str__(self):
        result = "Tokens:" + '\n'
        for x in range(len(self.token_list)):
            result += str(self.token_list[x].value) + ", " + self.token_list[x].token_type
        return result


if __name__ == "__main__":
    newLexer = Lexer()
    print(newLexer)

