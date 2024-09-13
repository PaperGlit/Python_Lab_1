def calculate(num1, num2, operator, digits):
    match operator:
        case "+":
            return round(num1 + num2, digits)
        case "-":
            return round(num1 - num2, digits)
        case "*":
            return round(num1 * num2, digits)
        case "/":
            return round(num1 / num2, digits)
        case "^":
            return round(num1 ** num2, digits)
        case "root":
            return round(num1 ** (1 / num2), digits)
        case "%":
            return round(num1 % num2, digits)
        case _:
            return "Error occurred during calculation"