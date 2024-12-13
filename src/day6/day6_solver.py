"""
Solver for day 6: Guard Gallivant
"""
from src.day_management.day_solver import DaySolver
from src.utils.enums import Direction


class Guard:
    """
    Guard class
    It represents a guard who can move forward only
    If faced with a solid wall, the guard will turn right
    The guard also has a map of the area
    The guard also stores the visited positions
    """
    def __init__(self, input_data):
        self.map = self.get_map(input_data)
        self.x, self.y, self.facing_direction = self.get_starting_position()
        self.visited = {(self.x, self.y)}

    def get_map(self, input_data):
        """
        Returns a map of the area
        """
        map = []
        for line in input_data:
            row = []
            for char in line:
                row.append(char)
            map.append(row)
        return map

    def get_starting_position(self):
        """
        Returns the starting position of the guard
        """
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == "^":
                    return x, y, Direction.UP
                if char == ">":
                    return x, y, Direction.RIGHT
                if char == "v":
                    return x, y, Direction.DOWN
                if char == "<":
                    return x, y, Direction.LEFT

    def move(self):
        """
        Moves the guard; return 0 if successful, 1 if out of bounds
        """
        new_position = self.get_new_position()
        if self.is_out_of_bounds(new_position[0], new_position[1]):
            return 1
        if self.map[new_position[1]][new_position[0]] == "#":
            self.facing_direction = self.turn_right()
            return 0
        self.x, self.y = new_position
        self.visited.add((self.x, self.y))
        return 0

    def place_obstructions(self):
        """
        Similar to move(); this time, start from the beginning again
        However, every time you encounter a spot where, if you would place
        an obstruction in front of the guard, the guard would get stuck
        in a loop, increase a counter
        """

    def turn_right(self):
        """
        Turns the guard to the right
        """
        if self.facing_direction == Direction.UP:
            return Direction.RIGHT
        elif self.facing_direction == Direction.RIGHT:
            return Direction.DOWN
        elif self.facing_direction == Direction.DOWN:
            return Direction.LEFT
        elif self.facing_direction == Direction.LEFT:
            return Direction.UP

    def is_out_of_bounds(self, x, y):
        """
        Returns True if the position is out of bounds
        """
        return x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map)

    def get_new_position(self):
        """
        Returns the new position of the guard
        """
        new_x, new_y = self.x, self.y
        if self.facing_direction == Direction.UP:
            new_y -= 1
        elif self.facing_direction == Direction.RIGHT:
            new_x += 1
        elif self.facing_direction == Direction.DOWN:
            new_y += 1
        elif self.facing_direction == Direction.LEFT:
            new_x -= 1
        return new_x, new_y

    def get_nr_of_visited_positions(self):
        """
        Returns the number of visited positions
        """
        return len(self.visited)


class Day6Solver(DaySolver):
    """
    Solver for day 6: Guard Gallivant
    """

    def solve_part_one(self):
        """
        Solves part one
        """
        guard = Guard(self.input_data)

        while True:
            if guard.move() == 1:
                break

        return guard.get_nr_of_visited_positions()

    def solve_part_two(self):
        """
        Solves part two
        """
        return 0
