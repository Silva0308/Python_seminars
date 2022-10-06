#4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
from random import randint
from random import choice
import pathlib
from pathlib import Path
def Poly(k):   
    my_list =[randint(0, 10) for x in range(k)]
    znak=['-','+']
    i =0
    path1 = Path("Python_seminars", "SEM_4", "poly_1.txt")
    with open(path1,"a", encoding="utf-8") as my_f:
        while k>1:
            if my_list[i] != 0:
                my_f.write(f'{my_list[i]}*x^{randint(2, k)}{choice(znak)}')
                k-=1
                i+=1
            else:
                i+=1
        if my_list[-1] !=0:
                my_f.write(f"{my_list[-1]}=0\n")
        else:
                my_f.write(f"{randint(1, k)}=0\n")
   
k =int(input('введите натуральное число: '))
if k<=0:
    print("это число не натуральное")
else:
    Poly(k)
        