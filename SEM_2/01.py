#1. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов

n = int(input("Введите n: "))
from random import randint
array1 = [randint(0, 10) for x in range(n)]
print(array1)