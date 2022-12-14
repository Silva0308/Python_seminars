# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.
from math import sqrt
def sqr_root(a,b,c,):
    d = b**2-4*a*c
    if a ==0:
       return print("error")
    with open("sqr_root.txt","a", encoding="utf-8") as my_f:    
        my_f.write(f"{a}x² + ({b})x +({c}) = 0\n")
        if d < 0:
            my_f.write("Уравнение не имеет корней\n")
        elif d == 0:
            my_f.write(f'{-b/(2*a)}\n')
        else:
            my_f.write(f'{(-b - sqrt(d)) / (2 * a)}\n')
            my_f.write(f'{(-b + sqrt(d)) / (2 * a)}\n')
for i in range(3):
    sqr_root(int(input("a= ")),int(input("b= ")), int(input("c= ")))