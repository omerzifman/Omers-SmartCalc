def show(massage: str):
    print(massage)

def get(massage: str) -> str:
    try:
        return input(massage)
    except EOFError: #if the input is ^Z
        show("input not valid")
        return None
    except KeyboardInterrupt: #if the input is ^C
        show("input not valid")
        return None

def showError(err: Exception):
    print("---------Error!---------")
    print("//"+ err.getName())
    print(err.getMessage())
    print(err.getEquation())