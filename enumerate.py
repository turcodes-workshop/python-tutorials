
softwareLangs = ["Python", "C#", "Dart"]

index = 0

for i in softwareLangs:
    print(i)


enms = enumerate(softwareLangs);

print(type(enms))
for i in enms:
    print(i)

for index,value in enumerate(softwareLangs,0):
    print(index, value)