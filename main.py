def calculator():
    operands = ["+", "-", "*", "/", "^", "root", "%"]
    memory = 0.0
    result = 0.0
    while True:

        while True:
            value1 = (input("Enter first number (or MR / MC): "))
            if value1.lower() == "mr":
                num1 = memory
                print("Recovered value: " + str(num1))
                break
            elif value1.lower() == "mc":
                memory = 0
                print("Memory cleared!")
                continue
            else:
                 try:
                     num1 = float(value1)
                     break
                 except ValueError:
                    print("Please enter a number")
                    continue

        operator_is_memory = False
        while True:
            operator = input("Enter operator: ")
            if operator.lower() == "ms":
                # noinspection PyUnboundLocalVariable
                memory = num1
                print("The value was stored in the memory!")
                operator_is_memory = True
                break
            elif operator not in operands:
                print("Please enter a valid operator")
                continue
            break
        if operator_is_memory:
            continue

        while True:
            value2 = (input("Enter second number (or MR / MC): "))
            if value2.lower() == "mr":
                num2 = memory
                print("Recovered value: " + str(num2))
                break
            elif value2.lower() == "mc":
                memory = 0
                print("Memory cleared!")
                continue
            else:
                try:
                    num2 = float(value2)
                    break
                except ValueError:
                    print("Please enter a number")
                    continue

        # noinspection PyUnboundLocalVariable
        if operator == "/" and num2 == 0:
            print("Error: cannot divide by zero")
        else:
            result = calculate(num1, num2, operator)
            # noinspection PyUnboundLocalVariable
            print("Result : " + str(result))

        try_again = input("Would you like to try again? (Y / N) // Store memory? (MS / M+ / M-): ").lower()

        match try_again:
            case "y":
                continue
            case "ms":
                memory = result
                print("Memory stored! Current value: " + str(memory))
                continue
            case "m+":
                memory += result
                print("Memory updated! Current value: " + str(memory))
                continue
            case "m-":
                memory -= result
                print("Memory updated! Current value: " + str(memory))
                continue
            case _:
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
