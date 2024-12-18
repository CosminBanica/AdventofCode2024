"""
This module contains the DayPicker class.
"""
from src.day14.day14_solver import Day14Solver
from src.day13.day13_solver import Day13Solver
from src.day12.day12_solver import Day12Solver
from src.day11.day11_solver import Day11Solver
from src.day10.day10_solver import Day10Solver
from src.day9.day9_solver import Day9Solver
from src.day8.day8_solver import Day8Solver
from src.day7.day7_solver import Day7Solver
from src.day6.day6_solver import Day6Solver
from src.day5.day5_solver import Day5Solver
from src.day4.day4_solver import Day4Solver
from src.day3.day3_solver import Day3Solver
from src.day2.day2_solver import Day2Solver
from src.day1.day1_solver import Day1Solver

day_solver_map = {
    14: Day14Solver,
    13: Day13Solver,
    12: Day12Solver,
    11: Day11Solver,
    10: Day10Solver,
    9: Day9Solver,
    8: Day8Solver,
    7: Day7Solver,
    6: Day6Solver,
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