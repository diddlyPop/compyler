"""
syntax - analyzes and verifies the structure of our Token list
"""
from lex import *
import sys


class Syntaxer:

    def S(self):        # S -> i = E
        self.In('S')
        if self.current.token_type == "Identifier":
            self.Check_and_Fetch("Identifier")
            self.Check_and_Fetch('=')
            self.E()
        self.Out('S')

    def E(self):        # E -> TQ
        self.In('E')
        self.T()
        self.Q()
        self.Out('E')

    def E_Prime(self):
        self.In("E_Prime")
        self.Out("E_Prime")

    def Q(self):        # Q -> +TQ | -TQ | sigma
        self.In('Q')
        if self.current.lexeme is '+':
            self.Check_and_Fetch('+')
            self.T()
            self.Q()
        elif self.current.lexeme is '-':
            self.Check_and_Fetch('-')
            self.T()
            self.Q()
        else:
            return None
            # TODO sigma
        self.Out('Q')

    def T(self):        # T -> FR
        self.In('T')
        self.F()
        self.R()
        self.Out('T')

    def R(self):        # R -> *FR | /FR | sigma
        self.In('R')
        if self.current.lexeme is '*':
            self.Check_and_Fetch('*')
            self.T()
            self.Q()
        elif self.current.lexeme is '/':
            self.Check_and_Fetch('/')
            self.T()
            self.Q()
        else:
            return None
            # TODO sigma
        self.Out('R')

    def F(self):        # F -> (E) | i
        self.In('F')
        self.Out('F')

    def In(self, call_from):
        self.Print_Tier(call_from, "In")
        self.tier += 1

    def Out(self, call_from):
        self.Print_Tier(call_from, "Out")
        self.tier -= 1

    def Print_Tier(self, called_from, in_or_out):
        tier_print_result = ""
        for i in range(self.tier + 1):
            tier_print_result += "--> "
        tier_print_result += in_or_out + " "
        tier_print_result += called_from
        print(tier_print_result)

    def Check_and_Fetch(self, check_against):
        if self.current.lexeme is check_against or self.current.token_type is check_against:
            if self.current_index == len(self.s_token_list) - 1:
                self.end_of_list = True
                print("end of token list")
            else:
                self.Print_Token()
                self.current_index += 1
                self.current = self.s_token_list[self.current_index]
        else:
            print("error fetching")
            exit("error fetching")

    def __init__(self, f_name):
        self.aLexer = Lexer(f_name)
        self.s_token_list = self.aLexer.token_list
        self.current = self.s_token_list[0]
        self.current_index = 0
        self.tier = 0
        self.end_of_list = False
        self.S()

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

    def Print_Token(self):
        result = '\n'
        result += "Token: %s \t" % self.current.token_type
        result += "Lexeme: %s " % self.current.lexeme
        result += '\n'
        print(result)


if __name__ == "__main__":
    file_name = "input2.txt"
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

