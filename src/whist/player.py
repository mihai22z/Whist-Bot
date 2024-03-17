from .utils import has_suit


class Player:
    """
    Represents a player for the Whist game, which can be either a human with human input or an AI agent.

    Attributes:
        name (string): The name of the player.
        cards (list of Card): The list of cards being held by the player.
    """

    def __init__(self, name):
        """
        Initializes the player with a name and an empty hand of cards.

        Parameters:
            name (string): The name of the player.
        """
        self.name = name
        self.cards = []

    def make_bid(self, is_last, total_bid):
        """
        Abstract method for making a bid. Subclasses should override this method to provide specific bidding behavior.

        Parameters:
            is_last (bool): True if the player is the last one to make a bid, False otherwise.
            total_bid (int): The current total bid made by all players in this round.

        Returns:
            int: The bid made by the player.
        """
        raise NotImplementedError

    def play_card(self, is_first, lead_suit, trump):
        """
        Abstract method for playing a card. Subclasses should override this method to define how the player chooses
        a card to play.

        Parameters:
            is_first (bool): True if the player is the first one to play a card in the trick, False otherwise.
            lead_suit (int): The suit that was led by the first player in the trick.
            trump (int): The trump suit for the current round.

        Returns:
            Card: The card played by the player.
        """
        raise NotImplementedError


class HumanPlayer(Player):

    def make_bid(self, is_last, total_bid):
        """
        Implements make_bid for a human player. The player is prompted to input their bid.

        Additional context is provided based on whether the player is last to bid and the current total bid.
        """
        print("Your cards are: ")
        for i, card in enumerate(self.cards):
            print(f"{i + 1}. {card}")

        if is_last:
            print("You are the last player to bid.")
            if total_bid > len(self.cards):
                print("The game is overbid; you can bid whatever you'd like.")
            else:
                print(f"The game is underbid; you cannot bid {len(self.cards) - total_bid}.")

        while True:
            try:
                bid = int(input(f"{self.name}, make a bid: "))
                if bid < 0 or bid > len(self.cards):
                    print(f"Invalid bid. You must bid a number between 0 and {len(self.cards)}.")
                elif is_last and bid == (len(self.cards) - total_bid):
                    print(f"You cannot bid {bid} as it would make the total bids equal to the number of cards.")
                else:
                    return bid
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_card(self, is_first, lead_suit, trump):
        """
        Implements play_card for a human player. The player is prompted to choose a card to play from their hand.

        If the player is not first, they must follow the lead suit or play a trump if they have no cards
        in the lead suit.
        """
        print("Your cards are: ")
        for i, card in enumerate(self.cards):
            print(f"{i + 1}. {card}")

        while True:
            try:
                card_number = int(input(f"{self.name}, select a card to play by entering its number: "))
                if card_number < 1 or card_number > len(self.cards):
                    print(f"Invalid card. Please select a card by entering a number between 1 and {len(self.cards)}.")
                    continue

                selected_card = self.cards[card_number - 1]

                if not is_first and has_suit(self, lead_suit):
                    if selected_card.suit != lead_suit:
                        print(f"You must play a card of the lead suit, {lead_suit}.")
                        continue

                elif not is_first and trump is not None and has_suit(self, trump) and selected_card.suit != trump:
                    print(f"You don't have the lead suit but have a trump suit card. You must play a trump suit, {trump}.")
                    continue

                return self.cards.pop(card_number - 1)

            except ValueError:
                print("Invalid input. Please enter a number.")
