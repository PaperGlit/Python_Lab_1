import os


def calculator():
    memory = 0.0
    result = 0.0
    memory_operations = ["ms", "m+", "m-"]

    while True:
        while True:
            main_prompt = input("1 - Calculate a number, 2 - View history: ")
            if main_prompt == "1":
                break
            elif main_prompt == "2":
                with open("history.txt", "r") as file:
                    print("Your history:\n" + file.read())
                continue
            else:
                print("Invalid input")
                continue

        num1 = validate_num(memory, "Enter first number (or MR / MC): ")

        operator = validate_operator()
        if operator == "ms":
            memory = num1
            print("Memory value stored! Current value: " + str(memory))
            continue

        num2 = validate_num(memory, "Enter second number (or MR / MC): ")

        if operator == "/" and num2 == 0:
            print("Error: cannot divide by zero")
        else:
            result = calculate(num1, num2, operator)
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


def validate_operator():
    operands = ["+", "-", "*", "/", "^", "root", "%"]
    while True:
        operator = (input("Enter operator (or MS): ")).lower()
        if operator == "ms":
            return operator
        elif operator in operands:
            return operator
        else:
            print("Please enter a valid operator")


def validate_memory(value, memory, num):
    match value:
        case "ms":
            memory = num
            print("Memory value stored! Current value: " + str(memory))
        case "m+":
            memory += num
            print("Memory value updated! Current value: " + str(memory))
        case "m-":
            memory -= num
            print("Memory value updated! Current value: " + str(memory))
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
    with open("history.txt", "x") as f:
        pass
calculator()
