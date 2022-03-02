audiCar = {
    "brand" : "Audi",
    "model": "A5",
    "year": 2019
}

# get values
result = audiCar["brand"]
result = audiCar.get("brand")


# query
result = "brand" in audiCar
result = len(audiCar)

# add
audiCar["color"] = "Black"

#del
"""audiCar.pop("year")
audiCar.popitem()
del audiCar["brand"]
# del audiCar ...komple silinir
audiCar.clear()"""

# object copy
car = audiCar.copy()

#update
audiCar.update({
    "brand": "BMW",
    "model": "520d"
})

print(audiCar)