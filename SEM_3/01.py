# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
from random import sample
from xxlimited import new
def list_search (n,x):
    if n<0:
        return "eror"
    new_list= sample(range (1, n*2,), n)
    print(new_list)
    if x in new_list:
        return "yes"
    return "No"

print(list_search(int(input()),int(input())))