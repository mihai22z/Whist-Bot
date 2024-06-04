import unittest
from src.whist import Player, Card
from src.whist.utils import has_suit, determine_trick_winner, determine_hand_size, calculate_score


class TestUtils(unittest.TestCase):

    def test_has_suit_true(self):
        """Test has_suit returns True when the player has a card of the specified suit."""
        player = Player('Mike')
        player.cards = [Card(7, 0), Card(8, 1), Card(9, 2)]
        self.assertTrue(has_suit(player, 0))

    def test_has_suit_false(self):
        """Test has_suit returns False when the player does not have a card of the specified suit."""
        player = Player('Mike')
        player.cards = [Card(7, 0), Card(8, 1), Card(9, 2)]
        self.assertFalse(has_suit(player, 3))

    def test_determine_trick_winner_with_highest_lead_suit(self):
        """Test that the player with the highest card of the lead suit wins when no trumps are played."""
        player_moves = [(0, Card(7, 1)), (1, Card(8, 1)), (2, Card(9, 1))]
        winner = determine_trick_winner(player_moves, 2)
        self.assertEqual(winner, 2)

    def test_determine_trick_winner_with_trump_card(self):
        """Test that the player who plays the highest trump card wins."""
        player_moves = [(0, Card(7, 1)), (1, Card(10, 2)), (2, Card(12, 2))]
        winner = determine_trick_winner(player_moves, 2)
        self.assertEqual(winner, 2)

    def test_determine_trick_winner_with_lowest_trump_when_higher_lead_suit_exists(self):
        """Test that a player who plays a lower trump card wins over a higher lead suit card."""
        player_moves = [(0, Card(10, 1)), (1, Card(8, 2)), (2, Card(9, 1))]
        winner = determine_trick_winner(player_moves, 2)
        self.assertEqual(winner, 1)

    def test_determine_trick_winner_when_multiple_trumps_player(self):
        """Test that the player with the highest trump card wins when multiple trumps are played."""
        player_moves = [(0, Card(7, 1)), (1, Card(9, 1)), (2, Card(8, 1))]
        winner = determine_trick_winner(player_moves, 1)
        self.assertEqual(winner, 1)

    def test_determine_trick_winner_when_no_trumps_or_lead_suit_played(self):
        """Test that the first player wins when no one plays a trump or a lead suit card."""
        player_moves = [(0, Card(7, 3)), (1, Card(8, 1)), (2, Card(9, 0))]
        winner = determine_trick_winner(player_moves, 2)
        self.assertEqual(winner, 0)

    def test_determine_hand_size_initial_rounds(self):
        """ Test the first phase where hand size should be 1 """
        num_players = 4
        for round_number in range(1, num_players + 1):
            self.assertEqual(determine_hand_size(num_players, round_number), 1)

    def test_determine_hand_size_incrementing_rounds(self):
        """ Test the second phase where hand size increments from 2 to 7 """
        num_players = 4
        expected_sizes = [2, 3, 4, 5, 6, 7]
        for i, size in enumerate(expected_sizes, start=1):
            self.assertEqual(determine_hand_size(num_players, num_players + i), size)

    def test_determine_hand_size_constant_eight_rounds(self):
        """ Test the third phase where hand size should be constant at 8 """
        num_players = 4
        start_round = num_players + 7
        for round_number in range(start_round, start_round + num_players):
            self.assertEqual(determine_hand_size(num_players, round_number), 8)

    def test_determine_hand_size_decrementing_rounds(self):
        """ Test the fourth phase where hand size decrements from 7 to 2 """
        num_players = 4
        start_round = 2 * num_players + 7
        expected_sizes = [7, 6, 5, 4, 3, 2]
        for i, size in enumerate(expected_sizes, start=1):
            self.assertEqual(determine_hand_size(num_players, start_round + i - 1), size)

    def test_determine_hand_size_final_rounds(self):
        """ Test the last phase where hand size should be 1 """
        num_players = 4
        start_round = 2 * num_players + 13
        total_rounds = 3 * num_players + 12
        for round_number in range(start_round, total_rounds + 1):
            self.assertEqual(determine_hand_size(num_players, round_number), 1)

    def test_determine_hand_size_invalid_round(self):
        """ Test the error handling for invalid round numbers """
        num_players = 4
        total_rounds = 3 * num_players + 12
        with self.assertRaises(ValueError):
            determine_hand_size(num_players, total_rounds + 1)  # Beyond total rounds
            determine_hand_size(num_players, 0)  # Below minimum round

    def test_calculate_score_good_bid(self):
        """ Test the score is calculated correctly when the player wins the number of tricks he bid """
        bid = 3
        won_tricks = 3
        self.assertEqual(calculate_score(bid, won_tricks), 8)

    def test_calculate_score_bad_bid(self):
        """ Test the score is calculated correctly when the player does not win the number of tricks he bid """
        bid = 3
        won_tricks = 5
        self.assertEqual(calculate_score(bid, won_tricks), -2)
