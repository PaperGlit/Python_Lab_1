def parse(string):
    #Out of those 3 variables, only num must be declared (the other 2 are just a safeguard)
    num = ""
    num1 = ""
    operator = ""
    for char in string:
        if char.isnumeric() or char == ".":
            num += char
            continue
        elif char == '+' or char == '-' or char == '*' or char == '/':
            operator = char
            num1 = float(num)
            num = ""
            continue
        else:
            print("Unknown character detected!")
            break
    num2 = float(num)
    return calculate(num1, num2, operator)


def calculate(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return "Error occurred during calculation"


inputString = input("Enter a string: ")
print(parse(inputString))
