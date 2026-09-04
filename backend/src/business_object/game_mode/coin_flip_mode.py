import secrets
from datetime import datetime

from business_object.game import Game
from business_object.player import Player
from business_object.game_mode.game_mode import GameMode


class CoinFlipMode(GameMode):
    """Game mode based on a coin flip."""

    def play(self, p1: Player, p2: Player, choice="heads", **kwargs) -> Game:
        """
        Play a coin flip game between two players.

        The first player chooses heads or tails. A random coin side
        is generated. If the result matches the first player's choice,
        player 1 wins; otherwise, player 2 wins.

        Args:
            p1: The first player.
            p2: The second player.
            choice: The first player's choice, either "heads" or "tails".
            **kwargs: Additional parameters, not used by this mode.

        Returns:
            A Game object containing the result of the coin flip.
        """
        result = secrets.choice(["heads", "tails"])

        winner = p1 if result == choice else p2

        description = (
            f"{p1.username} chose {choice}. "
            f"The coin landed on {result}."
        )

        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=description,
            timestamp=datetime.now()
        )