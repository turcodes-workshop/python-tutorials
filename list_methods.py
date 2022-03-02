numbers = [1,3,9,45,14,27,36,3,3]
chars = ["a","b","f","k","s","v","s"]
result = min(numbers)
result = max(numbers)

result = min(chars)
result = max(chars)

#add
numbers.append(323)
chars.append("da")
numbers.insert(3,12)
chars.insert(2,"c")


#delete
numbers.pop() # .. listedeki son değeri siler
chars.pop()
numbers.remove(36)
chars.remove("a")


#sorting
numbers.sort()
chars.sort()
numbers.sort(reverse=True)
numbers.reverse()
print(numbers.count(3))
print(chars.count("s"))


numbers.clear()
deneme = chars
chars.clear()
print(deneme)
