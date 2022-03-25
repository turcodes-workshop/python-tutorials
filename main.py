from tkinter import N
import constant

"""
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm1')

def kare_Al(number):
    return number * 2


print(kare_Al(12))
"""

result = constant.pi_multiplication(5.15)
print(f"{result:06.2f}") #06 -> kaç basamaklı olduğunu belirtir '.' dahildir.  2f ise . dan sonra kaç basamak olacak.



a = 0b1010 #Binary Literals


b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

print(type(a))
#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j
# print(a)
# print(a, b, c, d)
# print(float_1, float_2)
# print(x, x.imag, x.real)
