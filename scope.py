
# a = "global value"

# def fn1():
#     a = "locale value"
#     print(a)

# fn1()
# print(a)


"""
city = "İstanbul"
def changeCity(newCity):
    city = newCity
    print(city)

changeCity("Test")
print(city)

"""

#----------
"""city = "İstanbul"
def outher_func():
    city = "İzmir"
    def inline_func():
        city = "Ankara"
        print("inline func called: "+city)
    
    inline_func()
    print(city)

outher_func()"""


"""a = 10
def fn2():
    a = 20
    print(f"changed a to {a}")

fn2()
print(a)

"""

#global keyword

city = "İstanbul"
def changeCity(newCity):
    global city
    city = newCity
    print(city)

changeCity("Test")
print(city)

