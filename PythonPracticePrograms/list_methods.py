fruits = ['apple', 'banana', 'orange']
new = ['mango','berry']
fruits.append('kiwi')
fruits.remove('orange')
fruits.insert(1,'grapes')
fruits.extend(new)
fruits[1]="New Value"
print(fruits)
print(len(fruits))
# del fruits[1:3]
# print(fruits)
# print(len(fruits))
print(fruits.pop(1))
print(fruits)
print(fruits.index('mango'))
print(fruits.count('banana'))

print(fruits.reverse())
new_fruits = fruits.copy()
print(new_fruits)

# list() method is used convert a string into list
test = 'Automation'
print(list(test)) # ['A', 'u', 't', 'o', 'm', 'a', 't', 'i', 'o', 'n']

# ['apple', 'New Value', 'banana', 'kiwi', 'mango', 'berry']
# 6
# New Value
# ['apple', 'banana', 'kiwi', 'mango', 'berry']
# 3
# 1
# None
# ['berry', 'mango', 'kiwi', 'banana', 'apple']
# ['A', 'u', 't', 'o', 'm', 'a', 't', 'i', 'o', 'n']