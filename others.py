
# identity operator : is   -- ref type pointer sorgulama

x = y = [1,2,3,4]
z = [1,2,3,4]

result = (x == y)
result = (x == z)
result = (x is z)
result = (x is y)


# membership operator : in

a = ["python","javascript"]
result = "python" in a

email = "deneme@gmail.com"
result = "@" in email


print(result)
