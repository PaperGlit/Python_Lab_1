def validate(ops, mem_ops):
    while True:
        operator = (input("Enter operator (or MS / M+ / M-): ")).lower()
        if operator in mem_ops or operator in ops:
            return operator
        else:
            print("Please enter a valid operator")