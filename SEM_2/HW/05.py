# 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
n = int(input("Введите n: "))
from random import randint
array1 = [randint(-n, n) for x in range(n)]
print(array1)
for i in range(len(array1)):
    j = randint(0, i + 1)
    array1[i], array1[j]=array1[j], array1[i]
print(array1)