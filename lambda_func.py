
"""def exponentiation(base:int):
    return base **2

print(exponentiation(521))"""

#lambda arguments : expression

"""result = (lambda a: a ** 2)(3)
print(result)"""


exponentiation = lambda a: a ** 2

result = exponentiation(2)

addition = lambda a,b,c: a+b+c
result = addition(1,3,123)

print(result)