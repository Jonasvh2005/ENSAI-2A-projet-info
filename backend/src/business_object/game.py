from datetime import datetime
from business_object.player import Player


class Game:
    """Represent a game played between two players."""

    def __init__(
        self,
        player1: Player,
        player2: Player,
        game_mode: str,
        winner: Player | None,
        description: str,
        timestamp: datetime
    ):
        """
        Initialize a Game object.

        Args:
            player1: The first player participating in the game.
            player2: The second player participating in the game.
            game_mode: The type of game played, either "coinflip" or "dice".
            winner: The player who won the game, or None in case of a draw.
            description: Additional information about the game.
            timestamp: The date and time when the game was played.
        """
        self.id = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        """
        Return a human-readable representation of the game.

        Returns:
            A string describing the game, the two players, and the winner.
        """
        winner_name = self.winner.username if self.winner else "Draw"
        return (
            f"{self.game_mode} between {self.player1.username} "
            f"and {self.player2.username}. Winner: {winner_name}"
        )

