# 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
n = int(input("Введите число, ограничивающее диапазон: "))
pos_1 = int(input("Введите позицию первого множителя: "))
pos_2 = int(input("Введите позицию второго множителя: "))
new_list=[]
if n>0:
    for x in range(-n,n+1):
        new_list.append(x)
else:
    for x in range(-n,n-1, -1):
        new_list.append(x)
print(new_list)
if 0 < pos_1 <= len(new_list) and 0 < pos_2 <= len(new_list):
    print(new_list[pos_1-1]*new_list[pos_2-1])
else:
    print("Таких элементов в массиве нет")
