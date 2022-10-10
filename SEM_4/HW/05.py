#5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
import pathlib
from pathlib import Path

path1 = Path("Python_seminars", "SEM_4", "poly_1.txt")
with open(path1, "r") as file1:
    lines1=file1.readlines()
for i in range(len(lines1)):
    lines1[i] = lines1[i][:-4]
path2 = Path("Python_seminars", "SEM_4", "poly_2.txt")
with open(path2, "r") as file2:
    lines2=file2.readlines()
path3 =  Path("Python_seminars", "SEM_4", "poly_sum.txt") 
with open(path3,"a", encoding="utf-8") as my_f:
    if len(lines1)==len(lines2):
        for i in range(len(lines1)):
            my_f.write(f'{lines1[i]}{lines2[i]}')
    else:
        my_f.write("файлы не совпадают по размеру")
