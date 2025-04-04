def sum_greater_than(numbers, n):
    sum=0
    for i in numbers:
        if i>n:
            sum=sum+i
    return sum
            




list1 = [23, 43, 56, 54, 67, 89, 87]
print(sum_greater_than(list1, 75))