a = [3, 2, 4, 3, 6 ,7]
for i in a:
    print(i, "=", i**2)

a=[]
for b in range(1,100):
    if b%2!=0:
        a.append(b)
print(a)

it = 10
while it>-10:
    if it%2 == 0:
        print(it)
    it = it-1
    

it = 4
while it>0:
    if it == 3:
        print(it)
        break
    it = it-1

it = 4
while it>0:
    if it == 3:
        it = it-1
        continue
    print(it)
    it = it-1

    
    