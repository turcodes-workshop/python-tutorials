
#value types => string, number
number = 10
number2 = 20

number = number2
number2 = 30

print(number, number2)

#reference types => lists

x = ["Python", "Javascript"]
y = ["java","Js"]
x = y.copy()

y[0] = "c#"
print(x, y)