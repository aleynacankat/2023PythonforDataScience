#unique elements, unordered

myList = [10,20,30,40,50,10,20]

print(len(myList))

mySet = set(myList)

print(mySet)

mySet1 = {10,20,30,40,10,20,40}

print(mySet1)

mySet2 = {30,40,50,60,70,80}

mySet.union(mySet2)

print(mySet)

mySet.intersection(mySet2)
print(mySet)

countryList = ["de", "fr","tr","de","nl"]

emptyList = []

emptyList.append(10)
emptyList.append(20)
emptyList.append(30)

print(emptyList)

emptySet = {}
emptySet = set()

print(type(emptySet))

type(emptySet)

emptySet.add(10)
emptySet.add(10)
emptySet.add(10)
emptySet.add(10)
emptySet.add(10)
print(emptySet)

emptyList = list()

emptyList.append(10)
emptyList.append(20)
emptyList.append(30)

print(emptyList)

emptyDictionary = dict()
emptyDictionary["a"] = 10
emptyDictionary["b"] = 20

print(emptyDictionary)
