# 34 => İstanbul
# 35 => İzmir
"""
#list
cities = ["İstanbul", "İzmir"]
plates = [34, 35]


#dictionary
plates = { "İzmir": 35, "İstanbul": 34}
print(plates["İzmir"])
print(type(plates))

plates["Eskişehir"] = 26
plates["Bursa"] = 16
print(plates)

"""
products = {
    100: {
        "productName" : "Monitör",
        "productDescription": "16 inç",
        "guarenteePeriod" :3,
        "price": [800, 944]
    },
    101: {
        "productName" : "SSD",
        "productDescription": "256 GB",
        "guarenteePeriod" :2,
        "price": [1500,1770]
    }
}
print(products)
print(type(products))

result = products[100]["productName"]
total = products[100]["price"][1] + products[101]["price"][1]
print(result)
print(total)