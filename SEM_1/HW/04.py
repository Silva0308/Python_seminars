# 4. Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).
quarter= int(input("Введите номер чертверти: "))
if quarter <1 or quarter >4:
    print("Вы ввели неправильный номер")
elif quarter ==1:
    print ("x>0, y >0")
elif quarter ==2:
    print ("x<0, y >0")
elif quarter ==3:
    print ("x<0, y <0")
else:
    print ("x>0, y <0")