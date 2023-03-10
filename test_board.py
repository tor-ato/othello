from board import Board
from io import StringIO
import sys
import io

def test___init__():
    board = Board()

    assert board.values[3][3] == 1
    assert board.values[4][4] == 1
    assert board.values[3][4] == -1
    assert board.values[4][3] == -1

def test_display():
    board = Board()

    # テスト関数
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    board.display()
    sys.stdout = sys.__stdout__ 

    # テスト用変数
    test = io.StringIO()
    sys.stdout = test
    for i in board.values:
         print(i)
    sys.stdout = sys.__stdout__ 

    assert capturedOutput.getvalue() == test.getvalue()


def test_board_count_zeros():
    board = Board()
    expected = 60
    actual = board.count_zeros()
    assert expected == actual

def test_winner_judge():
    board = Board()

    board.values[0][0] = 1
    test_winner_one = 1
    winner_one = board.winner_judge()
    assert winner_one == test_winner_one

    board.values[0][0] = -1
    test_winner_one = -1
    winner_one = board.winner_judge()
    assert winner_one == test_winner_one

    board.values[0][0] = 0
    test_winner_one = 0
    winner_one = board.winner_judge()
    assert winner_one == test_winner_one

def test_count_reversible_rock():
    board = Board()

    excepted = [[3, 3]]

    player = -1
    X, Y = [2, 3]
    actual = board.count_reversible_rock(X, Y, player)

    assert excepted == actual



def test_count_put_able_rocks():
    board = Board()
    player = -1

    excepted = 4

    actual = board.count_put_able_spots(player)
    
    assert actual == excepted




def test_revers_rocks():
    board = Board()
    reversible_rocks = [[3, 3]]
    board.reverse_rocks(reversible_rocks)
    excepted = -1
    assert board.values[3][3] == excepted

def test_input_rock(monkeypatch):
    board = Board()
    monkeypatch.setattr('sys.stdin', StringIO('3 4'))

    player = 1

    assert board.input_rock(player) == [3, 4]










