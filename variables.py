# 7000 + %18

"""
print(7000)
print(7000 * 0.18);
print(7000 + 7000 * .18);
print(7000 + 7000 * .18);
"""

tax = 0.25
def calculateTaxWithProductPrice(productPrice: float):
    price = productPrice + productPrice * tax;
    return price

product1 = 712100
product2 = 8212
isStudent = True


print(calculateTaxWithProductPrice(product1))
print(calculateTaxWithProductPrice(product2))

a,b,name,issss = 10,23,"test",False;
print(a,b,name,issss)