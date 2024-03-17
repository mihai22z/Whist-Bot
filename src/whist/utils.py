def has_suit(player, suit):
    """
    Checks if the player has a card of the specified suit in their hand.

    Parameters:
        - player: The player object. This function assumes that the player object has an attribute 'cards' which
                  is a list of Card objects.
        - suit: An integer representing the suit to check for. The suits are typically represented by integers
                (e.g., 0 for Hearts, 1 for Spades, etc.).

    Returns:
        - bool: True if the player has at least one card of the specified suit, False otherwise.
    """
    return any(card.suit == suit for card in player.cards)
