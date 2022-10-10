# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def fact(n):
    i = 2
    if n==1:
         result=1
    else:
        result=[]
    while i*i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i+=1
    if n>1:
        result.append(n)
    return result

N = int(input("введите натуральное число: "))
if N<1:
    print("Это не натуральное число")
else:
    print(fact(N))