from business_object.game import Game
from business_object.game_mode_factory import GameModeFactory
from business_object.scoring_strategy import ScoringStrategy
from dao.player_dao import PlayerDao


class GameService:
    """Service responsible for playing games."""

    def play(
        self,
        player_id: int,
        opponent_id: int,
        game_mode: str,
        **kwargs
    ) -> Game:
        """
        Play a game between two players.

        Args:
            player_id: ID of the first player.
            opponent_id: ID of the second player.
            game_mode: Identifier of the game mode.
            **kwargs: Additional parameters required by the game mode.

        Returns:
            The Game object containing the result.
        """
        # Find players
        p1 = PlayerDao().find_by_id(player_id)
        p2 = PlayerDao().find_by_id(opponent_id)

        # Get the appropriate game mode
        mode = GameModeFactory.get_mode(game_mode)

        # Play the game
        game = mode.play(p1, p2, **kwargs)

        # Update Elo ratings
        scoring_strategy = ScoringStrategy()
        scoring_strategy.update_player_ratings(game)

        # Return the game
        return game