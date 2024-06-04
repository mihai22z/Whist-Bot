import unittest
from src.whist import Scoreboard, Player


class TestScoreBoard(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard()
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")
        self.scoreboard.add_player(self.player1)
        self.scoreboard.add_player(self.player2)

    def test_add_player(self):
        """Test adding a new player to the scoreboard."""
        self.scoreboard.add_player(self.player1)
        self.assertIn(self.player1, self.scoreboard.scores)
        self.assertEqual(self.scoreboard.scores[self.player1]['total_score'], 0)
        self.assertEqual(self.scoreboard.scores[self.player1]['rounds'], {})

    def test_update_score(self):
        """Test updating the score for a player."""
        self.scoreboard.update_score(self.player1, 3, 3, 2, -1)
        self.assertIn(3, self.scoreboard.scores[self.player1]['rounds'])
        self.assertEqual(self.scoreboard.scores[self.player1]['total_score'], -1)
        round_details = self.scoreboard.get_round_details(self.player1, 3)
        self.assertEqual(round_details['bid'], 3)
        self.assertEqual(round_details['won_tricks'], 2)
        self.assertEqual(round_details['score'], -1)
        self.assertEqual(round_details['cumulative_score'], -1)

    def test_get_score(self):
        """Test retrieving the total score for a player."""
        self.scoreboard.update_score(self.player1, 1, 2, 1, 5)
        self.scoreboard.update_score(self.player1, 2, 2, 2, 15)
        total_score = self.scoreboard.get_score(self.player1)
        self.assertEqual(total_score, 20)

    def test_get_round_details(self):
        """Test retrieving details of a specific round for a player."""
        self.scoreboard.update_score(self.player1, 1, 2, 1, 5)
        details = self.scoreboard.get_round_details(self.player1, 1)
        self.assertIsNotNone(details)
        self.assertEqual(details['bid'], 2)
        self.assertEqual(details['won_tricks'], 1)
        self.assertEqual(details['score'], 5)

    def test_nonexistent_player(self):
        """Test the behavior for a nonexistent player."""
        nonexistent_player = Player("Charlie")
        score = self.scoreboard.get_score(nonexistent_player)
        self.assertIsNone(score)
        details = self.scoreboard.get_round_details(nonexistent_player, 1)
        self.assertIsNone(details)


if __name__ == '__main__':
    unittest.main()
