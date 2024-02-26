import unittest
from src.whist import Card


class TestCard(unittest.TestCase):

    def test_card_creation(self):
        """Test card creation with valid inputs"""
        card = Card(3, 0)  # 3 of Hearts
        self.assertEqual(card.value, 3)
        self.assertEqual(card.suit, 0)
        self.assertEqual(str(card), "3 of Hearts")

        # Test the boundaries
        card_low = Card(2, 0)  # Minimum valid value
        card_high = Card(14, 3)  # Maximum valid value
        self.assertEqual(card_low.value, 2)
        self.assertEqual(card_high.value, 14)

    def test_invalid_card_creation(self):
        """Test card creation with invalid inputs raises errors"""
        with self.assertRaises(ValueError):
            Card(1, 0)  # Invalid value
        with self.assertRaises(ValueError):
            Card(15, 0)  # Invalid value
        with self.assertRaises(ValueError):
            Card(11, 2)  # Invalid value
        with self.assertRaises(ValueError):
            Card(3, -1)  # Invalid suit
        with self.assertRaises(ValueError):
            Card(13, 4)  # Invalid suit

    def test_card_comparison(self):
        """Test the card comparison operations"""
        card1 = Card(3, 1)  # 3 of Spades
        card2 = Card(5, 1)  # 5 of Spades
        card3 = Card(5, 2)  # 5 of Diamonds

        # Test less than and greater than
        self.assertTrue(card1 < card2)
        self.assertTrue(card2 > card1)

        # Test equality

        self.assertFalse(card1 == card2)
        self.assertTrue(card2 == Card(5, 1))
        self.assertFalse(card2 == card3)  # Same value, different suit

    def test_card_repr(self):
        """Test the string representation of the card"""
        card = Card(12, 2)  # Jack of Diamonds
        self.assertEqual(str(card), "Jack of Diamonds")


if __name__ == '__main__':
    unittest.main()
