class Error(Exception):
    """Base class for other custom exceptions"""
    def getName(self):
        pass
        """return exception name"""
    def getMessage(self):
        pass
        """return exception message"""
    def getEquation(self):
        pass
        """return equation"""

class notAmathematicalOperation(Error):
    """exception - Amathematical Operation not known"""
    def __init__(self, operator: str, equation: str = ""):
        self.errorName = "notAmathematicalOperationException"
        self.errorMessage = operator + " is not a known operator"
        self.equation = equation
    def getName(self):
        return self.errorName
    def getMessage(self):
        return self.errorMessage
    def getEquation(self):
        return self.equation

class AmathematicalException(Error):
    """exception - Amathematical"""
    def __init__(self, message: str, equation: str = ""):
        self.errorName = "AmathematicalException"
        self.errorMessage = message
        self.equation = equation
    def getName(self):
        return self.errorName
    def getMessage(self):
        return self.errorMessage
    def getEquation(self):
        return self.equation

class missingOperator(Error):
    """exception -  missing operator in a certain place of the code"""
    def __init__(self, operator: str, equation: str = ""):
        self.errorName = "missingOperatorException"
        self.errorMessage = operator + " is missing from the equation"
        self.equation = equation
    def getName(self):
        return self.errorName
    def getMessage(self):
        return self.errorMessage
    def getEquation(self):
        return self.equation

class missingNumber(Error):
    """exception -  missing number in a certain place of the code"""
    def __init__(self, operator: str, equation: str = ""):
        self.errorName = "missingNumberException"
        self.errorMessage = "A number is missing near the " + operator
        self.equation = equation
    def getName(self):
        return self.errorName
    def getMessage(self):
        return self.errorMessage
    def getEquation(self):
        return self.equation