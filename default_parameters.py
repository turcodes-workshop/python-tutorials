
# def hi(name:str, message: str =""):
#     print(f"{name}: {message}")

# hi("hasan","selam gencolar.")
# hi("mehmet")


# def exponentiation(base:int, ex:int):
#     return base ** ex

# calc = exponentiation(1123,212)
# print(calc)



def addition(a:int, b:int):
    return a+b

def subtraction(a:int, b:int):
    return a-b

def multiplication(a:int, b:int):
    return a*b

def division(a:int, b:int):
    return a/b

def mathProc(a:int,b:int, c):
    return c(a,b)

result = mathProc(1,3,subtraction)
print(result)