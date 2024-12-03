"""
Solver for day 3: Mull It Over
"""
import re
from src.day_management.day_solver import DaySolver


class Day3Solver(DaySolver):
    """
    Solver for day 3: Mull It Over
    """
    def __init__(self, input_data):
        self.do = True
        super().__init__(input_data)

    def get_mul_result(self, command_line):
        # Find all instances in string "command_line" that respect the
        # pattern "mul(X,Y)" where X and Y are integers of up to 3 digits
        # and return the list of matches
        mul_matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', command_line)
        mul_result = 0
        for match in mul_matches:
            mul_result += int(match[0]) * int(match[1])
        return mul_result

    def get_mul_result_with_ifs(self, command_line):
        # Find all instances in string "command_line" that respect one of these 3 paterns:
        # "mul(X,Y)" where X and Y are integers of up to 3 digits
        # "do()"
        # "don't()"
        # and return the list of matches
        # Find them using the same pattern, but with the 3 options, so that the order remains the same
        mul_matches = re.findall(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', command_line)

        mul_result = 0
        # print(mul_matches)
        for match in mul_matches:
            if match[0].startswith('mul') and self.do:
                mul_result += int(match[1]) * int(match[2])
                # print(mul_result)
            elif match[0] == 'do()':
                self.do = True
            elif match[0] == 'don\'t()':
                self.do = False

        return mul_result

    def solve_part_one(self):
        """
        Solves part one
        """
        command_lines = []
        for line in self.input_data:
            command_lines.append(line)

        mul_results = 0
        for command_line in command_lines:
            mul_results += self.get_mul_result(command_line)

        return mul_results

    def solve_part_two(self):
        """
        Solves part two
        """
        command_lines = []
        for line in self.input_data:
            command_lines.append(line)

        mul_results = 0
        for command_line in command_lines:
            mul_results += self.get_mul_result_with_ifs(command_line)

        return mul_results
