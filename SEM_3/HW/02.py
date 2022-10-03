# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint


def list_fill(n):
    array1 = [randint(0, 10) for x in range(n)]
    print(array1)
    return array1


def pair_mult(array):
    l = len(array)
    for i in range(l//2):
        print(array[i]*array[l-1-i], end=" ")
    if l % 2 != 0:
        print(array[l//2])


my_list = list_fill(int(input()))
pair_mult(my_list)
