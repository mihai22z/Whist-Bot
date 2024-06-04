import unittest
from src.whist import Deck, Card


class TestDeck(unittest.TestCase):

    def test_deck_creation(self):
        """Test deck creation with valid inputs"""
        # Initialize a deck
        num_players = 4
        deck = Deck(num_players)

        # Generate the expected list of cards for the same number of players
        expected_deck = []
        for i in range(3 + (6 - num_players) * 2, 16):
            for j in range(4):
                if i != 11:
                    expected_deck.append(Card(i,j))

        # Convert both lists to sets for easy comparison
        deck_set = set((card.value, card.suit) for card in deck.cards)
        expected_deck_set = set((card.value, card.suit) for card in expected_deck)

        # Assert the two sets are equal
        self.assertSetEqual(deck_set, expected_deck_set)

    def test_invalid_deck_creation(self):
        """Test deck creation with invalid inputs raises errors"""
        with self.assertRaises(ValueError):
            deck = Deck(2)  # Invalid number of players
        with self.assertRaises(ValueError):
            deck = Deck(7)  # Invalid number of players

    def test_trump_set(self):
        """Test that the trump is correctly set"""
        deck = Deck(4)
        expected_trump = deck.cards[-1].suit
        deck.set_trump()
        self.assertEqual(expected_trump, deck.trump)

    def test_trump_card_set(self):
        """Test that the trump card is correctly set"""
        deck = Deck(4)
        expected_trump_card = deck.cards[-1]
        deck.set_trump()
        self.assertEqual(expected_trump_card, deck.trump_card)

    def test_empty_deck_trump(self):
        """Test setting the trump card for an empty deck raises errors"""
        deck = Deck(4)
        deck.cards = []
        with self.assertRaises(RuntimeError):
            deck.set_trump()

    def test_draw(self):
        """Test drawing a card from the deck"""
        deck = Deck(4)
        expected_card = deck.cards[-1]
        drawn_card = deck.draw()
        self.assertEqual(drawn_card, expected_card)

    def test_draw_empty_deck(self):
        """Test drawing a card from an empty deck raises errors"""
        deck = Deck(4)
        deck.cards = []
        with self.assertRaises(RuntimeError):
            deck.draw()


if __name__ == '__main__':
    unittest.main()
