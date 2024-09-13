from functions import history_write

def validate(operation, memory, num):
    match operation:
        case "ms":
            memory = num
            print("Memory value stored! Current value: " + str(memory))
        case "m+":
            history_write.write(str(memory) + " + " + str(num) + " = " + str(memory + num))
            memory += num
            print("Memory value updated and saved into history! Current value: " + str(memory))
        case "m-":
            history_write.write(str(memory) + " - " + str(num) + " = " + str(memory - num))
            memory -= num
            print("Memory value updated and saved into history! Current value: " + str(memory))
        case _:
            print("Error occurred during memory validation")
            return 0.0
    return memory