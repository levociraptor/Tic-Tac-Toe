from random import randint


class Board:
    def __init__(self) -> None:
        self.playing_field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

    def display_field(self) -> None:
        for line in self.playing_field:
            for cell in line:
                print(cell, end='  ')
            print('\n')

        print()

    def player_move(self, x: int, y: int, symbol: str) -> None:
        while True:
            if self.playing_field[x-1][y-1] != '*':
                print('Выбранное место уже занято выберете другое')
                x = int(input('Введите номер строки куда вы хотите поставить ваш символ\n'))
                y = int(input('Введите номер колонки куда вы хотите поставить ваш символ\n'))
            else:
                self.playing_field[x-1][y-1] = symbol
                return

    def bot_move(self, symbol: str) -> None:
        while True:
            x = randint(0, 2)
            y = randint(0, 2)
            if self.playing_field[x][y] != '*':
                continue

            self.playing_field[x][y] = symbol
            return

    def _get_diagonal_lines(self) -> list[list[str]]:
        if len(self.playing_field) != 3:
            raise ValueError('Программа работает корректно, только с полем 3 на 3')

        lines = []
        one_line = [self.playing_field[0][0], self.playing_field[1][1], self.playing_field[2][2]]
        another_line = [self.playing_field[0][2], self.playing_field[1][1], self.playing_field[2][0]]
        lines.extend([one_line, another_line])
        return lines

    def _get_horizontal_lines(self) -> list[list[str]]:
        return self.playing_field

    def _get_vertical_lines(self) -> list[list[str]]:
        if len(self.playing_field) != 3:
            raise ValueError('Программа работает корректно, только с полем 3 на 3')

        lines = [['*'] * len(self.playing_field[0]) for _ in range(len(self.playing_field))]

        for i in range(len(self.playing_field)):
            for j in range(len(self.playing_field[i])):
                lines[j][i] = self.playing_field[i][j]

        return lines

    def _check_line_winner(self, line: list[str]) -> bool:
        symbols = set(line)

        if len(symbols) == 1 and symbols.pop() != '*':
            return True

        return False

    def check_win_game(self) -> bool:
        lines = []
        lines.extend(self._get_diagonal_lines())
        lines.extend(self._get_horizontal_lines())
        lines.extend(self._get_vertical_lines())

        for line in lines:
            if self._check_line_winner(line):
                return True

        return False
