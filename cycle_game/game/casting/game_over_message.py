import constants
from game.casting.actor import Actor


class GameOver(Actor):
    """
    Displays a Game Over Message
    """
    def __init__(self):
        "Constructs a game over message."
        super().__init__()
        self._color = constants.GREEN

    def get_color(self):
        """Gets the actor's color and returns that color (r, g, b)."""
        return super().get_color()

    def set_color(self, color):
        """Updates the color to the given one."""
        return super().set_color(color)