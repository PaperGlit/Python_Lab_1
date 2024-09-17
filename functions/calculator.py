from functions import validate_num, validate_operator, validate_memory, calculate, history_write, try_again
from GlobalVariables import memory_operations


def perform(memory, digits):
    num1 = validate_num.validate(memory, "Enter first number (or MR / MC): ", digits)

    operator = validate_operator.validate()
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

    history_write.write(num1, num2, operator, result)

    return try_again.parse(memory, result)