import secrets
from datetime import datetime

from business_object.game import Game
from business_object.player import Player
from business_object.game_mode.game_mode import GameMode


class DiceMode(GameMode):
    """Game mode where both players roll a die."""

    def play(self, p1: Player, p2: Player, **kwargs) -> Game:
        """
        Play a dice game between two players.

        Each player rolls a six-sided die. The player with the
        highest roll wins. If both rolls are equal, the game is a draw.

        Args:
            p1: The first player.
            p2: The second player.
            **kwargs: Additional parameters, not used by this mode.

        Returns:
            A Game object containing the result of the dice game.
        """
        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))

        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None

        description = f"{p1.username} rolled {d1}, {p2.username} rolled {d2}"

        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description=description,
            timestamp=datetime.now()
        )