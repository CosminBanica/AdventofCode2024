"""
Solver for day 9: Disk Fragmenter
"""
from src.day_management.day_solver import DaySolver


class Day9Solver(DaySolver):
    """
    Solver for day 9: Disk Fragmenter
    """
    def get_initial_line(self):
        initial_line = []
        curr_id = 0
        is_file = True
        input_data = self.input_data[0]

        for char in input_data:
            if is_file:
                for i in range(int(char)):
                    initial_line.append(curr_id)

                curr_id += 1
            else:
                for i in range(int(char)):
                    initial_line.append('.')

            is_file = not is_file

        return initial_line

    def get_initial_sizes(self):
        initial_files, initial_empty = [], []
        curr_id = 0
        current_pos = 0
        is_file = True
        input_data = self.input_data[0]

        for char in input_data:
            if is_file:
                initial_files.append((current_pos, curr_id, int(char)))
                curr_id += 1
            else:
                initial_empty.append((current_pos, int(char)))

            current_pos += int(char)
            is_file = not is_file

        return initial_files, initial_empty


    def get_final_line(self, initial_line):
        final_line = []

        left = 0
        right = len(initial_line) - 1

        while left < right:
            final_line.append(initial_line[left])

            if final_line[left] == '.':
                while initial_line[right] == '.':
                    right -= 1

                if left >= right:
                    break

                final_line[left] = initial_line[right]
                initial_line[right] = '.'

            left += 1

        return final_line

    def get_final_files(self, initial_files, initial_empty):
        final_files = []
        last_file_id = initial_files[-1][1]

        # Get a dict of file positions in the list
        file_positions = {}
        for i in range(len(initial_files)):
            file_positions[initial_files[i][1]] = i

        # Go through the files in reverse
        for i in range(last_file_id, -1, -1):
            pos = file_positions[i]
            file = initial_files[pos]

            moved_file = False
            # Go through empty spaces to find one which fits
            for j in range(len(initial_empty)):
                empty_space = initial_empty[j]

                remaining_space = empty_space[1] - file[2]
                if remaining_space >= 0:
                    if remaining_space == 0:
                        initial_empty.pop(j)
                    else:
                        initial_empty[j] = (empty_space[0] + file[2], remaining_space)

                    initial_files.pop(pos)
                    final_files.append((empty_space[0], file[1], file[2]))
                    moved_file = True
                    break

            if not moved_file:
                final_files.append(file)

        return final_files

    def get_checksum(self, final_line):
        res = 0
        for i, nr in enumerate(final_line):
            res += i * nr

        return res

    def solve_part_one(self):
        """
        Solves part one
        """
        initial_line = self.get_initial_line()

        final_line = self.get_final_line(initial_line)

        return self.get_checksum(final_line)

    def solve_part_two(self):
        """
        Solves part two
        """
        initial_files, initial_empty = self.get_initial_sizes()

        final_files = self.get_final_files(initial_files, initial_empty)

        checksum = 0
        for file in final_files:
            for i in range(file[2]):
                checksum += file[1] * (file[0] + i)

        return checksum
