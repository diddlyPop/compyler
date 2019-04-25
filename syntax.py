"""
syntax - analyzes and verifies the structure of our Token list
"""
from lex import *


class Syntaxer:

    def E(self):
        self.In('E')
        self.Out('E')

    def Q(self):
        self.In('Q')
        self.Out('Q')

    def T(self):
        self.In('T')
        self.Out('T')

    def R(self):
        self.In('R')
        self.Out('R')

    def In(self, call_from):
        self.Print_Tier()
        self.tier += 1
        print("Exit %c" % call_from)

    def Out(self, call_from):
        self.Print_Tier()
        self.tier -= 1
        print("Exit %c" % call_from)

    def Print_Tier(self):
        for i in range(self.tier):
            print("-->")

    def Fetch(self):
        self.current_index += 1
        self.current = self.s_token_list[self.current_index]

    def __init__(self, f_name):
        self.aLexer = Lexer(f_name)
        self.s_token_list = self.aLexer.token_list
        self.current = self.s_token_list[0]
        self.current_index = 0
        self.tier = 0

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

