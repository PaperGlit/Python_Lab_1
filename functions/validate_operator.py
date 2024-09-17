from GlobalVariables import *


def validate():
    while True:
        operator = (input("Enter operator (or MS / M+ / M-): ")).lower()
        if operator in operands or operator in memory_operations:
            return operator
        else:
            print("Please enter a valid operator")