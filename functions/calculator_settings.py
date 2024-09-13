def settings(digits):
    settings_prompt = input("1 - Change the amount of digits after a decimal point in a number, 2 - Clear history: ")

    match settings_prompt:
        case "1":
            while True:
                digits_prompt = input("Enter the amount of digits: ")
                try:
                    digits = int(digits_prompt)
                    print("Settings changed successfully")
                    return digits
                except ValueError:
                    print("Please enter a number")

        case "2":
            with open("history.txt", "w"):
                pass
            print("History cleared successfully")
            return digits

        case _:
            print("Invalid input")
            return digits
