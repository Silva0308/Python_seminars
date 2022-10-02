# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

n = int(input("Введите n: "))
new_list=[]
for i in range(1,n+1):
    new_list.append(3*i+1)
print(new_list)