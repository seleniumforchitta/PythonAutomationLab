str = "Automation Test Lead"
print(str[-1::-1])

str1 = str.split(' ')
fin = ""
for i in str1[-1::-1]:
    fin = fin+i
    fin = fin+" "

print(fin)

