def read():
    with open("history.txt", "r") as file:
        print("Your history:\n" + file.read())