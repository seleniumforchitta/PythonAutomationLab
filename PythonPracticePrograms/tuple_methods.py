# A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created.
numbers = (1, 2, -5, 6, 3, -2)
print(numbers)

for i in numbers:
    print(i)

cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# cars[0] = 'Nissan' - Not Possible
print(cars)
print(len(cars))

for car in cars:
    print(car)

print(3 in numbers) # True
print(-3 in numbers) # False

print(numbers.index(2))








