from interface import *
from operations import *
from customExceptions import *

WELCOME_MESSAGE = """
welcome to Omer's smart calculator!
operations allowed:
add         +       power       ^       average     @
sub         -       module      %       tildes      ~
mul         *       max         $       factorial   !
div         /       min         &       brackets    ()
"""
def isNum(num: str) -> bool:
    """
    gets a char
    returns if it is a number
    """
    try:
        float(num)
    except:
        return False
    return True

def IsLeagel(equation: str, index: float) -> bool:
    """
    gets a char
    returns if it is a number
    """
    if(index >= len(equation)):
        raise missingNumber(equation, equation)
    if not(isNum(equation[index])):
        if(isLegalDot(equation, index) or isNegNum(equation, index)):
            return True
        return False
    return True

def isLegalDot(equation: str, dotIndex: float) -> bool:
    if(equation[dotIndex] != '.'):
        return False
    if(dotIndex > 0 and dotIndex < len(equation)):
        if(isNum(equation[dotIndex-1]) or isNum(equation[dotIndex+1])):
            return True
    elif(dotIndex == 0):
        return isNum(equation[dotIndex+1])
    elif(dotIndex == len(equation)):
        return isNum(equation[dotIndex-1])
    return False

def isNegNum(equation: str, NegIndex: float) -> bool:
    if(equation[NegIndex] != '-'):
        return False
    if(NegIndex > 0 and NegIndex < len(equation)-1): #neg signe cand be without a num after it
        if(not(isNum(equation[NegIndex-1])) and IsLeagel(equation, NegIndex+1)): #neg num cant have a num on the left side of the neg num, its sub
            return True
    elif(NegIndex == 0):
        return IsLeagel(equation, NegIndex+1)
    return False

def removeSpacesAndNegSings(equation: str) -> str:
    """
    gets an equation
    returns the equation without spaces
    """
    length = len(equation)-1
    i = 0
    while(i < length): # runs on the equation and removes spaces
        if(equation[i] == " "):
            j = i #if there are several spaces together, i is the beggining of the spaces and j is the end
            while(j < length-1):
                if(equation[j+1] == " "):
                    j += 1
                else:
                    break
            equation = equation[0: i:] + equation[j + 1::] #remove the spaces
        i+=1
        length = len(equation)-1
    length = len(equation)-1
    i = 0
    while(i < length): # runs on the equation and removes neg signs
        if(isNegNum(equation, i)):
            k = i #if there are several - together, i is the beggining of the neg signs and k is the end
            while(k < length-1):
                if(isNegNum(equation, k+1)):
                    k += 1
                else:
                    break
            if((i-k) % 2 !=0):
                equation = equation[0: i:] + equation[k + 1::] #leaves one neg sign, UNdual num of neg signs
            else:
                equation = equation[0: i+1:] + equation[k + 1::] #remove the negs entirely, dual num of neg signs #leaves one neg sign, UNdual num of neg signs
        i+=1
        length = len(equation)-1
    return equation

def maxPrioritie(mathematical_equation:str) -> float:
    """
    gets an equation
    returns the max prioritie operator
    """
    max_Prioritie = 0
    length = len(mathematical_equation)
    i = 0
    while(i < length): # runs on the equation
        if not(IsLeagel(mathematical_equation, i)):
            try:
                max_Prioritie = PerformANoperation("$", max_Prioritie, getPriorities()[mathematical_equation[i]])
            except:
                raise notAmathematicalOperation(mathematical_equation[i], mathematical_equation)
        i+=1
    return max_Prioritie

def getIndexByPrioritie(mathematical_equation:str, prioritie:float) -> float:
    """
    gets an equation and the operator prioritie
    returns index of the first appearance of a given prioritie operator
    """
    length = len(mathematical_equation)
    i = 0
    while(i < length): # runs on the equation
        if not(IsLeagel(mathematical_equation, i)):
            try:
                if(getPriorities()[mathematical_equation[i]] == prioritie):
                    return i
            except:
                raise notAmathematicalOperation(mathematical_equation[i], mathematical_equation)
        i+= 1
    

def removeBrackets(mathematical_equation:str, index:float) -> str:
    """
    gets an equation and index
    returns the mathematical_equation with the value of the brackets insted of the equation indixe, that starts in a given index (if exists)
    """
    try:
        end_index = mathematical_equation.index(')')
    except:
        raise missingOperator(')', mathematical_equation)
    return mathematical_equation[0: index:] + solve(mathematical_equation[index+1:end_index]) + mathematical_equation[end_index + 1::] #returns the mathematical_equation with the brackets solved

def GetLeftNumIndex(mathematical_equation:str, index:float) -> float:
    """
    gets an equation and the operator index
    returns index of the start of the number that is on the left of the operator in the index given
    """
    num_index = index-1
    if not(IsLeagel(mathematical_equation, num_index)):
        raise missingNumber(mathematical_equation[num_index], mathematical_equation)
    if(num_index-1 >= 0):
        while((num_index-1 >= 0) and IsLeagel(mathematical_equation, num_index-1)):
            num_index -= 1
    if(num_index < 0):
        raise missingNumber(mathematical_equation[num_index], mathematical_equation)
    return num_index

def GetRightNumIndex(mathematical_equation:str, index:float) -> float:
    """
    gets an equation and the operator index
    returns index of theend of the number that is on the right of the operator in the index given
    """
    num_index = index+1
    if not(IsLeagel(mathematical_equation, num_index)):
        raise missingNumber(mathematical_equation[num_index], mathematical_equation)
    if(num_index+1 < len(mathematical_equation)):
        while((num_index+1 < len(mathematical_equation)) and IsLeagel(mathematical_equation, num_index+1)):
            num_index += 1
    return num_index

def OperatorOnRight(mathematical_equation: str, operatorIndex: int) -> str:
    left_num = GetLeftNumIndex(mathematical_equation, operatorIndex) #index of the start of the number that is on the left of the operator
    return mathematical_equation.replace(mathematical_equation[left_num:operatorIndex+1], str(PerformANoperation(mathematical_equation[operatorIndex],float(mathematical_equation[left_num:operatorIndex]),0))) #returns the mathematical_equation with the operand in index solved

def OperatorOnLeft(mathematical_equation: str, operatorIndex: int) -> str:
    right_num = GetRightNumIndex(mathematical_equation, operatorIndex) #index of the end of the number that is on the left of the operator
    return mathematical_equation.replace(mathematical_equation[operatorIndex:right_num+1], str(PerformANoperation(mathematical_equation[operatorIndex],float(mathematical_equation[operatorIndex+1:right_num+1]),0))) #returns the mathematical_equation with the operand in index solved

def OperatorOnCenter(mathematical_equation: str, operatorIndex: int) -> str:
    left_num = GetLeftNumIndex(mathematical_equation, operatorIndex) #index of the start of the number that is on the left of the operator
    right_num = GetRightNumIndex(mathematical_equation, operatorIndex) #index of the end of the number that is on the left of the operator
    return mathematical_equation.replace(mathematical_equation[left_num:right_num+1], str(PerformANoperation(mathematical_equation[operatorIndex],float(mathematical_equation[left_num:operatorIndex]),float(mathematical_equation[operatorIndex+1:right_num+1])))) #returns the mathematical_equation with the operand in index solved


def solve(mathematical_equation:str) -> float:
    mathematical_equation = removeSpacesAndNegSings(mathematical_equation)
    while not(isNum(mathematical_equation)): #run until all the operands executed
        index = getIndexByPrioritie(mathematical_equation, maxPrioritie(mathematical_equation)) # the index of the first appearance of the max prioritie operator
        if(mathematical_equation[index] == '('):
            mathematical_equation = removeBrackets(mathematical_equation, index) #the mathematical_equation with the brackets solved
        elif(mathematical_equation[index] == ')'):
            raise missingOperator('(', mathematical_equation) #if there is only ) without a (
        elif(mathematical_equation[index] in getRightOperators()):
            mathematical_equation = OperatorOnRight(mathematical_equation, index)
        elif(mathematical_equation[index] in getLeftOperators()):
            mathematical_equation = OperatorOnLeft(mathematical_equation, index)
        else:
            mathematical_equation = OperatorOnCenter(mathematical_equation, index)
    return mathematical_equation


def calculator(): #init for first run
    show(WELCOME_MESSAGE)
    mathematical_equation = None
    while(mathematical_equation == None): #if there was a problem with the input it will be re-entered
        mathematical_equation = get("Please enter the mathematical equation: \n")
    try:
        mathematical_equation = solve(mathematical_equation)
    except notAmathematicalOperation as err:
        showError(err)
    except AmathematicalException as err:
        showError(err)
    except missingOperator as err:
        showError(err)
    except missingNumber as err:
        showError(err)
    show(mathematical_equation)

#)

def main():#replace by index insted off slising
    calculator()
    """try:
        calculator()
    except Exception as err: #for raised exceptions
        if not(isinstance(err, EOFError)):
            showError(err)
        else: # if input is EOF
            showError(missingNumber("equation"))"""
if __name__ == "__main__":
    main()