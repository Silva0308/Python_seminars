# 4. Напишите программу, которая принимает на вход дробь и выводит первую цифру дробной части
n =float(input('Введите число'))
a=int(n*10%10)
if a!=0:
    print (a)
else:
    print('no')