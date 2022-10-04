# 1. Вычислить число c заданной точностью d

from decimal import Decimal
n = Decimal(input('введите число: '))
d = str(input('введите точность округления в формате 1.000: '))
print(n.quantize(Decimal(d)))



