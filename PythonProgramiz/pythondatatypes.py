# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
list1 = [2,3,4,5,6,7,8] 
tup1 = (3,2,1,2,2) # immutable
set1 = {3,3,4,5,6} # can't have duplicate
dict1 = {1:"Hellow", 3:45, "Hi":23}
print(list1)
print(tup1)
print(set1)
print(dict1)

list2 = [2,2,4,4,6,7,8] 
tup2 = tuple(list2) 
set2 = set(list2) 
dict2 = dict([[2,"Hi"],["key","Pair"],[3,4]])
print(list2)
print(tup2)
print(set2)
print(dict2)

a = 123
b = '456'
print(a+int(b))

name = input("Enter you name: ")
print(name)

print(id(a))
