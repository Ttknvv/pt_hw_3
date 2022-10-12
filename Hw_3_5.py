num = 8

list = [0, 1]
list1 = [0, 1]
list2 = []
for i in range(2, num + 1):
    list.append(list[i-2] + list[i-1])

for i in range(2, num + 1):
    list1.append((-1) ** (i+1) * (list[i-2] + list[i-1]))

for i in list1[::-1]:
    list2.append(i)

for i in list:
    list2.append(i)

print(list2)