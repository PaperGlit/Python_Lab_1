from BL.functions import calculate


def find(num1, num2, operator):
    if operator == "/" and num2 == 0:
        print("Error: cannot divide by zero")
        return False
    else:
        result = calculate.calculate(num1, num2, operator)
        print("Result : " + str(result))
        return result