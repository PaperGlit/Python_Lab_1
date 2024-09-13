def validate(memory, num_prompt, digits):
    while True:
        value = (input(num_prompt)).lower()

        if value.lower() == "mr":
            print("Recovered value: " + str(memory))
            return memory
        elif value.lower() == "mc":
            memory = 0.0
            print("Memory cleared!")
        else:
            try:
                return round(float(value), digits)
            except ValueError:
                print("Please enter a valid number / memory operation")