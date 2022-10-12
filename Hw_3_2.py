#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
lenList = len(list1)
for i in range(0, int(lenList/2)):
    list2.append(list1[i] * list1[lenList - i - 1])

if len(list1)%2 != 0:
    list2.append(list1[int(lenList/2)]**2)

print(list2)