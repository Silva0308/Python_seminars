# 1. Вычислить число c заданной точностью d

from decimal import Decimal
n = Decimal(input('введите число: '))
d = input('введите точность округления в формате 0.0001: ')
print(n.quantize(Decimal(d)))



