class Card:
    """
    Represents a card in a deck for the Whist game, with suit and value attributes.

    Attributes:
        suits (list of str): Class variable that defines the suit names.
        values (list of str) Class variable that defines the card values, with 'None' placeholders for indices 0, 1 and
        11 to align the card values with their indices.

    Parameters:
        v (int): The value index of the card. Must be between 2 and 14, excluding 11, which is not used in the game.
        s (int): The suit index of the card. Must be between 0 and 3, corresponding to the suits list.

    Raises:
        ValueError: If 'v' is not in the allowed range or if 's' is not between 0 and 3 (inclusive).
    """
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = ["None", "None", "2", "3", "4", "5", "6", "7", "8", "9", "10", "None", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        if v < 2 or v > 14 or v == 11:
            raise ValueError("Invalid card value")
        if s < 0 or s > 3:
            raise ValueError("Invalid suit index")
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        """
        Less than comparison for sorting cards by value.

        Parameters:
            c2 (Card): Another card to compare to.

        Returns:
            bool: True if this card's value is less than the value of c2, False otherwise.
        """
        if self.value < c2.value:
            return True
        else:
            return False

    def __gt__(self, c2):
        """
        Greater than comparison for sorting cards by value.

        Parameters:
            c2 (Card): Another card to compare to.

        Returns:
            bool: True if this card's value is greater than the value of c2, False otherwise.
        """
        if self.value > c2.value:
            return True
        else:
            return False

    def __eq__(self, c2):
        """
        Equality comparison based on both value and suit.

        Parameters:
            c2 (Card): Another card to compare to.

        Returns:
            bool: True if both the value and suit of the cards are equal, False otherwise.
        """
        return self.value == c2.value and self.suit == c2.suit

    def __repr__(self):
        """
        Provides a human-readable string representation of the Card instance.

        Returns:
            str: A string in the form 'Value of Suit', representing the card.
        """
        return f"{self.values[self.value]} of {self.suits[self.suit]}"
