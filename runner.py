from functions import calculator, history_read, calculator_settings


def main():
    memory = 0.0
    digits = 3

    while True:
        main_prompt = input("1 - Calculate a number, 2 - View history, 3 - Additional settings: ")
        match main_prompt:
            case "1":
                code_break = calculator.perform(memory, digits)
                if code_break:
                    break
                else:
                    continue
            case "2":
                history_read.read()
            case "3":
                digits = calculator_settings.settings(digits)
            case _:
                break