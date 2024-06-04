class Scoreboard:
    """
    A class to manage and track scores, bids, and won tricks for each player throughout the game.

    The Scoreboard class stores a detailed record of each player's performance across multiple rounds,
    including their bids, tricks won, and scores per round. It also tracks cumulative scores to provide
    a comprehensive overview of each player's progress in the game.

    Attributes:
        scores (dict): A dictionary mapping each player to their scoring records. Each player's entry
                       contains their total cumulative score and detailed records for each round.
    """

    def __init__(self):
        """
        Initializes a new Scoreboard instance with an empty scoring dictionary.
        """
        self.scores = {}

    def add_player(self, player):
        """
        Adds a new player to the scoreboard with an initial scoring structure.

        Args:
            player (Player): The player object to add to the scoreboard. Assumes the player has a unique identifier.
        """
        if player not in self.scores:
            self.scores[player] = {
                'total_score': 0,
                'rounds': {}
            }

    def update_score(self, player, round_number, bid, won_tricks, round_score):
        """
        Updates the scoreboard with the results of a single round for a specified player.

        Args:
            player (Player): The player for whom the score is being updated.
            round_number (int): The round number being updated.
            bid (int): The bid made by the player for this round.
            won_tricks (int): The number of tricks won by the player in this round.
            round_score (int): The score achieved by the player in this round.

        This method updates both the round-specific data and the cumulative score for the player.
        """
        if player not in self.scores:
            self.add_player(player)

        round_data = self.scores[player]['rounds'].get(round_number, {})
        round_data.update({
            'bid': bid,
            'won_tricks': won_tricks,
            'score': round_score
        })

        last_total = self.scores[player]['total_score']
        new_total = last_total + round_score
        round_data['cumulative_score'] = new_total

        self.scores[player]['rounds'][round_number] = round_data
        self.scores[player]['total_score'] = new_total

    def get_score(self, player):
        """
        Retrieves the total cumulative score for a specified player.

        Args:
            player (Player): The player whose total score is requested.

        Returns:
            int: The total score of the player if they are in the scoreboard, otherwise None.
        """
        return self.scores[player]['total_score'] if player in self.scores else None

    def get_round_details(self, player, round_number):
        """
        Retrieves the details of a specific round for a specified player.

        Args:
            player (Player): The player whose round details are requested.
            round_number (int): The specific round number for which details are requested.

        Returns:
            dict: A dictionary containing bid, won tricks, score, and cumulative score for the round if available.
                  Returns None if the player or round data does not exist.
        """
        if player in self.scores and round_number in self.scores[player]['rounds']:
            return self.scores[player]['rounds'][round_number]
        return None
