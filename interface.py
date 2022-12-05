def show(massage: str):
    print(massage)

def get(massage: str) -> str:
    return input(massage)

def showError(err: Exception):
    print("---------Error!---------")
    print("//"+ err.getName())
    print(err.getMessage())