"""
Solver for day 4: Ceres Search
"""
from src.day_management.day_solver import DaySolver


class Day4Solver(DaySolver):
    """
    Solver for day 4: Ceres Search
    """
    def get_horizontal_lines(self):
        return self.input_data

    def get_vertical_lines(self):
        vertical_lines = []
        num_columns = len(self.input_data[0])

        for col in range(num_columns):
            vertical_line = ""

            for row in self.input_data:
                vertical_line += row[col]

            vertical_lines.append(vertical_line)

        return vertical_lines

    def get_diagonal_lines(self):
        diagonal_lines = []
        num_rows = len(self.input_data)
        num_columns = len(self.input_data[0])

        # Top-left to bottom-right diagonals
        for start in range(num_rows + num_columns - 1):
            diagonal = ""
            for row in range(max(0, start - num_columns + 1), min(start + 1, num_rows)):
                col = start - row
                if col < num_columns:
                    diagonal += self.input_data[row][col]
            if diagonal:
                diagonal_lines.append(diagonal)

        # Top-right to bottom-left diagonals
        for start in range(num_rows + num_columns - 1):
            diagonal = ""
            for row in range(max(0, start - num_columns + 1), min(start + 1, num_rows)):
                col = num_columns - 1 - (start - row)
                if col >= 0:
                    diagonal += self.input_data[row][col]
            if diagonal:
                diagonal_lines.append(diagonal)

        return diagonal_lines

    def get_blocks(self):
        blocks = []
        num_rows = len(self.input_data)
        num_columns = len(self.input_data[0])

        # Iterate through each possible top-left corner of a 3x3 block
        for row in range(num_rows - 2):
            for col in range(num_columns - 2):
                block = [
                    [self.input_data[row + i][col + j] for j in range(3)]
                    for i in range(3)
                ]
                blocks.append(block)

        return blocks

    def get_nr_occurences(self, strings, word):
        matches = 0
        for string in strings:
            matches += string.count(word)
        return matches

    def get_nr_crosses(self, blocks):
        count = 0
        target_words = {"MAS", "SAM"}

        for block in blocks:
            # Extract the main diagonals
            main_diagonal = [block[i][i] for i in range(3)]
            anti_diagonal = [block[i][2 - i] for i in range(3)]

            # Check if either diagonal contains "MAS" or "SAM"
            if "".join(main_diagonal) in target_words and "".join(anti_diagonal) in target_words:
                count += 1

        return count

    def solve_part_one(self):
        """
        Solves part one
        """
        horizontal_lines = self.get_horizontal_lines()
        vertical_lines = self.get_vertical_lines()
        diagonal_lines = self.get_diagonal_lines()

        words_found = self.get_nr_occurences(horizontal_lines, "XMAS")
        words_found += self.get_nr_occurences(horizontal_lines, "SAMX")
        words_found += self.get_nr_occurences(vertical_lines, "XMAS")
        words_found += self.get_nr_occurences(vertical_lines, "SAMX")
        words_found += self.get_nr_occurences(diagonal_lines, "XMAS")
        words_found += self.get_nr_occurences(diagonal_lines, "SAMX")

        return words_found

    def solve_part_two(self):
        """
        Solves part two
        """
        blocks = self.get_blocks()

        count = self.get_nr_crosses(blocks)

        return count
