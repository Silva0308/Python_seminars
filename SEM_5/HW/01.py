# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

from random import sample
import string

def make_str(n:int):
    result_str=''
    for x in range(n):
        result_str += '{} '.format("".join(sample('абв', k=3)))
    return result_str

def cut_word(m_str:str):
    new_str = m_str.replace('абв ','')
    return new_str  
    #Сначала сделала такой вариант, он тоже работает :)
    # a='абв'                   
    # split_line = m_str.split()
    # final_list = [word for word in split_line if word !=a]
    # final_string = ' '.join(final_list)
    # return final_string


n=int(input("Введите количество слов: "))
if n<1:
    print('проверьте цифру')
else:
    text= make_str(n)
    print(text)    
print(cut_word(text))