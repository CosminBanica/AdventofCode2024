"""
Solver for day 12: Garden Groups
"""
from src.day_management.day_solver import DaySolver


class Day12Solver(DaySolver):
    """
    Solver for day 12: Garden Groups
    """
    def is_in_bounds(self, pos, garden_map):
        if 0 <= pos[0] < len(garden_map) and 0 <= pos[1] < len(garden_map[0]):
            return True
        else:
            return False

    def get_garden_map(self):
        garden_map = []
        for line in self.input_data:
            garden_row = []
            for char in line:
                garden_row.append(char)
            garden_map.append(garden_row)

        return garden_map

    def is_oob_or_diff_region(self, x, y, garden_map, region):
        if not self.is_in_bounds((x, y), garden_map):
            return True
        elif garden_map[x][y] != region:
            return True
        return False

    def get_corners(self, x, y, garden_map, region):
        """
        When I refer to plots surrounding the plot (x, y), I mean the plots to the left, right, up and down of it.
        - If up and right are same region as current region, and diagonal up-right is different, then +1 corner
        - If up and left are same region as current region, and diagonal up-left is different, then +1 corner
        - If down and right are same region as current region, and diagonal down-right is different, then +1 corner
        - If down and left are same region as current region, and diagonal down-left is different, then +1 corner
        - If up and right are different region than current region, then +1 corner
        - If up and left are different region than current region, then +1 corner
        - If down and right are different region than current region, then +1 corner
        - If down and left are different region than current region, then +1 corner
        """
        corners = 0
        # Check inner corners
        if self.is_oob_or_diff_region(x - 1, y + 1, garden_map, region) and not self.is_oob_or_diff_region(x - 1, y, garden_map, region) and not self.is_oob_or_diff_region(x, y + 1, garden_map, region):
            corners += 1
        if self.is_oob_or_diff_region(x - 1, y - 1, garden_map, region) and not self.is_oob_or_diff_region(x - 1, y, garden_map, region) and not self.is_oob_or_diff_region(x, y - 1, garden_map, region):
            corners += 1
        if self.is_oob_or_diff_region(x + 1, y + 1, garden_map, region) and not self.is_oob_or_diff_region(x + 1, y, garden_map, region) and not self.is_oob_or_diff_region(x, y + 1, garden_map, region):
            corners += 1
        if self.is_oob_or_diff_region(x + 1, y - 1, garden_map, region) and not self.is_oob_or_diff_region(x + 1, y, garden_map, region) and not self.is_oob_or_diff_region(x, y - 1, garden_map, region):
            corners += 1
        # Check outer corners
        if self.is_oob_or_diff_region(x - 1, y, garden_map, region) and self.is_oob_or_diff_region(x, y - 1, garden_map, region):
            corners += 1
        if self.is_oob_or_diff_region(x - 1, y, garden_map, region) and self.is_oob_or_diff_region(x, y + 1, garden_map, region):
            corners += 1
        if self.is_oob_or_diff_region(x + 1, y, garden_map, region) and self.is_oob_or_diff_region(x, y - 1, garden_map, region):
            corners += 1
        if self.is_oob_or_diff_region(x + 1, y, garden_map, region) and self.is_oob_or_diff_region(x, y + 1, garden_map, region):
            corners += 1

        return corners

    def get_regions(self, garden_map):
        regions = []
        visited = set()

        current_region = ""
        region_perims = []

        for i, line in enumerate(garden_map):
            for j, plot in enumerate(line):
                if current_region == "" and (i, j) not in visited:
                    current_region = plot
                    queue = [(i, j)]
                    visited.add((i, j))

                    while queue:
                        x, y = queue.pop()

                        plot_perimeter = 0
                        if self.is_in_bounds((x - 1, y), garden_map):
                            if garden_map[x - 1][y] != current_region:
                                plot_perimeter += 1
                            elif (x - 1, y) not in visited:
                                queue.append((x - 1, y))
                                visited.add((x - 1, y))
                        else:
                            plot_perimeter += 1
                        if self.is_in_bounds((x + 1, y), garden_map):
                            if garden_map[x + 1][y] != current_region:
                                plot_perimeter += 1
                            elif (x + 1, y) not in visited:
                                queue.append((x + 1, y))
                                visited.add((x + 1, y))
                        else:
                            plot_perimeter += 1
                        if self.is_in_bounds((x, y - 1), garden_map):
                            if garden_map[x][y - 1] != current_region:
                                plot_perimeter += 1
                            elif (x, y - 1) not in visited:
                                queue.append((x, y - 1))
                                visited.add((x, y - 1))
                        else:
                            plot_perimeter += 1
                        if self.is_in_bounds((x, y + 1), garden_map):
                            if garden_map[x][y + 1] != current_region:
                                plot_perimeter += 1
                            elif (x, y + 1) not in visited:
                                queue.append((x, y + 1))
                                visited.add((x, y + 1))
                        else:
                            plot_perimeter += 1

                        nr_sides = self.get_corners(x, y, garden_map, current_region)

                        # print(f"Plot {current_region} ({x}, {y}) has {nr_sides} sides")
                        region_perims.append((plot_perimeter, nr_sides))

                    regions.append((current_region, region_perims))
                    current_region = ""
                    region_perims = []

        return regions

    def solve_part_one(self):
        """
        Solves part one
        """
        garden_map = self.get_garden_map()

        regions = self.get_regions(garden_map)

        result = 0
        for region in regions:
            region_perimeter = 0
            for plot in region[1]:
                region_perimeter += plot[0]
            result += region_perimeter * len(region[1])

        return result

    def solve_part_two(self):
        """
        Solves part two
        """
        garden_map = self.get_garden_map()

        regions = self.get_regions(garden_map)

        result = 0
        for region in regions:
            region_sides = 0
            for plot in region[1]:
                region_sides += plot[1]
            result += region_sides * len(region[1])
            # print(f"Region {region[0]}: {len(region[1])} plots, {region_sides} sides")

        return result
