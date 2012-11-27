'''
Created on 20 Nov 2012

@author: chris
'''

def _add(num1, num2):
    '''
    This method is for easy math operator selection
    '''
    return num1 + num2


def _sub(num1, num2):
    '''
    This method is for easy math operator selection
    '''
    return num1 - num2


def _mul(num1, num2):
    '''
    This method is for easy math operator selection
    '''
    return num1 * num2


def _div(num1, num2):
    '''
    This method is for easy math operator selection
    '''
    if num2 == 0:
        res = 0
    else:
        res = num1 / num2
    
    return res


def resolve_points(equation, info_dict):
    '''
    This returns the result of the activity
    '''
    if not isinstance(equation, list):
        if isinstance(equation, int) or isinstance(equation, long) or isinstance(equation, float):
            return equation
        elif isinstance(equation, str):
            return info_dict[equation]
        else:
            raise Exception("Unrecognised entry in equation: " + str(equation + " which is of " + str(type(equation))))
    elif len(equation) == 3:
        num1 = resolve_points(equation[0], info_dict)
        num2 = resolve_points(equation[2], info_dict)
        op = equation[1]
        result = getattr(__import__("math_solver"),"_" + op)(num1, num2)
        return result
    else:
        raise Exception("Incorrect number of args in equation: " + str(equation))