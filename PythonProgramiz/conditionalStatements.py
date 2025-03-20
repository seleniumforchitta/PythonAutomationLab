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
while n>1:
    n=n-1
    if n%10==0:
        continue
    sum = sum+n
print("The sum is =", sum)

# while with else 
counter = 0
while counter<3:
    print("inside loop")
    counter = counter+1
else:
    print("inside else")
    
