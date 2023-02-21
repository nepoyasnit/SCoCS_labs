ADD_OPERATOR = 'add'
SUB_OPERATOR = 'sub'
MUL_OPERATOR = 'mult'
DIV_OPERATOR = 'div'


def calculate(first_number: float, second_number: float, operator: str):
    if operator == ADD_OPERATOR:
        return first_number + second_number
    elif operator == SUB_OPERATOR:
        return first_number - second_number
    elif operator == MUL_OPERATOR:
        return first_number * second_number
    elif operator == DIV_OPERATOR:
        return first_number / second_number
