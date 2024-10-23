from playing_field import Board

from typing import Callable

board = Board()


def closure_counter() -> Callable:
    count = 0

    def inner_counter() -> bool:
        nonlocal count
        count += 1
        if count == 9:
            return True
        else:
            return False

    return inner_counter


def main() -> None:
    while True:
        # Выбор фигуры, которой будет играть игрок и бот
        player_symbol = input('\nВведите символ, которым вы будете играть\n'
                              'На выбор у вас есть символ Х и 0\n')

        x_varint = ['x', 'X', 'х', 'Х']
        o_variant = [0, 'o', 'O', 'о', 'О']
        if player_symbol in x_varint:
            bot_symbol = '0'
            break
        elif player_symbol in o_variant:
            bot_symbol = 'X'
            break
        else:
            print('Вы выбрали некоректный символ\n'
                  'Пожалуйста выберете символ x или о')
    print()

    board.display_field()

    # Счетчик ходов

    counter = closure_counter()

    # Бесконечный игровой цикл
    while True:
        # Игрок вводит номер строки и столбца куда он поставит свой символ
        player_move_line = int(input('Введите номер строки куда вы хотите поставить ваш символ\n'))
        player_move_column = int(input('Введите номер колонки куда вы хотите поставить ваш символ\n'))

        board.player_move(player_move_line, player_move_column, player_symbol)

        board.display_field()

        if board.check_win_game():
            print("Вы выиграли")
            break

        # Проверка на конец игры
        if counter():
            print('Ничья')
            break

        board.bot_move(bot_symbol)

        board.display_field()

        if board.check_win_game():
            print("Выигрыл бот")
            break

        # Проверка на конец игры
        if counter():
            print('Ничья')
            break


if __name__ == '__main__':
    main()
