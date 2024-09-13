from functions import validate_num, validate_operator, validate_memory, calculate, history_write
from GlobalVariables import *


def perform(memory, digits):
    num1 = validate_num.validate(memory, "Enter first number (or MR / MC): ", digits)

    operator = validate_operator.validate(operands, memory_operations)
    if operator in memory_operations:
        validate_memory.validate(operator, memory, num1)
        return False

    num2 = validate_num.validate(memory, "Enter second number (or MR / MC): ", digits)

    if operator == "/" and num2 == 0:
        print("Error: cannot divide by zero")
        return False
    else:
        result = calculate.calculate(num1, num2, operator, digits)
        print("Result : " + str(result))

    history_write.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result))
    print("The operation was saved into history")

    try_again = input("Would you like to try again? (Y / N) // Store a value into memory? (MS / M+ / M-): ").lower()
    if try_again in memory_operations:
        validate_memory.validate(try_again, memory, result)
    elif try_again == "y":
        return False
    else:
        return True