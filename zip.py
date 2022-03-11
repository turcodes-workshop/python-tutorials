

list1 = [1,2,3,4,5]
list2 = ["bir","iki","üç","dört","beş"]
list3 = ["a","b","c","d","e"]
"""list1.append(list2)
print(list1)"""
zip1 = zip(list1,list2,list3)
print(type(zip1))
print(zip1)

for i in zip1:
    print(i)

for x,y,z in zip(list1,list2,list3):
    print(x,z,y)