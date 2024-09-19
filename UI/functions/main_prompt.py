from DAL.functions import history_read
from UI.functions import calculator_settings
from BL.functions import calculator


#False - continue; True - break
def prompt():
    case = input("1 - Calculate a number, 2 - View history, 3 - Additional settings: ")
    match case:
        case "1":
            return calculator.perform()
        case "2":
            history_read.read()
            return False
        case "3":
            calculator_settings.settings()
            return False
        case _:
            return True