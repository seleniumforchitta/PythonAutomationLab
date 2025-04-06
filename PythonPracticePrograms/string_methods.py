print("Oython String")

str = "Automation"
print(str.upper())
print(str.lower())
str1 = "Python is fun"
tup = str1.partition('is ') # Partition returns a tuple
# Partition takes a string parameter separator as an argument that separates the string at first occurance of it 
print(tup)
lis = str1.split( ) # split returns a list
print(lis)

song = 'Let it be, let it be, let it be, let it be'
print(song.replace('let', 'Don\'t let', 2)) # it will replace 1st 2 occurance of the string

print(song.find('let')) # if string doesn't exist find() returns -1
print(song.index('let')) # if string doesn't exist index() throws value error

