# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def getbin(num):
    if (num==0):
        k=[0] 
        return k 
    else:
        s = []
        while(num):
            s.append(num%2)
            num=num//2
        s.reverse()    
        return s
print(getbin(24))