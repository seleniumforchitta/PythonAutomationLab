# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

dict1 = {1:'Ashok', 2:'Ram', 3:'Hari', 4:'Gopal'}
print(dict1)
print(dict1.keys())
print(dict1.values())
list1 = list(dict1.values())
print(list1)

dict1[5] = 'Ramsen'
print(dict1)

del dict1[4]
print(dict1)

# Change Dictionary Items
dict1[5] = 'Tamsen'
print(dict1)

for val in dict1:
    print(val, end=",")
    print(dict1[val])

dict1.pop(1)
print(dict1) # {2: 'Ram', 3: 'Hari', 5: 'Tamsen'}

new_dict = {1:'Kuch Bhi', 2:'Changed'}
dict1.update(new_dict)
print(dict1) # {2: 'Changed', 3: 'Hari', 5: 'Tamsen', 1: 'Kuch Bhi'}

