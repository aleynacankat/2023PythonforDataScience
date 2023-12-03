num = 100

print(type(num))

num2 =99.99

print(type(num2))

print(round(2.1)) # 2
print(round(5.9)) # 6
print(abs(-34)) # 34

name4 = 'Hello! \"Rockstar Programmer"'

print(name4)

first_name = 'Aleyna'
last_name = 'Cankat'
welcome_message = f'Welcome{first_name} {last_name}'

print(welcome_message)

language = 'python'

print(language[::-2])

deneme = 'javascript is awesome'

print(len(deneme))

new_quote = deneme.replace('javascript', 'python')
print(new_quote)

is_cool = True
is_dirty = False

print(10>9)

favorite_languages = ['javascript', 'python', 'typescript']
shopping_cart_items = ['football', 123, True]

first_item = shopping_cart_items[0]
print(first_item)
soccer_stars = ['ronaldo', 'messi','ibrahimovic','zidane','beckham']

clone = soccer_stars[:] # copies the list. Commonly used in Python
reverse_order = soccer_stars[::-1] # reverses the order of data
print(reverse_order) # ['beckham', 'zidane', 'ibrahimovic', 'messi', 'suarez']

scores = [44,48,55,89,34]

scores.append(100)

print(scores)

scores.extend([23])
print(scores)

alphabets = ['a', 'b', 'c']
print(alphabets.index('a'))

numbers = [1,4,6,3,2]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers_clone = numbers.copy()
print(numbers_clone)

avengers = ['ironman', 'spiderman', 'antman', 'hulk']

matrix1 = [[1,2,3],[1,3,5],[2,3,4]]

first_item1 = matrix1[0]

print(first_item1)

range_of_numbers = list(range(10))

print(range_of_numbers)

first, second, third = ['tesla', 'ford', 'ferrari']
print(first)

a,*others = [1,2,3,4,5]
print(a)
print(others)

first, *others, last = [1,2,3,4,5]

print(first)
print(others)
print(last)

##Dictionaries

user = {'name': 'Max', 'age':40, 'married':False}

print(user['name'])
print(user['married'])

#keys are immutable data type

abstract = {
    'first': 123,
    True: 'hello',
    777: [1,2,3,4,5]
}

print(abstract['first'])

house = {
    'rooms': 4,
    'occupants':2,
    'doors':6
}

user = {'name': 'Raghav', 'age': 20, 'country': 'India'}

print('name' in user.keys()) #True
print('Raghav' in user.values()) #True

cat = {
    'name':'Tom',
    'greet':'meow'
}

cat_copy = cat.copy()
print(cat_copy)

cat.pop('name')

#Tuples

my_tuple = (1,2,3)
print(my_tuple[1])
print(1 in my_tuple)

colors = ('red', 'orange', 'blue', 'yellow')
new_colors = colors[1:4]
print(new_colors)

color_1,*others = colors
print(color_1)
print(others)

print(len(colors))
print(colors.count('orange'))
print(colors.index('orange'))

set_of_numbers = {1,2,3,4,5,5} # {1,2,3,4,5}
print(set_of_numbers)
emails = ['samantha@hey.com', 'rock@hey.com', 'samantha@hey.com']

emails_set = set(emails)
unique_emails = list(emails_set)

print(unique_emails)
