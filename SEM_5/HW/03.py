# # 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

board = list(range(1, 10))
wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
        (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|',
              board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-' * 13)


def take_input(player):
    while True:
        value = input('Куда поставить ' + player+'? ')
        if not (value in '123456789'):
            print('Ошибка. Повторите ввод')
            continue
        value = int(value)
        if str(board[value - 1]) in '❌⭕':
            print('Эта клетка занята. Повторите ввод')
            continue
        board[value - 1] = player
        break


def check():
    for each in wins:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def game():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('❌')
        else:
            take_input('⭕')
        if counter > 3:
            winner = check()
            if winner:
                draw_board()
                print('Ура! 🎉', winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья!')
            break


game()
