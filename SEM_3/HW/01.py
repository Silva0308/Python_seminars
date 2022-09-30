# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import randint
def list_fill(n):
    array1 = [randint(0, 10) for x in range(n)]
    print(array1)
    return array1


def list_sum(array):
    sum = 0
    for i in range(0, len(array), 2):
        sum += array[i]
    print(sum)


my_list = list_fill(int(input()))
list_sum(my_list)
