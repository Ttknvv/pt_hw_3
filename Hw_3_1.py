#Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list1 = [1, 3, 2, 5, 6, 2]
sum = 0
for i in range(0, len(list1)):
    print(i)
    if i%2 != 0:
        sum = sum + list1[i]

print(sum)