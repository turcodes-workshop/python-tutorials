
def parseInt(number):
    try:
        return int(number)
    except ValueError:
        #Value error logla
        return 0


"""
# sample1
number = input("Sayı Giriniz: ")
number = parseInt(number)
if (number > 0):
    if(number % 2 == 1):
        print("Number is even and odd")
    else:
        print("Number is even but not odd")
else:
    print("Number is negative")
"""

"""
# sample2
x = input("x : ")
y = input("y : ")
z = input("z : ")

x = parseInt(x)
y = parseInt(y)
z = parseInt(z)

if(x > y and x>z):
    print("x is greater than all numbers")
elif (y>x and y>z):
    print("y is greater than all numbers")
elif (z > x and z > y):
    print("z is greater than all numbers")
"""

# sample3
name = input("name :")
age = input("age :")
age = parseInt(age)
education = input("education : ")

if (age >= 18):
    if(education =="highschool" or education == "university"):
        print("You can get a driver's licence")
    else:
        print(f"{name} can't get a driver's licence because of insufficient education")
else:
    print(f"{name} can't get a driver's license because of insufficient age")

