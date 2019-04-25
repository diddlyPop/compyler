"""
syntax - analyzes and verifies the structure of our Token list
"""
from lex import *


class Syntaxer:

    def __init__(self, file_name):
        aLexer = Lexer(file_name)
        print(aLexer)

    def __str__(self):
        result = '\n'
        result += "Tokens: " + str(len(self.s_token_list)) + "\t\t Lexemes" + '\n'
        for x in range(len(self.s_token_list)):
            result += str(self.s_token_list[x].token_type)
            if str(self.s_token_list[x].token_type) == "Keyword" or str(self.s_token_list[x].token_type) == "Integer" or \
                    str(self.s_token_list[x].token_type) == "Real":
                result += "\t"
            result += "\t\t "
            result += self.s_token_list[x].lexeme + '\n'
        return result


if __name__ == "__main__":
    file_name = "input1.txt"
    if len(file_name) < 3:
        file_name = sys.argv[1]
        while file_name[-4:] != ".txt" or not os.path.isfile(file_name):
            if file_name[-4:] != ".txt":
                file_name = input("Input must be .txt file: ")
            if not os.path.isfile(file_name):
                print("File cannot be found in this directory.")
                file_name = input("Enter new file: ")
    aSyntaxer = Syntaxer(file_name)
    print(aSyntaxer)

