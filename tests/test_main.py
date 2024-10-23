from tic_tac.playing_field import Board


def test__check_win_game__return_false():
    board = Board()

    result = board.check_win_game()

    assert result == False


def test__check_win_game__return_true():
    board = Board()
    board.player_move(1, 1, 'X')
    board.player_move(1, 2, 'X')
    board.player_move(1, 3, 'X')

    result = board.check_win_game()

    assert result == True


def test__get_diagonal_lines__return_diagonal_lines():
    board = Board()
    board.playing_field = [['1', '*', '1'], ['*', '1', '*'], ['1', '*', '1']]

    lines = board._get_diagonal_lines()

    assert lines == [['1', '1', '1'], ['1', '1', '1']]


def test__get_horizontal_lines__return_horizontal_lianes():
    board = Board()
    board.playing_field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    lines = board._get_horizontal_lines()

    assert lines == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def test__get_vetical_lines__return_vertical_lines():
    board = Board()
    board.playing_field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    lines = board._get_vertical_lines()

    assert lines == [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
