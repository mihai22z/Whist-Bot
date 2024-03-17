import unittest
from src.whist import Player, HumanPlayer, Card
from unittest.mock import patch


class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        """Test player is created with the right name and an empty hand of cards"""
        name = "Mike"
        player = Player(name)
        self.assertEqual(player.name, name)
        self.assertFalse(player.cards)

    def setUp(self):
        self.name = "Mike"
        self.player = HumanPlayer(self.name)
        # Player's hand: 7 of Hearts, 8 of Spades, 9 of Diamonds
        self.player.cards = [Card(7, 0), Card(8, 1), Card(9, 2)]

    def test_human_player_make_bid(self):
        """Test human player making bid with valid input"""
        with patch('builtins.input', return_value='2'):
            bid = self.player.make_bid(is_last=False, total_bid=1)
            self.assertEqual(bid, 2)

    def test_human_player_make_bid_invalid_input(self):
        """Test human player making bid with invalid input."""
        # The first choice (-1) is invalid, as the player must choose a number from 0 to the number of cards in hand.
        with patch('builtins.input', side_effect=['-1', '2']):
            bid = self.player.make_bid(is_last=False, total_bid=1)
            self.assertEqual(bid, 2)

    def test_human_player_make_bid_underbid(self):
        """Test human player making bid with input breaking the underbid rule"""
        # The first choice (1) is invalid, as the player is the last one to bid and the total would be equal to
        # the number of cards, which is against the rules.
        with patch('builtins.input', side_effect=['1', '2']):
            bid = self.player.make_bid(is_last=True, total_bid=2)
            self.assertEqual(bid, 2)

    def test_human_player_play_card(self):
        """Test human player playing a valid card"""
        expected_card = self.player.cards[0]
        with patch('builtins.input', return_value='1'):
            card = self.player.play_card(is_first=False, lead_suit=0, trump=1)
            self.assertEqual(card, expected_card)
            self.assertNotIn(expected_card, self.player.cards)

    def test_human_player_play_card_trump(self):
        """Test human player playing a valid trump card out of necessity"""
        # Lead suit is Clubs and player does not have a Clubs card but has a Heart (trump) and must play it.
        expected_card = self.player.cards[0]
        with patch('builtins.input', return_value='1'):
            card = self.player.play_card(is_first=False, lead_suit=3, trump=0)
            self.assertEqual(card, expected_card)

    def test_human_player_play_card_invalid(self):
        """Test human player playing an invalid card"""
        # The first 2 choices (0 and 4) are invalid, as the player has to choose a number from 1 to the number of cards
        # they are currently holding.
        expected_card = self.player.cards[0]
        with patch('builtins.input', side_effect=['0', '4', '1']):
            card = self.player.play_card(is_first=False, lead_suit=0, trump=1)
            self.assertEqual(card, expected_card)

    def test_human_player_play_card_invalid_trump(self):
        """Test human player playing an invalid card when supposed to play a trump card"""
        # Lead suit is Clubs and player does not have a Clubs card but has a Spade (trump) and must play it.
        # The first 2 choices (8 of Spades and 9 of Diamonds) are invalid because the player must play a Heart (trump).
        expected_card = self.player.cards[0]
        with patch('builtins.input', side_effect=['2', '3', '1']):
            card = self.player.play_card(is_first=False, lead_suit=3, trump=0)
            self.assertEqual(card, expected_card)  # Expecting the first card (7 of Hearts) to be played

    def test_human_player_play_card_invalid_suit(self):
        """Test human player playing an invalid card when supposed to play a certain suit"""
        # Lead suit is Hearts and player has a Hearts card which they must play.
        # The first 2 choices (8 of Spades and 9 of Diamonds) are invalid since the player must play a Heart (lead suit)
        expected_card = self.player.cards[0]
        with patch('builtins.input', side_effect=['2', '3', '1']):
            card = self.player.play_card(is_first=False, lead_suit=0, trump=2)
            self.assertEqual(card, expected_card)  # Expecting the first card (7 of Hearts) to be played
