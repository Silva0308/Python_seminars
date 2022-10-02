# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
num = int(input("Задайте число: "))
list_num=[0]
fib1 = 1
fib2 = 0
for i in range(num):
    fib1, fib2 = fib2, fib1 + fib2
    list_num.append(fib2)
    list_num.insert(0,((-1) **(i) * fib2))
print(list_num)
