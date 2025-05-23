'''
Calculator functions
'''

class CalcError(ValueError):
    '''Custom Exceptions for Calculator functions'''
    pass

def calculate(expr_list):
    '''
    Accepts a list of strings containing numbers and operators.
    Returns the result of calculating the expression as an `int` or `float`.
    '''
    # needs to be list of 3 items
    if not isinstance(expr_list, list) or len(expr_list) != 3:
        raise CalcError('Expression must be a list of three strings')

    return None
