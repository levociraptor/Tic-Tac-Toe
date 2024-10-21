from random import choice


def check_win_the_game(playing_field: list[list[str]], symbol: str) -> bool:
    """Функция проверяет есть ли выигрышная комбинация на поле"""
    # Проверка игрового поля во вертикали и горизонтали
    counter = 0
    for i in range(len(playing_field)):
        for j in range(len(playing_field[i])):
            if playing_field[i][j] == symbol:
                if i == 0:
                    if playing_field[i+1][j] == symbol and playing_field[i+2][j] == symbol:
                        return True
                counter += 1
        if counter == 3:
            return True
        else:
            counter = 0

    # Проверка игрового поля по диагонали
    if playing_field[1][1] == symbol:
        if playing_field[0][0] == symbol and playing_field[2][2] == symbol:
            return True
        if playing_field[0][2] == symbol and playing_field[2][0] == symbol:
            return True

    # Если нигде на поле нет выгрышной комбинации возвращается ложь
    return False


def output_playing_field_on_screen(playing_field: list[list[str]]) -> None:
    """Функция выыодит игровое поле на экран"""
    for line in playing_field:
        for cell in line:
            print(cell, end='  ')
        print('\n')
    print('\n\n')


def main() -> None:
    # Правила игры
    print('Приветсвую вас и игре крестики и нолики\n'
          'Для начала вам надо будет выбрать символ, которым вы будуте играть\n'
          'У вас будет выбор из крестика "X" и нолика "0" \n'
          'Потом будет выведено поле наполненое звездочками "*"\n'
          'Вам нужно будет ввести номер строчки и номер столбца, '
          'в котором вы хотите поставить ваш символ \n'
          'Потом ход сделает ваш противник\n'
          'Игра будет закончена, когда либо вы, либо ваш противник соберет'
          ' линию из ваших элементов\n'
          'Линия может быть собрана по вертикали, по горизонтали или по диагонали')

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

    # Задание игрового поля
    playing_field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

    # Создания списка возможных вариантов для хода
    validation_field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Вывод в консоль поля для игры
    for line in playing_field:
        for cell in line:
            print(cell, end='  ')
        print('\n')

    # Счетчик ходов
    counter = 0

    # Бесконечный игровой цикл
    while True:
        # Игрок вводит номер строки и столбца куда он поставит свой символ
        player_move_line = int(input('Введите номер строки куда вы хотите поставить ваш символ\n'))
        player_move_column = int(input('Введите номер колонки куда вы хотите поставить ваш символ\n'))

        # Проверка занята ли выбранная клетка
        if validation_field[player_move_line-1][player_move_column-1] == 0:
            print('Выбраная вами клетка уже занята. Пожалуйста, выберете другую')
            continue

        # Замена звездочки, на которую указал игрок символом, которым игрок играет
        playing_field[player_move_line-1][player_move_column-1] = player_symbol

        # Удаление из списка возможных для хода вариантов, уже сделанного хода
        validation_field[player_move_line-1][player_move_column-1] = 0

        # Вывод в консоль поля для игры
        output_playing_field_on_screen(playing_field)

        # Проверка на выигрыш игрока
        if check_win_the_game(playing_field, player_symbol):
            print('Поздравляю вы победили')
            break

        # Проверка на конец игры
        counter += 1
        if counter == 9:
            print('Ничья')
            break

        # Ход противника
        while True:
            bot_move = choice(choice(validation_field))
            if bot_move != 0:
                break

        for i in range(len(validation_field)):
            if bot_move in validation_field[i]:
                index = validation_field[i].index(bot_move)
                validation_field[i][index] = 0
                playing_field[i][index] = bot_symbol

        # Вывод в консоль поля для игры
        output_playing_field_on_screen(playing_field)

        # Проверка на выигрыш бота
        if check_win_the_game(playing_field, bot_symbol):
            print('К сожалению вас обыграли')

        # Проверка на конец игры
        counter += 1
        if counter == 9:
            print('Ничья')
            break

if __name__ == '__main__':
    main()