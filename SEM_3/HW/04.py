# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
n=int(input("Введите размер массива: "))
my_list=[round(random.uniform(0, 100), 3) for x in range(n)]
print(my_list)
new_list=[round(i%1,3) for i in my_list if i%1 != 0]
print(new_list)
print(max(new_list) - min(new_list))