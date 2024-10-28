import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_game_created(self):
        frame = Frame(1, 5)
        game = BowlingGame()
        game.add_frame(frame)
        self.assertEqual(frame, game.get_frame_at(0))

    def test_get_frame_raises_on_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_add_frame_can_add_10_games(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        last_frame = Frame(2, 6)
        game.add_frame(last_frame)
        self.assertEqual(last_frame, game.get_frame_at(9))

    def test_add_frame_raises_on_11_games(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertRaises(BowlingError, game.add_frame, Frame(2,6))

    def test_calculate_scores_sums_scores_of_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(81, game.calculate_score())