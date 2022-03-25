
list = [1, 2 , 36,15,25,69,15,123,12345,4852]

dictionaries = {
    "key": 123,
    "key1": {
        "tt": "sadfas"
    }
}

test = dictionaries

print(type(test))
print(test is dictionaries)
print(type(dictionaries))
print(dictionaries["key1"]["tt"])
