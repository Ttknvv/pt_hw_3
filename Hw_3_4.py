num = 136
list = []
list1 = []
while num != 0:
    list.append(int(num%2))
    num = int(num/2)
for i in list[::-1]:
    list1.append(i)

print(list1)

