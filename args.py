
# def addition(a,b):
#     return a+b

# def additions(numbers):
#     result = 0
#     for num in numbers:
#         result+=num
#     return result

# numbers = [5,15,20,25]

# result = additions(numbers= numbers)
# print(result) 


def addition(*args):
    result = 0
    for i in args:
        result+=i
    return result

result = addition(1,36,45,5,4896,123,5189)
print(result)