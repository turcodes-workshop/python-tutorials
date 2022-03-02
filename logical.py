
# and operators

x = 15
#result = 10 < x < 20

#and operators
result = (x > 10) and (x < 20)

note = 90
absenteeism = 4
result = (note >= 50) and (absenteeism < 10)

# or operators
result = (x<10) or (x%3 == 0)

# Not operators
result = not(x < 0)

penal = False
result = (note >= 85) and (absenteeism < 10) and not(penal)
print(result)

