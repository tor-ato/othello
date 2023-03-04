from board import Board

def test_board_count_zeros():
    board = Board()
    expected = 60
    actual = board.count_zeros()
    assert expected == actual

def test_hoge():
    assert 100 == 100