"""
Solver for day 13: Claw Contraption
"""
from heapq import heappush, heappop
from math import gcd
from src.day_management.day_solver import DaySolver

TOKENS_A = 3
TOKENS_B = 1

class Day13Solver(DaySolver):
    """
    Solver for day 13: Claw Contraption
    """
    def get_machines(self):
        """
        Input is text like:
        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400

        Button A: X+26, Y+66
        Button B: X+67, Y+21
        Prize: X=12748, Y=12176

        etc.
        """
        machines = []
        machine = {}
        for line in self.input_data:
            if line == "":
                machines.append(machine)
                machine = {}
            else:
                if "Prize" not in line:
                    parts = line.split(": ")
                    button = parts[0].split(" ")[1]
                    x, y = parts[1].split(", ")
                    x = int(x.split("+")[1])
                    y = int(y.split("+")[1])
                    machine[button] = {"x": x, "y": y}
                else:
                    x, y = line.split(", ")
                    x = int(x.split("=")[1])
                    y = int(y.split("=")[1])
                    machine["prize"] = {"x": x, "y": y}
        machines.append(machine)
        return machines

    def get_tokens(self, machine):
        """
        Get the minimum number of tokens needed to reach the prize
        Start at 0, 0 and objective is to reach prize coords
        Looking at example:
        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400

        Each press of button A moves you +94 on x and +34 on y
        Each press of button B moves you +22 on x and +67 on y
        Each press of button A costs 3 tokens
        Each press of button B costs 1 token
        Return the minimum number of tokens needed to reach the prize
        If it's impossible to reach the prize, return 0
        If the prize can't be reached in 100 presses of button A and 100 presses of button B, return 0
        """
        prize_x = machine["prize"]["x"]
        prize_y = machine["prize"]["y"]
        button_a_x = machine["A"]["x"]
        button_a_y = machine["A"]["y"]
        button_b_x = machine["B"]["x"]
        button_b_y = machine["B"]["y"]

        for i in range(101):
            for j in range(101):
                if prize_x == i * button_a_x + j * button_b_x and prize_y == i * button_a_y + j * button_b_y:
                    return i * TOKENS_A + j * TOKENS_B

        return 0

    def get_tokens_two(self, machine):
        """
        Get the minimum number of tokens needed to reach the prize
        Different from get_tokens in that the prize coords are increased by 10000000000000
        So it will take much more presses to reach the prize
        This means we can't just check 101 presses of button A and 101 presses of button B
        We have to do a smarter approach
        Start at 0, 0 and objective is to reach prize coords
        Looking at example:
        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=10000000008400, Y=10000000005400

        Each press of button A moves you +94 on x and +34 on y
        Each press of button B moves you +22 on x and +67 on y
        Each press of button A costs 3 tokens
        Each press of button B costs 1 token
        Return the minimum number of tokens needed to reach the prize
        If it's impossible to reach the prize, return 0
        """
        prize_x = machine["prize"]["x"]
        prize_y = machine["prize"]["y"]
        button_a_x = machine["A"]["x"]
        button_a_y = machine["A"]["y"]
        button_b_x = machine["B"]["x"]
        button_b_y = machine["B"]["y"]

        b = (prize_x * button_a_y - prize_y * button_a_x) // (button_b_x * button_a_y - button_b_y * button_a_x)
        a = (prize_x * button_b_y - prize_y * button_b_x) // (button_a_x * button_b_y - button_a_y * button_b_x)

        if button_a_x * a + button_b_x * b == prize_x and button_a_y * a + button_b_y * b == prize_y:
            return a * TOKENS_A + b * TOKENS_B

        return 0


    def solve_part_one(self):
        """
        Solves part one
        """
        machines = self.get_machines()

        total_tokens = 0

        for machine in machines:
            total_tokens += self.get_tokens(machine)

        return total_tokens

    def solve_part_two(self):
        """
        Solves part two
        """
        machines = self.get_machines()

        total_tokens = 0

        for machine in machines:
            machine["prize"]["x"] += 10000000000000
            machine["prize"]["y"] += 10000000000000
            total_tokens += self.get_tokens_two(machine)

        return total_tokens
