# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
n = int(input("Введите число: "))
if n>0:
    for i in range(-n,n+1):
        print(i,end=' ')
else:
    for i in range(-n,n-1, -1):
        print(i,end=' ')