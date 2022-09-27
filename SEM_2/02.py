#1. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# n = int(input("Введите n: "))
# a=1
# for i in range(n):
#     print(a, end=" ")
#     a*=-3
    

n = int(input("Введите n: "))
for i in range(n):
    print((-3)**i, end=" ")