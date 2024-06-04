from .card import Card
from random import shuffle


class Deck:
    """
    Represents a deck of playing cards for the Whist game. The deck is adjusted based on the number of players and
    is capable of setting a trump suit and allowing cards to be drawn.

    Attributes:
        trump (int): The suit of the trump card, initially None.
        trump_card (Card): The card is chosen as the trump, initially None.
        cards (list of Card): The list of cards in the deck.
    """

    def __init__(self, num_players):
        """
        Initializes the deck with cards appropriate for the number of players.

        Parameters:
            num_players (int): The number of players playing the game.

        Raises:
            ValueError: If the number of players is not between 3 and 6 (inclusive).
        """
        self.trump = None
        self.trump_card = None
        if num_players < 3 or num_players > 6:
            raise ValueError("Invalid number of players")
        self.cards = [Card(i, j) for i in range(3 + (6 - num_players) * 2, 16) if i != 11 for j in range(4)]
        shuffle(self.cards)

    def set_trump(self):
        """
        Sets the trump suit by drawing the last card from the deck and revealing it to all players.
        The drawn card is set aside as the trump card.

        Raises:
            RuntimeError: If the deck is empty when attempting to set the trump.
        """
        if len(self.cards) == 0:
            raise RuntimeError("Cannot set trump from an empty deck")
        self.trump_card = self.cards.pop()
        self.trump = self.trump_card.suit
        print("The trump card is " + str(self.trump_card))

    def draw(self):
        """
        Draws the top card from the deck.

        Returns:
            Card: The card drawn from the top of the deck.

        Raises:
            RuntimeError: If the deck is empty when attempting to draw a card.
        """
        if len(self.cards) == 0:
            raise RuntimeError("Cannot draw from an empty deck")
        return self.cards.pop()
