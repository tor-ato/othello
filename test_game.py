from game import Game

def test__init__():
    game = Game()
    test = 0
    assert game.player == test
    

def test_coin_tos():
    game = Game()
    test_one = 1
    test_minus_one = -1

    game.coin_tos()

    assert game.player in [test_one, test_minus_one]


def test_change_player():
    game = Game()
    game.player = 1
    game.change_player()
    test_one_minus = -1
    assert game.player == test_one_minus

    game.player = -1
    game.change_player()
    test_one = 1
    assert game.player == test_one

    
