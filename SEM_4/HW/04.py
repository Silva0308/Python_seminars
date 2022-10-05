#4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
from random import randint
from random import choice
def Poly(k):   
    result =''
    my_list =[randint(0, 10) for x in range(k)]
    znak=['-','+']
    i =0
    while k>1:
        if my_list[i] != 0:
            result+=(f'{my_list[i]}*x^{randint(2, k)}{choice(znak)}')
            k-=1
            i+=1
        else:
            i+=1
    if my_list[-1] !=0:
        result+=(f"{my_list[-1]}=0")
    else:
        result+=(f"{randint(1, k)}=0")
    with open("poly_1.txt","a", encoding="utf-8") as my_f:
        my_f.write(f'{result}\n')

k =int(input('введите натуральное число: '))
if k<=0:
    print("это число не натуральное")
else:
    Poly(k)
        