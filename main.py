def calculator():
    operands = ["+", "-", "*", "/", "^", "root", "%"]
    while True:

        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Please enter a number")
                continue

        while True:
            operator = input("Enter operator: ")
            if operator not in operands:
                print("Please enter a valid operator")
                continue
            break

        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Please enter a number")
                continue

        # noinspection PyUnboundLocalVariable
        if operator == "/" and num2 == 0:
            return "Error: cannot divide by zero"

        # noinspection PyUnboundLocalVariable
        print("Result : " + str(calculate(num1, num2, operator)))

        try_again = input("Would you like to try again? (y/n): ").lower()

        if try_again != "y":
            break



def calculate(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "^":
            return num1 ** num2
        case "root":
            return num1 ** (1 / num2)
        case "%":
            return num1 % num2
        case _:
            return "Error occurred during calculation"

calculator()