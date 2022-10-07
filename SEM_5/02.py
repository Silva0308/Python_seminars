from random import choices


def new_list(n):
    n_list = choices(range(1, n*2), k=n)
    print(n_list)
    return (n_list)


def range_num(m_list):
    ranged_list=[]
    for i in range(len(m_list)):
        f=m_list[i]
        t_list=[f]
        for x in range(i+1, len(m_list)):
            if m_list[x] >f:
                f=m_list[x]
                t_list.append(f)
        if len(t_list)>1:
            ranged_list.append(t_list)       
    return ranged_list

n = int(input())
my_list = (new_list(n))
print(range_num(my_list))