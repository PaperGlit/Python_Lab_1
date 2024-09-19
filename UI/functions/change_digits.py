from BL.functions import validate_digits


def change():
    while True:
        digits_prompt = input("Enter the amount of digits: ")
        digits = validate_digits.validate(digits_prompt)
        if digits:
            print("Settings changed successfully")
            break
        else:
            print("Invalid input, please enter a valid non-negative integer number")