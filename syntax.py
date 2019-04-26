"""
syntax - analyzes and verifies the structure of our Token list
"""
from lex import *
import sys


class Syntaxer:

    def S(self):        # S -> i = E
        if self.need_print:
            self.current.rules_used.append(self.rules_dict['S'])
        self.In('S')
        if self.current.token_type == "Identifier":
            self.Check_and_Fetch("Identifier")
            self.Check_and_Fetch('=')
            self.E()
        self.Out('S')

    def E(self):        # E -> TQ
        if self.need_print:
            self.current.rules_used.append(self.rules_dict['E'])
        self.In('E')
        self.T()
        self.Q()
        self.Out('E')

    def Q(self):        # Q -> +TQ | -TQ | sigma
        if self.need_print:
            self.current.rules_used.append(self.rules_dict['Q'])
        self.In('Q')
        if self.current.lexeme is ';':
            self.Check_and_Fetch(';')
        elif self.current.lexeme is '+':
            self.Check_and_Fetch('+')
            self.T()
            self.Q()
        elif self.current.lexeme is '-':
            self.Check_and_Fetch('-')
            self.T()
            self.Q()
        self.Out('Q')

    def T(self):        # T -> FR
        if self.need_print:
            self.current.rules_used.append(self.rules_dict['T'])
        self.In('T')
        self.F()
        self.R()
        self.Out('T')

    def R(self):        # R -> *FR | /FR | sigma
        if self.need_print:
            self.current.rules_used.append(self.rules_dict['R'])
        self.In('R')
        if self.current.lexeme is ';':
            self.Check_and_Fetch(';')
        elif self.current.lexeme is '*':
            self.Check_and_Fetch('*')
            self.T()
            self.Q()
        elif self.current.lexeme is '/':
            self.Check_and_Fetch('/')
            self.T()
            self.Q()
        self.Out('R')

    def F(self):        # F -> (E) | i
        if self.need_print:
            self.current.rules_used.append(self.rules_dict['F'])
        self.In('F')
        if self.current.lexeme is '(':
            self.Check_and_Fetch('(')
            self.E()
            self.Check_and_Fetch(')')
        elif self.current.token_type is "Identifier":
            self.Check_and_Fetch("Identifier")
        else:
            self.errors.append("Error in F with %s " % self.current.lexeme)
        self.Out('F')

    def In(self, call_from):
        self.tier += 1
        self.Print_Tier(call_from, "In")

    def Out(self, call_from):
        self.Print_Tier(call_from, "Out")
        self.tier -= 1

    def Print_Tier(self, called_from, in_or_out):
        for i in range(self.tier):
            self.tier_print_result += "--> "
        self.tier_print_result += in_or_out + " "
        self.tier_print_result += called_from
        self.tier_print_result += '\n'

    def Error_Check(self):
        if len(self.errors) >= 1:
            for i in range(len(self.errors)):
                print(self.errors[i])
        else:
            print("\nSyntax Passes!")

    def Start_Analyzing(self):
        while not self.end_of_list:
            self.S()
        self.Error_Check()
        print('\n' + self.tier_print_result)

    def Check_and_Fetch(self, check_against):
        if self.current.lexeme is check_against or self.current.token_type is check_against:
            if self.current_index == len(self.s_token_list) - 1:
                self.Print_Token()
                self.current.lexeme = ""
                self.end_of_list = True
                self.need_print = False
                print("\nEnd of List")
            else:
                self.Print_Token()
                self.current_index += 1
                self.current = self.s_token_list[self.current_index]
        else:
            self.errors.append("Error finding %s" % self.current.lexeme)

    def Print_Token(self):
        result = '\n'
        result += "Token: %s \t" % self.current.token_type
        result += "Lexeme: %s " % self.current.lexeme
        print(result)
        for i in range(len(self.current.rules_used)):
            print(self.current.rules_used[i])

    def __init__(self, f_name, p_bool):
        self.aLexer = Lexer(f_name)
        self.s_token_list = self.aLexer.token_list
        self.current = self.s_token_list[0]
        self.current_index = 0
        self.tier = 0
        self.end_of_list = False
        self.errors = []
        self.need_print = p_bool
        self.rules_dict = {'S': "S -> i = E", 'E': "E -> TQ", 'T': "T -> FR", 'Q': "Q -> +TQ | -TQ | sigma",
                                'F': "(E) | i", 'R': "R -> *FR | /FR | sigma"}
        self.tier_print_result = ""

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
    file_name = "input2.txt"
    if len(file_name) < 3:
        file_name = sys.argv[1]
        while file_name[-4:] != ".txt" or not os.path.isfile(file_name):
            if file_name[-4:] != ".txt":
                file_name = input("Input must be .txt file: ")
            if not os.path.isfile(file_name):
                print("File cannot be found in this directory.")
                file_name = input("Enter new file: ")
    aSyntaxer = Syntaxer(file_name, True)
    aSyntaxer.Start_Analyzing()

