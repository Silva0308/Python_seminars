# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input("Введите n: "))
a=1
for i in range(1,n+1):
    print(a, end=" ")
    a*= i+1
   
