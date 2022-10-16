import csv
from user_interface import get_info as gi
from pathlib import Path
def creating ():
    file = Path("Python_seminars", "SEM_7",'Phonebook.csv')
    with open (file, 'w', encoding = 'utf-8') as data:
        file_writer = csv.writer(data, delimiter = ",", lineterminator="\r")
        file_writer.writerow(['Фамилия', 'Имя','Номер телефона','Описание'])
        file_writer.writerow(gi())