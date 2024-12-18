"""
Solver for day 14: Restroom Redoubt
"""
from src.day_management.day_solver import DaySolver

MAX_X = 101
MAX_Y = 103

class Day14Solver(DaySolver):
    """
    Solver for day 14: Restroom Redoubt
    """
    def get_robots(self):
        robots = []
        for line in self.input_data:
            pos, vector = line.strip().split(" ")
            pos = pos.split("=")[1].split(",")
            vector = vector.split("=")[1].split(",")
            robot = {"pos":(int(pos[0]), int(pos[1])), "vec":(int(vector[0]), int(vector[1]))}
            robots.append(robot)

        return robots

    def belonging_quadrant(self, pos):
        x, y = pos

        if x < (MAX_X // 2) and y < (MAX_Y // 2):
            return 0
        elif x > (MAX_X // 2) and y < (MAX_Y // 2):
            return 1
        elif x < (MAX_X // 2) and y > (MAX_Y // 2):
            return 2
        elif x > (MAX_X // 2) and y > (MAX_Y // 2):
            return 3

        return None

    def get_final_pos(self, robot, steps):
        x = (robot["pos"][0] + robot["vec"][0] * steps) % MAX_X
        y = (robot["pos"][1] + robot["vec"][1] * steps) % MAX_Y

        return x, y

    def get_quadrants_count(self, robots):
        quadrants_count = [0, 0, 0, 0]

        for robot in robots:
            final_pos = self.get_final_pos(robot, 100)
            belonging_quadrant = self.belonging_quadrant(final_pos)
            # print(f"Final_pos: {final_pos}, quadrant: {belonging_quadrant}")
            if belonging_quadrant is None:
                continue
            quadrants_count[belonging_quadrant] += 1

        # print(quadrants_count)

        return quadrants_count


    def solve_part_one(self):
        """
        Solves part one
        """
        robots = self.get_robots()

        quadrants = self.get_quadrants_count(robots)

        res = 1

        for quadrant in quadrants:
            res *= quadrant

        return res

    def solve_part_two(self):
        """
        Solves part two
        """
        return 0
