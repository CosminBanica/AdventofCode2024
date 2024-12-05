"""
This module contains the DayPicker class.
"""
from src.day5.day5_solver import Day5Solver
from src.day4.day4_solver import Day4Solver
from src.day3.day3_solver import Day3Solver
from src.day2.day2_solver import Day2Solver
from src.day1.day1_solver import Day1Solver

day_solver_map = {
    5: Day5Solver,
    4: Day4Solver,
    3: Day3Solver,
    2: Day2Solver,
    1: Day1Solver,
}


def get_input_data(input_file_path):
    """
    Returns the input data from the input file
    """
    input_data = []
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            input_data.append(line.strip())
    return input_data


def get_day_solver(day, input_file_path):
    """
    Returns the day class based on the day number
    """
    if day in day_solver_map:
        return day_solver_map[day](get_input_data(input_file_path))

    return None