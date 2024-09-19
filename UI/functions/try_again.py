from UI.functions import validate_memory
from GlobalVariables import memory_operations


def parse(result):
    try_again = input("Would you like to try again? (Y / N) // Store a value into memory? (MS / M+ / M-): ").lower()
    if try_again in memory_operations:
        validate_memory.validate(try_again, result)
    elif try_again == "y":
        return False
    else:
        return True