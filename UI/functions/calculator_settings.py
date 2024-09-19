from UI.functions import change_digits
from DAL.functions import history_clear


def settings():
    settings_prompt = input("1 - Change the amount of digits after a decimal point in a number, 2 - Clear history: ")

    match settings_prompt:
        case "1":
            change_digits.change()

        case "2":
            history_clear.clear()
            print("History cleared successfully")

        case _:
            print("Invalid input")