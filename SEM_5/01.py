# Создайте список из N натуральных чисел. Среди чисел не хватает одного, чтобы выполнялось условие A[i]-1=A[i-1]. Найдите его
from random import choice


def new_list(n):
    n_list = [x for x in range(n+1)]
    n_list.remove(choice(n_list))
    print(n_list)
    return (n_list)


my_list = new_list(int(input()))


def find(m_list):
    for i in range(1,len(m_list)):
        if m_list[i]-1 != m_list[i-1]:
            return m_list[i]-1
    return -1

print(find(my_list))
