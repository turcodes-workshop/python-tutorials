
# for item in range(100):
#     if(item<10):
#         print("testtestest")


numbers = [1,3,7,12,22,34]
result = []

for number in numbers:
    if(number%2 == 0):
        result.append(number)


result = [num for num in numbers if num % 3 == 0] #use if
result = [num if num%2 == 1 else "even num" for num in numbers] #use if-else
print(result)   