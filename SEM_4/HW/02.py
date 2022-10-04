# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def fact(n):
    i = 2
    if n<0:
        n*= -1
        result = [-1]
    elif n==0:
        result = 0
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

print(fact(int(input("введите число: "))))