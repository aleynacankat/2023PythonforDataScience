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