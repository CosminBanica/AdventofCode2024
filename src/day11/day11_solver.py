"""
Solver for day 11: Plutonian Pebbles
"""
from collections import Counter
from src.day_management.day_solver import DaySolver


class Day11Solver(DaySolver):
    """
    Solver for day 11: Plutonian Pebbles
    """
    def split(self, stone):
        str_stone = str(stone)
        midpoint = len(str_stone) // 2

        return int(str_stone[:midpoint]), int(str_stone[midpoint:])

    def blink(self, stones):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stone_left, new_stone_right = self.split(stone)
                new_stones.append(new_stone_left)
                new_stones.append(new_stone_right)
            else:
                new_stones.append(stone * 2024)

        return new_stones

    def blink_one(self, stone):
        if stone == 0:
            return (1,)
        elif len(str(stone)) % 2 == 0:
            new_stone_left, new_stone_right = self.split(stone)
            return new_stone_left, new_stone_right
        return (stone * 2024,)

    def solve_part_one(self):
        """
        Solves part one
        """
        stones = self.input_data[0].strip().split(" ")
        stones = [int(stone) for stone in stones]

        for _ in range(25):
            stones = self.blink(stones)
            # print(stones)

        return len(stones)

    def solve_part_two(self):
        """
        Solves part two
        """
        stones = self.input_data[0].strip().split(" ")
        stones = [int(stone) for stone in stones]

        stones_count = Counter(stones)

        for _ in range(75):
            next_stones_count = Counter()
            for k, v in stones_count.items():
                if v == 0:
                    continue

                for stone in self.blink_one(k):
                    next_stones_count[stone] += v
            stones_count = next_stones_count

        return stones_count.total()
