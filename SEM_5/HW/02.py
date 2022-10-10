# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from pathlib import Path


def code(text: str):
    coded_text = [1, text[0]]
    for elem in text[1:]:
        if elem != coded_text[-1]:
            coded_text += [1, elem, ]
        else:
            coded_text[-2] += 1
    return ''.join(map(str, coded_text))


def deco(coded_text: str):
    decoded_text = ''
    for i in range(0, len(coded_text), 2):
        decoded_text += str(coded_text[i+1])*int(coded_text[i])
    return decoded_text


path1 = Path("Python_seminars", "SEM_5", "origin.txt")
with open(path1, "r") as my_f1:
    my_text = ''.join(map(str, my_f1.readlines()))
coded_str = code(my_text)
path2 = Path("Python_seminars", "SEM_5", "coded.txt")
with open(path2, "w", encoding="utf-8") as my_f2:
    my_f2.write(coded_str)
with open(path2, "r") as my_f2:
    coded_text = ''.join(map(str, my_f2.readlines()))
decoded_text = deco(coded_text)
path3 = Path("Python_seminars", "SEM_5", "decoded.txt")
with open(path3, "w", encoding="utf-8") as my_f3:
    my_f3.write(decoded_text)
