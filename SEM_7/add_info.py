from pathlib import Path


def adding():
    to_add = []
    print("\nВы добавляете информацию в телефонную книгу.\n")
    to_add.append(input('Фамилия: '))
    to_add.append(input('Имя: '))
    to_add.append(input('Номер телефона: '))
    to_add.append(input('Описание: '))
    file3 = Path("Python_seminars", "SEM_7", 'last_key.txt')
    with open(file3, "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    file = Path("Python_seminars", "SEM_7", 'Phonebook.csv')
    with open(file, "a", encoding='utf-8') as base:
        base.write('\n{},{},{},{},{}\n\n'.format(
            new_key + 1, to_add[0], to_add[1], to_add[2], to_add[3]))
    file2 = Path("Python_seminars", "SEM_7", 'Phonebook.txt')
    with open(file2, "a", encoding='utf-8') as b_t:
        b_t.write(
            f'№ {new_key + 1}\nФамилия: {to_add[0]}\nИмя: {to_add[1]}\nНомер телефона: {to_add[2]}\nОписание: {to_add[3]}\n\n\n')
    with open(file3, "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
    return to_add
