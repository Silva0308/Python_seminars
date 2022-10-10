# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
from random import randint
n = int(input("Введите количество чисел: "))
if n<=0:
    print("не может быть такой последовательности")
else:
    my_list = [randint(0, 10) for x in range(n)]
    print (my_list)
    new_list = []
    [new_list.append(i) for i in my_list if i not in new_list]
    print(f"Список из неповторяющихся элементов: {new_list}")