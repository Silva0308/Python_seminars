# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
from random import randint


def input_dat(name):
    while True:
        x = (
            input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
        if not (x.isdigit()):
            print('Вы ввели не число!')
            continue
        x = int(x)
        if x < 1 or x > 28:
            print("Введите корректное количество конфет: ")
            continue
        return x


def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = input("Введите имя игрока: ")
player2 = "Умный бот"
value = 258
flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = value % (28+1)
        if k==0:
            k=randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
