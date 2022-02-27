
name = "Hasan"
surname = "Türkmen"
age = 26
txt = "Benim adım " + name + " ve soyadım " + surname + ". Yaşım ise " + str(age) + "."
print(txt)

print(txt[0]) # B
print(txt[1]) # e
print(txt[-1]) # .

print(txt[0:5]) # Benim

print(txt[6:16]) #adım Hasan .. iki index arasında ki karakterleri alır.
print(txt[:5]) # Benim .. 0 dan belirtilen index e kadar alır.
print(txt[10:]) # Hasan ve soyadım Türkmen. Yaşım ise 26. ... 10. indexten başlar sona kadar alır.

print(txt[0:30:3]) # Biamaneod ... 0.indexten 30.indexe kadar 3..3 ilerler.
print(txt[::2]) #Bnmaı aa esydmTrmn aı s 6 ... başlangıçtan sona kadar 2..2 ilerler.