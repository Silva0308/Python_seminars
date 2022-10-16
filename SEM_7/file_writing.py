from user_interface import get_info as gi
from pathlib import Path
import csv

info = gi()
def writing_scv ():
    file = Path("Python_seminars", "SEM_7",'Phonebook.csv')
    with open (file, 'w', encoding = 'utf-8') as data:
        file_writer = csv.writer(data, delimiter = ",", lineterminator="\r")
        file_writer.writerow(['Фамилия', 'Имя','Номер телефона','Описание'])
        file_writer.writerow(info)

def writing_txt ():
    file = Path("Python_seminars", "SEM_7",'Phonebook.txt')
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')