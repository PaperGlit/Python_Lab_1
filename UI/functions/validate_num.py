import GlobalVariables

def validate(num_prompt = "Enter the number (or MR / MC)"):
    while True:
        value = (input(num_prompt)).lower()

        if value.lower() == "mr":
            print("Recovered value: " + str(GlobalVariables.memory))
        elif value.lower() == "mc":
            GlobalVariables.memory = 0.0
            print("Memory cleared!")
        else:
            try:
                return round(float(value), GlobalVariables.digits)
            except ValueError:
                print("Please enter a valid number / memory operation")