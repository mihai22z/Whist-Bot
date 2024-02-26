class Card:
    suits = ["Hearts",
             "Spades",
             "Diamonds",
             "Clubs"]

    # First two elements, have the value None so that each card value corresponds to the values tuple index
    # Same applies for 11, since it is not part of the Whist game
    values = ["None", "None", "2",
              "3", "4", "5", "6",
              "7", "8", "9", "10",
              "None", "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        # value and suit are ints
        if v < 2 or v > 14 or v == 11:
            raise ValueError("Invalid card value")
        if s < 0 or s > 3:
            raise ValueError("Invalid card value")
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        else:
            return False

    def __eq__(self, c2):
        return self.value == c2.value and self.suit == c2.suit

    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"
