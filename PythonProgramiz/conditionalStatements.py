num = 3.4
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")


num = [3, 4, 5, 6, 7, 8, 9]
sum = 0
for i in num:
    sum = sum + i
print("The sum is = ", sum)

sum = 0
for i in range(len(num)):
    sum = sum + num[i]
print("The sum is = ", sum)

n = 100
sum = 0
while n>0:
    sum = sum+n
    n=n-1
print("The sum is =", sum)

