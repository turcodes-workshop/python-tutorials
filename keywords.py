from cgitb import reset


def fullName(firstName:str, lastName:str):
    return f"Welcome to system, {firstName} {lastName}"

result = fullName(lastName="türkmen", firstName="hasan")
print(result)