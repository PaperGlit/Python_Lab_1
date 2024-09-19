from UI.functions import try_again, validate_operator, validate_num, validate_memory, num_prompt, calculator_result
from DAL.functions import history_write
from GlobalVariables import memory_operations


#False - continue; True - break
def perform():
    num1 = validate_num.validate(num_prompt.prompt(1))

    operator = validate_operator.validate()
    if operator in memory_operations:
        validate_memory.validate(operator, num1)
        return False

    num2 = validate_num.validate(num_prompt.prompt(2))

    result = calculator_result.find(num1, num2, operator)

    if not result:
        return False

    history_write.write(num1, num2, operator, result)

    return try_again.parse(result)