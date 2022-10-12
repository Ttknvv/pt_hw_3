#Задайте список из вещественных чисел.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in list1:
    list2.append(round(i%1, 3))
min = list2[0]
max = list2[0]

for i in range(0, len(list2)):
    if list2[i] > max:
        max = list2[i]
    elif list2[i] != 0 and list2[i] < min:
        min = list2[i]

print(max - min)