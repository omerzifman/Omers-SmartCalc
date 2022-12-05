from customExceptions import *
PRIORITY_DICT = {
        '(' : 7,
        '!' : 6,
        '~' : 6,
        '#' : 6,
        '@' : 5,
        '&' : 5,
        '$' : 5,
        '%' : 4,
        '^' : 3,
        '/' : 2,
        '*' : 2,
        '-' : 1,
        '+' : 1,
        ')' : 0
    }
LEFT_OPERATORS = ['~'] # for operators that need the number to be on the left
RIGHT_OPERATORS = ['!', '#'] # for operators that need the number to be on the right

def __add__(x, y) -> float:
    """
    gets 2 floats - x,y
    return the sum of x,y in a float form
    """
    return x+y

def __sub__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the subtraction of y on x in a float form
    """
    return x-y

def __mul__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the multiplication of y on x in a float form
    """
    return x*y

def __div__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the division of x,y in a float form
    """
    if(y == 0):
        raise AmathematicalException("cant div by zero")
    return x/y

def __pow__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the power of y on x in a float form
    """
    if(x < 0 and 1<y<0):
        return AmathematicalException("cant do power on "+ str(x) + " " + str(y))
    elif(y < 0 and 1<x<0):
        return AmathematicalException("cant do power on "+ str(x) + " " + str(y))
    return x**y

def __module__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the module of y on x in a float form
    """
    return x%y

def __max__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the max of x,y in a float form
    """
    if(x>y):
        return x
    return y

def __min__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the min of x,y in a float form
    """
    if(x>y):
        return y
    return x

def __avg__(x,y) -> float:
    """
    gets 2 floats - x,y
    return the average of x,y in a float form
    """
    return (x+y)/2.0

def __factorial__(x) -> int:
    """
    gets 1 floats - x
    return the factorial of x in a float form
    """
    if(x < 0):
        raise AmathematicalException("factorial isnt valid for neg numbers")
    if(x%1 != 0):
        raise AmathematicalException("factorial isnt valid for unNatural numbers")
    facto = 1
    for i in range(1,int(x)+1): #the casting is in case the x is a float, like 7.0
        facto = facto * i
    return facto

def __tildes__(x) -> float:
    """
    gets 1 floats - x
    return the tildes of x in a float form
    """
    return (-1)*x

def __sum__(x) -> float:
    """
    gets 1 float - x
    return the sum of  all digits of x in a int form
    """
    sign = 1 #the x sign
    if(x < 0):
        sign = -1 #the x sign
        x *= (-1)
    if(x%1 != 0):
        raise AmathematicalException("digits sum isnt valid for unNatural numbers")
    x = int(x) # x has to be a natural number
    sum = 0
    for digit in str(x): 
        sum += int(digit)      
    return sum*sign #returns the sign to the sum

def getPriorities():
    return PRIORITY_DICT

def getLeftOperators():
    return LEFT_OPERATORS

def getRightOperators():
    return RIGHT_OPERATORS