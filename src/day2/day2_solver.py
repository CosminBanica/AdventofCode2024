"""
Solver for day 2: Red-Nosed Reports
"""
from src.day_management.day_solver import DaySolver


class Day2Solver(DaySolver):
    """
    Solver for day 2: Red-Nosed Reports
    """
    def is_diff_good(self, a, b, is_asc, max_diff=3):
        diff = b - a
        if diff == 0:
            return False

        if is_asc and diff < 0:
            return False

        if not is_asc and diff > 0:
            return False

        if abs(diff) > max_diff:
            return False

        return True

    def is_safe(self, report, max_diff=3, max_tolerance=0):
        report = report.split()
        report = [int(x) for x in report]
        first_diff = report[1] - report[0]

        i = 1
        is_asc = first_diff > 0
        if first_diff == 0 or abs(first_diff) > max_diff:
            if max_tolerance == 0:
                return False
            max_tolerance -= 1
            second_diff = report[2] - report[0]
            if second_diff == 0 or abs(second_diff) > max_diff:
                third_diff = report[2] - report[1]
                if third_diff == 0 or abs(third_diff) > max_diff:
                    return False
                else:
                    is_asc = third_diff > 0
                    report.pop(0)
            else:
                is_asc = second_diff > 0
                report.pop(1)

        while i < len(report) - 1:
            is_diff_good = self.is_diff_good(report[i], report[i + 1], is_asc, max_diff)
            if not is_diff_good:
                if max_tolerance == 0:
                    return False
                max_tolerance -= 1

                is_diff_good = self.is_diff_good(report[i - 1], report[i + 1], is_asc, max_diff)
                if not is_diff_good:
                    if i + 2 >= len(report):
                        return True
                    is_diff_good = self.is_diff_good(report[i], report[i + 2], is_asc, max_diff)
                    if not is_diff_good:
                        return False
                    else:
                        report.pop(i + 1)
                else:
                    report.pop(i)
                    i -= 1
            i += 1

        return True

    def get_unsafe_reports(self, reports, max_diff=3, max_tolerance=0):
        safe_reports = 0

        for report in reports:
            if self.is_safe(report, max_diff, max_tolerance):
                safe_reports += 1

        return safe_reports

    def solve_part_one(self):
        """
        Solves part one
        """
        reports = []
        for line in self.input_data:
            reports.append(line)

        safe_reports = self.get_unsafe_reports(reports)
        return safe_reports

    def solve_part_two(self):
        """
        Solves part two
        """
        reports = []
        for line in self.input_data:
            reports.append(line)

        safe_reports = self.get_unsafe_reports(reports, max_tolerance=1)
        return safe_reports
