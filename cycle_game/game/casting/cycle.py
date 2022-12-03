import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Cycle(Actor):
    def __init__(self, position):
        """Constructs a new tron cycle """
        super().__init__()

        self._segments = []
        self._color = Color(255, 255, 255)
        self._prepare_cycle(position)
        self._name = ""

    def get_segments(self):
        """Gets the segments for each cycle."""
        return self._segments

    def get_name(self):
        """Gets the players name."""
        return self._name

    def move_next(self):
        """Moves the actor to its next position according to its velocity."""

        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        """
        Gets the first actor from _segments.
        """
        return self._segments[0]

    def wall(self, game_over):
        """
        Builds the wall for each cycle.
        """
        wall = self._segments[-1]
        velocity = wall.get_velocity()
        offset = velocity.reverse()
        position = wall.get_position().add(offset)

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        if not game_over:
            segment.set_color(self._color)
        else:
            segment.set_color(constants.WHITE)
        self._segments.append(segment)

    def turn_cycle(self, velocity):
        """Changes the direction for a cycle by changing the velocity.
        """

        self._segments[0].set_velocity(velocity)

    def _prepare_cycle(self, position):
        """Constructs a new cycle.
        """
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "O" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)

    def set_cycle_color(self, color):
        """
        Sets the color for each segment of a cycle.
        """

        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)

    def set_name(self, name):
        """
        Sets the name of the user.
        """
        self._name = name