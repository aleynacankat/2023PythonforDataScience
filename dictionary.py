#key value pairing

fruitList =["banana", "apple"]

calorieList = [100,150]

print(fruitList[0])

fitnessDictionary = {"banana": 100, "apple":150}

print(type(fitnessDictionary))

print(fitnessDictionary["banana"])

print(fitnessDictionary.keys())

print(list(fitnessDictionary.values()))

fitnessDictionary["kavun"]=300
print(fitnessDictionary)

print(fitnessDictionary.get)

print(fitnessDictionary.get("appl",0)) #eger yoksa 0 yazdir

myDictionary = {100:"a", 200:"b", 300:"c"}
myDictionary[100]

myMixedDict = {"key1":100, "key2":3.14, "key3":["10,20,30"]}

print(myMixedDict["key3"][1])

lastDict = {"k1":10, "k2": [10,20,30,40,50],"k3":"string", "k4":{"a":100, "b":200}}
print(lastDict["k2"][2])