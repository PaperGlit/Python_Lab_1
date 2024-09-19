import GlobalVariables


def validate(digits_prompt):
    try:
        digits = int(digits_prompt)
        if digits >= 0:
            GlobalVariables.digits = digits
            return True
        else:
            return False
    except ValueError:
        return False