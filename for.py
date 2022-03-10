
numbers = [1,3,5,6,7,9,10]
numbers.sort(reverse=True)

for i in numbers:
    print(i)

for i in numbers:
    print("Hello")


names = ["hasan", "barış", "mert", "deniz"]
for name in names:
    print(name)

for name in names:
    for n in name:
        print(n)

_tuple = [(1,2),(3,4),(1,5)]
for t,y in _tuple:
    print(t,y)

cities = {"01": "Ankara", "02": "Adıyaman","03": "Afyon", "04": "Ağrı"}
for c in cities:
    print(c) #01,02,03,04

for c in cities:
    print(cities[c]) #Ankara,Adıyaman,Afyon

for c in cities.values():
    print(c) # Ankara,Adıyaman,Afyon

for key,value in cities.items():
    print(key,value) # 01 Ankara, 02 Adıyaman ...