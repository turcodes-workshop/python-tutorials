list1 = [1,3,5,13]
thistuple = (1,2,"altı",False,"qas")
thistuple2 = (1,4,"beş",True,"qas")

print(type(list1))
print(type(thistuple))


print(list1[0])
print(thistuple[2])

print(len(list1))
print(len(thistuple))

list1[0] = 2
# thistuple[0] = 2

list1.append(45)

print(list1)
print(thistuple)

print(list1.count(3))
print(thistuple.count(2))
sumtuple = thistuple + thistuple2
print(sumtuple)
print(sumtuple.count(1))


list2 = tuple([6,8,3,12])

print(type(list2))
print(list2)