from DAL.functions import history_write
import GlobalVariables


def validate(operation, num):
    match operation:
        case "ms":
            GlobalVariables.memory = num
            print("Memory value stored! Current value: " + str(GlobalVariables.memory))
        case "m+":
            num_sum = GlobalVariables.memory + num
            history_write.write(str(GlobalVariables.memory), str(num), "+", str(num_sum))
            GlobalVariables.memory += num
            print("Memory value updated and saved into history! Current value: " + str(GlobalVariables.memory))
        case "m-":
            num_diff = GlobalVariables.memory - num
            history_write.write(str(GlobalVariables.memory), str(num), "-", str(num_diff))
            GlobalVariables.memory -= num
            print("Memory value updated and saved into history! Current value: " + str(GlobalVariables.memory))
        case _:
            print("Error occurred during memory validation")