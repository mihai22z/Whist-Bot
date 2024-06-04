from .utils import determine_trick_winner, determine_hand_size, calculate_score
from .deck import Deck
from .scoreboard import Scoreboard


class Game:

    def __init__(self, players):
        self.players = players
        self.num_players = len(players)
        self.lead_player_pos = 0
        self.player_moves = []
        self.discard_deck = []
        self.deck = Deck(self.num_players)
        self.scoreboard = Scoreboard()
        self.current_bids = [0] * self.num_players
        self.current_won_tricks = [0] * self.num_players
        for player in players:
            self.scoreboard.add_player(player)

    def play_round(self, round_number):
        self.current_bids = [0] * self.num_players
        self.current_won_tricks = [0] * self.num_players

        hand_size = determine_hand_size(self.num_players, round_number)
        self.deal_cards(hand_size)
        if hand_size < 8:
            self.deck.set_trump()

        self.make_bids(hand_size)
        for i in range(hand_size):
            trick_winner_pos = self.play_trick(self.deck.trump)
            self.current_won_tricks[trick_winner_pos] = self.current_won_tricks[trick_winner_pos] + 1

        for i in range(self.num_players):
            player = self.players[i]
            bid = self.current_bids[i]
            won_tricks = self.current_won_tricks[i]
            score = calculate_score(bid, won_tricks)
            self.scoreboard.update_score(player, round_number, bid, won_tricks, score)

    def make_bids(self, hand_size):
        total_bid = 0
        for i in range(0, self.num_players - 1):
            player_pos = (self.lead_player_pos + i) % self.num_players
            player = self.players[player_pos]
            self.current_bids[player_pos] = player.make_bid(False, total_bid)
        last_player = self.players[self.lead_player_pos - 1]
        self.current_bids[self.lead_player_pos - 1] = last_player.make_bid(True, total_bid)

    def deal_cards(self, hand_size):
        self.deck = Deck(self.num_players)
        for i in range(hand_size):
            for j in range(0, self.num_players):
                player_pos = (self.lead_player_pos + j) % self.num_players
                player = self.players[player_pos]
                player.cards.append(self.deck.draw())

    def play_trick(self, trump):
        """
        Executes a single trick in the game, where each player plays a card in turn.

        The function starts with the lead player, identified by 'self.lead_player_pos', playing the first card.
        Subsequent players play their cards based on the lead suit and trump suit rules. The function determines
        the winner of the trick using the 'determine_trick_winner' utility function, updates the lead player
        for the next trick, and moves all played cards to the discard deck.

        Parameters:
            trump (int): The suit that acts as the trump for the current round. Can be 'None' if there's no trump.

        Returns:
            int: The position of the player who won the trick. This player will lead the next trick.
        """
        self.player_moves.clear()
        lead_card = self.players[self.lead_player_pos].play_card(is_first=True, lead_suit=None, trump=trump)
        self.player_moves.append((self.lead_player_pos, lead_card))
        lead_suit = lead_card.suit

        for i in range(1, self.num_players):
            player_pos = (self.lead_player_pos + i) % self.num_players
            player = self.players[player_pos]
            self.player_moves.append((player_pos, player.play_card(is_first=False, lead_suit=lead_suit, trump=trump)))

        trick_winner_pos = determine_trick_winner(self.player_moves, trump)
        self.lead_player_pos = trick_winner_pos

        for move in self.player_moves:
            self.discard_deck.append(move[1])

        return trick_winner_pos
