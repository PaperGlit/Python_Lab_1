def write(value):
    with open("history.txt", "r") as history_file:
        history = history_file.read()
        if history == "":
            new_history = value
        else:
            new_history = value + "\n" + history
    with open("history.txt", "w") as history_file:
        history_file.write(new_history)
