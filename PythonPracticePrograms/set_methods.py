# Set is a collection of unique data. So we can't include deuplicate elements inside set

id = {1, 2, 3, 4, 43, 456, 'test', "test"}
print(id) # o/p - {1, 2, 3, 4, 'test', 456, 43} - if you put a duplicate it will not throw error rather it will just exclude that element. and order will also be random everytime you run because - set has no particular order.

id1 = {} # it will create an empty directory as the syntax is same for set & directory
id2 = set() # it will create an empty set

id.add(32)
print(id) # {32, 1, 2, 3, 4, 456, 'test', 43}
id.add(2) # already the element is there so no change
print(id) # {32, 1, 2, 3, 4, 456, 43, 'test'}

# like extend in list - we can use update()
list1 = [3, 4, 5, 6, 7, 8]
id.update(list1)
print(id) # {1, 2, 3, 4, 5, 6, 7, 456, 8, 32, 43, 'test'}


id.discard('test') # removes an element from the set
print(id) # {1, 2, 3, 4, 5, 6, 7, 456, 8, 32, 43}
id.pop() # randomly removes an item
print('pop',id)
id.remove(456) # remove vs discard - both the removes specified element but remove throws error if the element doesn't exist
print(id)


print(max(id)) # if there are multiple data type then it will throw an error
print(min(id))

print(sorted(id)) # [1, 2, 3, 4, 5, 6, 7, 8, 32, 43, 456] - covert the set to list
print(sum(id))

# first set
A = {1, 3, 5}

# second set
B = {0, 1, 2, 4}
print(A | B)
print(A.union(B))
print(A & B)
print(A.intersection(B))
print(A - B)
print(A.difference(B))
print(A ^ B)
print(A.symmetric_difference(B))

