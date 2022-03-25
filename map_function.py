
numbers =  [1,3,5,8,12]
squares = []


def func_scuare(num):
    """docs...."""
    return num **2

result = list(map(func_scuare, numbers))

result = list(map(lambda num: num **2, numbers))

print(result)


print(func_scuare.__annotations__)
print(func_scuare.__name__)
print(func_scuare.__doc__)


print(open.__doc__)