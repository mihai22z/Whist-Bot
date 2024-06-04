def has_suit(player, suit):
    """
    Determines whether the player has at least one card of the specified suit in their hand.

    Parameters:
        player (Player): The player whose hand is being checked. It's expected that the player has a 'cards' attribute,
                         which is a list of Card objects.
        suit (int): The suit to check for in the player's hand. Suits are represented as integers
                    (e.g., 0 for Hearts, 1 for Spades, etc.), and this representation should be consistent across
                    the game's logic.

    Returns:
        bool: True if there's at least one card of the specified suit in the player's hand; otherwise, False.

    Note:
        The function does not modify the player's hand or any card within it. It's a read-only operation that can
        be safely used at any point in the game logic without side effects.
    """
    return any(card.suit == suit for card in player.cards)


def determine_trick_winner(player_moves, trump):
    """
    Determines the winning player in a trick based on the cards played and the rules for trump and lead suits.

    The function iterates through the player_moves to find the highest trump card played; if no trump cards are played,
    it finds the highest card of the lead suit. The player who played the highest-ranking card wins the trick.

    Parameters:
        player_moves (list of tuples): Each tuple contains an integer representing the player's position
                                         and a Card object representing the card played by that player.
        trump (int): The integer representing the trump suit of the current round. If there is no trump,
                       this could be None.

    Returns:
        int: The position of the player who won the current trick. This is the index in the game's player list,
               not a unique player identifier.

    Note:
        The function assumes that player_moves is not empty and that each player plays exactly one card in the trick.
    """
    if not player_moves:
        raise ValueError("player_moves cannot be empty")

    lead_suit = player_moves[0][1].suit
    max_trump_value = 0
    max_lead_suit_value = 0
    winning_player_pos = player_moves[0][0]
    for i, move in enumerate(player_moves):
        player_pos = move[0]
        card = move[1]
        if card.suit == trump and card.value > max_trump_value:
            max_trump_value = card.value
            winning_player_pos = player_pos
        elif card.suit == lead_suit and card.value > max_lead_suit_value and max_trump_value == 0:
            max_lead_suit_value = card.value
            winning_player_pos = player_pos
    return winning_player_pos


def determine_hand_size(num_players, round_number):
    """
    Calculates the number of cards (hand size) to be dealt to each player in a given round of a card game.

    The game follows a specific round structure based on the number of players (X):
    - First X rounds: Hand size is 1.
    - Next 6 rounds: Hand size increments sequentially from 2 to 7.
    - Next X rounds: Hand size is 8.
    - Next 6 rounds: Hand size decrements sequentially from 7 to 2.
    - Last X rounds: Hand size is 1.

    Args:
        num_players (int): The number of players participating in the game.
        round_number (int): The current round number.

    Returns:
        int: The hand size for the given round.

    Raises:
        ValueError: If the round number is out of the expected range based on the game structure.
    """
    total_rounds = 3 * num_players + 12
    third_phase_start = num_players + 7  # Start of the third phase
    fifth_phase_start = 2 * num_players + 13  # Start of the fifth phase

    if round_number <= num_players:
        # First phase: increasing from 1 up to 1 (constant)
        return 1
    elif num_players < round_number <= num_players + 6:
        # Second phase: increasing from 2 to 7
        return round_number - num_players + 1
    elif third_phase_start <= round_number <= third_phase_start + num_players - 1:
        # Third phase: constant at 8
        return 8
    elif third_phase_start + num_players <= round_number <= third_phase_start + num_players + 5:
        # Fourth phase: decreasing from 7 to 2
        return 8 - (round_number - (third_phase_start + num_players - 1))
    elif fifth_phase_start <= round_number <= total_rounds:
        # Fifth phase: constant at 1
        return 1
    else:
        # This condition should not normally be hit unless an invalid round_number is provided
        raise ValueError("Invalid round number")


def calculate_score(bid, won_tricks):
    """
    Calculates the score a player obtained at the end of a round, depending on their bid and number of won tricks.

    Args:
        bid (int): The number of tricks the player bid for at the start of the round.
        won_tricks (int): The number of tricks the player won by the end of the round.

    Returns:
        int: The score to be added to the total score of the player. This score can be negative.
    """
    if bid == won_tricks:
        return 5 + bid
    else:
        return -abs(bid - won_tricks)
