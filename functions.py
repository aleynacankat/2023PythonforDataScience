
myName = "Aleyna"

myName.upper()

def helloPython():
    print("hello")
    print("python")

print(helloPython())

def helloName(name):
    print("hello")
    print(name)

print("python")

#return:

def summation(num1,num2,num3):
    print(num1+num2+num3)

def returnSummation(num1,num2,num3):
    return num1+num2+num3 #deger dondurur

x = returnSummation(10,2,8)

print(x)

def controlString(s):
    if s[0] == "a":
        print("a")

print(controlString("aan"))

#args, kwargs

def argsSum(*args):
    return sum(args)

def kwargsExample(**kwargs):
    print(kwargs)

kwargsExample(apple = 100, banana=150,melon=200)

def kwargsExample3(**kwargs):
    if "apple" in kwargs:
        print("appleee")
    else:
        print(":(")