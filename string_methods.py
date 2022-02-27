text = "My name is Hasan Türkmen. I'm live in Istanbul."

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.islower())
print(text.isalnum())
print(text.isascii())
print(text.istitle())

print(text.strip())
print(text.split('.'))
print("-".join(text))

print(text.index("Hasan"))
print(text.startswith("M"))
print(text.endswith("."))
print(text.replace("Istanbul", "Bursa"))

print(text.count("M"))
print(len(text))
print(len("12"))