import os


def calculator():
    memory = 0.0
    result = 0.0
    digits = 3
    memory_operations = ["ms", "m+", "m-"]
    operands = ["+", "-", "*", "/", "^", "root", "%"]

    while True:
        main_prompt = input("1 - Calculate a number, 2 - View history, 3 - Additional settings: ")

        match main_prompt:
            case "1":
                num1 = round(validate_num(memory, "Enter first number (or MR / MC): "), digits)

                operator = validate_operator(operands, memory_operations)
                if operator in memory_operations:
                    memory = validate_memory(operator, memory, num1)
                    continue

                num2 = round(validate_num(memory, "Enter second number (or MR / MC): "), digits)

                if operator == "/" and num2 == 0:
                    print("Error: cannot divide by zero")
                else:
                    result = round(calculate(num1, num2, operator), digits)
                    print("Result : " + str(result))

                history_write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result))
                print("The operation was saved into history")

                try_again = input("Would you like to try again? (Y / N) // Store memory? (MS / M+ / M-): ").lower()
                if try_again in memory_operations:
                    memory = validate_memory(try_again, memory, result)
                elif try_again == "y":
                    result = 0.0
                    continue
                else:
                    break

            case "2":
                with open("history.txt", "r") as file:
                    print("Your history:\n" + file.read())

            case "3":
                settings_prompt = input("1 - Change the amount of digits after a dot in a number, 2 - Clear history: ")

                match settings_prompt:
                    case "1":
                        while True:
                            digits_prompt = input("Enter the amount of digits: ")
                            try:
                                digits = int(digits_prompt)
                                print("Settings changed successfully")
                                break
                            except ValueError:
                                print("Please enter a number")

                    case "2":
                        with open("history.txt", "w"):
                            pass
                        print("History cleared successfully")

                    case _:
                        print("Invalid input")

            case _:
                break


def validate_num(memory, num_prompt):
    while True:
        value = (input(num_prompt)).lower()

        if value.lower() == "mr":
            print("Recovered value: " + str(memory))
            return memory
        elif value.lower() == "mc":
            memory = 0.0
            print("Memory cleared!")
        else:
            try:
                return float(value)
            except ValueError:
                print("Please enter a valid number / memory operation")


def validate_operator(operands, memory_operations):
    while True:
        operator = (input("Enter operator (or MS / M+ / M-): ")).lower()
        if operator in memory_operations or operator in operands:
            return operator
        else:
            print("Please enter a valid operator")


def validate_memory(operation, memory, num):
    match operation:
        case "ms":
            memory = num
            print("Memory value stored! Current value: " + str(memory))
        case "m+":
            history_write(str(memory) + " + " + str(num) + " = " + str(memory + num))
            memory += num
            print("Memory value updated and saved into history! Current value: " + str(memory))
        case "m-":
            history_write(str(memory) + " - " + str(num) + " = " + str(memory - num))
            memory -= num
            print("Memory value updated and saved into history! Current value: " + str(memory))
        case _:
            print("Error occurred during memory validation")
            return 0.0
    return memory


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


def history_write(value):
    with open("history.txt", "r") as history_file:
        history = history_file.read()
        if history == "":
            new_history = value
        else:
            new_history = value + "\n" + history
    with open("history.txt", "w") as history_file:
        history_file.write(new_history)


if not os.path.exists("history.txt"):
    with open("history.txt", "x"):
        pass
calculator()
