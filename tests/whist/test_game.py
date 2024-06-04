import unittest
from src.whist import Game, Player, Card
from unittest.mock import patch


class TestGame(unittest.TestCase):

    def setUp(self):
        player1 = Player("Alice")
        # Alice's hand: King of Hearts, 9 of Diamonds, 10 of Clubs
        player1.cards = [Card(14, 0), Card(9, 2), Card(10, 3)]

        player2 = Player("Bob")
        # Bob's hand: 8 of Hearts, 7 of Diamonds, King of Diamonds
        player2.cards = [Card(8, 0), Card(7, 2), Card(14, 2)]

        player3 = Player("Charlie")
        # Charlie's hand: Queen of Diamonds, Jack of Clubs, Ace of Clubs
        player3.cards = [Card(13, 2), Card(12, 3), Card(15, 3)]

        player4 = Player("Dan")
        # Dan's hand: 8 of Spades, 10 of Spades, King of Spades
        player4.cards = [Card(8, 1), Card(10, 1), Card(14, 1)]

        self.game = Game([player1, player2, player3, player4])

    def test_play_trick_first_player_plays_first_card(self):
        """Test play_trick will have the lead player play the first card of the trick."""
        cards_to_play = [Card(14, 0), Card(8, 0), Card(12, 3), Card(8, 1)]
        expected_first_card = cards_to_play[0]
        with patch.object(Player, 'play_card', side_effect=cards_to_play) as mock_play_card:
            self.game.play_trick(trump=0)

            self.assertTrue(mock_play_card.called, "The play_card method was not called")
            self.assertEqual(self.game.player_moves[0][1], expected_first_card,
                             "The first card played was not as expected")
            self.assertEqual(self.game.player_moves[0][0], 0, "The first player did not play the first card")
            
