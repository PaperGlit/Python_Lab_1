def write(num1, num2, operator, result):
    with open("history.txt", "a") as history_file:
        history_file.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result) + "\n")
    print("The operation was saved into history")

