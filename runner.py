from GlobalVariables import *
from functions import validate_num, validate_operator, validate_memory, calculate, history_write

def calculator():
    memory = 0.0
    result = 0.0
    digits = 3

    while True:
        main_prompt = input("1 - Calculate a number, 2 - View history, 3 - Additional settings: ")

        match main_prompt:
            case "1":
                num1 = validate_num.validate(memory, "Enter first number (or MR / MC): ", digits)

                operator = validate_operator.validate(operands, memory_operations)
                if operator in memory_operations:
                    memory = validate_memory.validate(operator, memory, num1)
                    continue

                num2 = validate_num.validate(memory, "Enter second number (or MR / MC): ", digits)

                if operator == "/" and num2 == 0:
                    print("Error: cannot divide by zero")
                else:
                    result = round(calculate.calculate(num1, num2, operator), digits)
                    print("Result : " + str(result))

                history_write.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result))
                print("The operation was saved into history")

                try_again = input("Would you like to try again? (Y / N) // Store a value into memory? (MS / M+ / M-): ").lower()
                if try_again in memory_operations:
                    memory = validate_memory.validate(try_again, memory, result)
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