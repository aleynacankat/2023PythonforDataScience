myString = "aleyna"

for c in myString:
    print(c)

myTuple = (10,20,30,40,50)

for num in myTuple:
    print(num/5*2)

myNewList = [("a","b"),("c","d"),("e,f")]

for element in myNewList:
    print(element)

#tuple unpacking

myDictionary = {"k1":100, "k2": 200, "k3": 300}

for element in myDictionary:
    print(element)

for (key, value) in myDictionary.items():
    print(value)

#continue break pass : donguden cikarir

AList = [10,20,30,40,50]

print("for loop started")
for num in AList:
    print(num)
print("for loop ended")

for number in AList:
    if number == 40:
        print("yes")
        break

for number in AList:
    print(number)
    if number == 40:
        print("yes")
        continue

for num in AList:
    pass

#while

x = 0

while x < 10:
    print(x)
    x = x + 1

lastList = [10,20,30,40,50]

while 20 in lastList:
    print("20 in lastList")
    lastList.remove(20)
name = "Aleyna"
print(f"welcome {name}") #print("welcome",name)

p = 0
while p < 20:
    print(f"value of p: {p}")
    p += 1