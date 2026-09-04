from abc import ABC, abstractmethod

from business_object.game import Game
from business_object.player import Player


class GameMode(ABC):
    """Abstract base class for all game modes."""

    @abstractmethod
    def play(self, p1: Player, p2: Player, **kwargs) -> Game:
        """
        Play a game between two players.

        Args:
            p1: The first player.
            p2: The second player.
            **kwargs: Additional parameters required by the game mode.

        Returns:
            The Game object containing the result.
        """
        pass