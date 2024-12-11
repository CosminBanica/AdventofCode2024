"""
Solver for day 7: Bridge Repair
"""
import operator
import math
from src.day_management.day_solver import DaySolver

def result_of_concat(result, ending):
    result = str(result)
    ending = str(ending)
    return result.endswith(ending)

def remove_concat(result, ending):
    result = str(result)
    ending = str(ending)
    index = result.rfind(ending)

    new_result = result[:index]

    if new_result == "":
        return 0

    return int(new_result)

class Day7Solver(DaySolver):
    """
    Solver for day 7: Bridge Repair
    """
    def __init__(self, input_data):
        self.operands = [operator.sub, operator.truediv]
        super().__init__(input_data)

    def is_query_possible(self, query):
        q = [query]

        while q:
            nr, component = q.pop()

            for op in self.operands:
                last_index = len(component) - 1
                new_nr = op(nr, component[last_index])

                if abs(new_nr - math.floor(new_nr)) != 0.0:
                    continue

                if new_nr == 0 and last_index == 0:
                    return True

                if new_nr == 0 and last_index != 0:
                    continue

                if new_nr < 0:
                    continue

                if last_index == 0 and new_nr != 0:
                    continue

                if new_nr < component[last_index - 1]:
                    continue

                q.insert(0, (new_nr, component[:-1]))

        return False

    def is_query_possible_concat(self, query):
        q = [query]

        while q:
            nr, component = q.pop()

            for op in self.operands:
                last_index = len(component) - 1
                new_nr = op(nr, component[last_index])

                if abs(new_nr - math.floor(new_nr)) != 0.0:
                    continue

                new_nr = int(new_nr)

                if new_nr == 0 and last_index == 0:
                    return True

                if new_nr == 0 and last_index != 0:
                    continue

                if new_nr < 0:
                    continue

                if last_index == 0 and new_nr != 0:
                    continue

                if new_nr < component[last_index - 1]:
                    continue

                q.insert(0, (new_nr, component[:-1]))

            if result_of_concat(nr, component[-1]):
                new_nr = remove_concat(nr, component[-1])

                if new_nr == 0:
                    return True

                if len(component) > 1:
                    q.insert(0, (new_nr, component[:-1]))

        return False

    def solve_part_one(self):
        """
        Solves part one
        """
        queries = []
        for line in self.input_data:
            nr, components = line.split(":")
            nr = int(nr)
            components = components.strip().split(" ")
            components = [int(component) for component in components]
            queries.append((nr, components))

        possible_nrs = []
        for query in queries:
            is_possible = self.is_query_possible(query)
            if is_possible:
                possible_nrs.append(query[0])

        return sum(possible_nrs)

    def solve_part_two(self):
        """
        Solves part two
        """
        queries = []
        for line in self.input_data:
            nr, components = line.split(":")
            nr = int(nr)
            components = components.strip().split(" ")
            components = [int(component) for component in components]
            queries.append((nr, components))

        possible_nrs = []
        for query in queries:
            is_possible = self.is_query_possible_concat(query)
            if is_possible:
                possible_nrs.append(query[0])

        return sum(possible_nrs)
