from src.day_management.day_solver import DaySolver


class Day1Solver(DaySolver):
    """
    Solver for day 1: Historian Hysteria
    """
    def get_lists(self):
        list1 = []
        list2 = []
        for line in self.input_data:
            # First number goes to list1, second to list2
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))
        return list1, list2

    def get_freq_dicts(self):
        freq_dict1 = {}
        freq_dict2 = {}
        for line in self.input_data:
            # First number goes to list1, second to list2
            num1, num2 = line.split()
            if num1 not in freq_dict1:
                freq_dict1[num1] = 1
            else:
                freq_dict1[num1] += 1

            if num2 not in freq_dict2:
                freq_dict2[num2] = 1
            else:
                freq_dict2[num2] += 1

        return freq_dict1, freq_dict2

    def solve_part_one(self):
        list1, list2 = self.get_lists()
        list1 = sorted(list1)
        list2 = sorted(list2)

        diff_sum = 0
        for i in range(len(list1)):
            diff_sum += abs(list1[i] - list2[i])

        return diff_sum

    def solve_part_two(self):
        dict1, dict2 = self.get_freq_dicts()

        similarity = 0
        for key in dict1:
            if key not in dict2:
                continue
            similarity += dict1[key] * dict2[key] * int(key)

        return similarity
