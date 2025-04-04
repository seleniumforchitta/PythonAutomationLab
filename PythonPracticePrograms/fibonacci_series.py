def fibnacci(n):
    li = []
    i = 0
    j = 1
    while(i<n):
        li.append(i)
        temp = i
        i = j
        j = temp+j
        
        
    return li

print(fibnacci(22))


def fibo(n):
    mi = []
    a, b = 0, 1
    while a<n:
        mi.append(a)
        a, b = b, a+b
    return mi

print(fibo(100))