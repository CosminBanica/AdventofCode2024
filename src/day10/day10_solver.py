"""
Solver for day 10: Hoof It
"""
from src.day_management.day_solver import DaySolver


class Day10Solver(DaySolver):
    """
    Solver for day 10: Hoof It
    """
    def get_hike_map_zeroes(self):
        hike_map = []
        zeroes = []

        for i, line in enumerate(self.input_data):
            map_line = []
            for j, char in enumerate(line):
                map_line.append(int(char))
                if char == '0':
                    zeroes.append((i, j))
            hike_map.append(map_line)

        return hike_map, zeroes

    def is_in_bounds(self, pos, hike_map):
        if 0 <= pos[0] < len(hike_map) and 0 <= pos[1] < len(hike_map[0]):
            return True
        else:
            return False

    def get_score(self, hike_map, start, distinct):
        score = 0
        visited = set()
        queue = [start]

        while queue:
            curr_pos = queue.pop()

            curr_nr = hike_map[curr_pos[0]][curr_pos[1]]

            if curr_nr == 9 and curr_pos not in visited and distinct:
                score += 1
                visited.add(curr_pos)
                continue
            elif curr_nr == 9 and not distinct:
                score += 1
                continue

            visited.add(curr_pos)

            next_positions = [
                (curr_pos[0] + 1, curr_pos[1]),
                (curr_pos[0] - 1, curr_pos[1]),
                (curr_pos[0], curr_pos[1] + 1),
                (curr_pos[0], curr_pos[1] - 1)
            ]

            for position in next_positions:
                if self.is_in_bounds(position, hike_map):
                    if position not in visited:
                        next_nr = hike_map[position[0]][position[1]]
                        if next_nr == curr_nr + 1:
                            queue.insert(0, position)

        return score

    def solve_part_one(self):
        """
        Solves part one
        """
        hike_map, zeroes = self.get_hike_map_zeroes()

        scores = []

        for zero in zeroes:
            scores.append(self.get_score(hike_map, zero, True))

        # print(scores)

        return sum(scores)

    def solve_part_two(self):
        """
        Solves part two
        """
        hike_map, zeroes = self.get_hike_map_zeroes()

        scores = []

        for zero in zeroes:
            scores.append(self.get_score(hike_map, zero, False))

        # print(scores)

        return sum(scores)
