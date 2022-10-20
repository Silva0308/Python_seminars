from pathlib import Path
from exceptions import data_search, user_choice


def look():  # поиск по данным
    search = data_search()
    file = Path("Python_seminars", "SEM_7", 'Phonebook.csv')
    if file.exists:
        with open(file, 'r', encoding='utf-8') as text:
            count = False
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                if search in v:
                    print('Данные из телефонного справочника в фаиле Phonebook.csv')
                    print(v.strip())
                    count = True
            if not count:
                print('Таких данных нет в справочнике фаила Phonebook.csv')

    file1 = Path("Python_seminars", "SEM_7", 'Phonebook.txt')
    if file1.exists:
        with open(file1, 'r', encoding='utf-8') as text:
            count = False
            text_txt = text.readlines()
            for i, v in enumerate(text_txt):
                if search in v:
                    while i == '':
                        i -= 1
                    print('Данные из телефонного справочника в фаиле Phonebook.txt')
                    print(
                        f'{text_txt[i - 1]}{text_txt[i]}{text_txt[i + 1]}{text_txt[i + 2]}{text_txt[i + 3]}\n')
                    count = True
            if not count:
                print('Таких данных нет в справочнике фаила Phonebook.txt')
            return search


def delete_contact():
    look()
    print('Введите номер записи, которую хотите удалить:\n')
    del_key = user_choice()
    file = Path("Python_seminars", "SEM_7", 'Phonebook.csv')
    with open(file, 'r', encoding='utf-8') as data:
        contact = data.readlines()
        with open(file, 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if i != del_key:
                    data.write(contact[i])
    return del_key
