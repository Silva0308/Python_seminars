#2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from pprint import pprint 

def last_names():
    last_names = []
    while True:
        last_name = input("Введите фамилию: ")
        if last_name == 'end':
            return last_names
        last_names.append(last_name)

def get_name(last_names):
    names = []
    for i in range(len(last_names)):
        name = input("Введите имя: ")
        names.append(name)

def telephone(last_names):
    tels = []
    for i in range(len(last_names)):
        tel = input("Введите номер телефона: ")
        tels.append(tel)

def info(last_names):
    des = []
    for i in range(len(last_names)):
        info = input("Введите комментарий: ")
        des.append(info)


def dic(last_names, names, tels, info):
    pb={}
    for i in range(len(last_names)):
        key=i+1
        pb[key]=[]
        pb[key].append(last_names[i])
        pb[key].append(names[i])
        pb[key].append(tels[i])
        pb[key].append(info[i])
    return pb


print(dic(last_names(), get_name(last_names()), telephone(last_names()), info(last_names())))