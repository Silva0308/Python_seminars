from pathlib import Path


def writing_scv(phonebook):
    file = Path("Python_seminars", "SEM_7", 'Phonebook.csv')
    with open(file, 'a', encoding='utf-8') as data:
        data.write('№,Фамилия,Имя,Номер телефона,Описание\n')
        for v in phonebook.items():
            data.write(
                f'{last_key()},{v[0]},{v[1]},{v[2]},{v[3]}\n')


def writing_txt(phonebook):
    file = Path("Python_seminars", "SEM_7", 'Phonebook.txt')
    with open(file, 'a', encoding='utf-8') as data:
        for v in phonebook.items():
            data.write(
                f'№ {last_key()}\nФамилия: {v[0]}\nИмя: {v[1]}\nНомер телефона: {v[2]}\nОписание: {v[3]}\n\n')


def last_key():
    file = Path("Python_seminars", "SEM_7", 'last_key.txt')
    with open(file, "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    with open(file, "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
    return new_key + 1

# writing_txt(phonebook)
# writing_scv(phonebook)
