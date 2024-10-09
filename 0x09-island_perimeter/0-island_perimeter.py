#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of an island in a grid.
    Args:
    grid (list of list of ints): A 2D grid representing the map

    Returns:
    int: The perimeter of the island.
    """
    # Initialize the perimeter to zero
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find land (1)
            if grid[r][c] == 1:
                # Check all four neighbors (top, bottom, left, right)

                # Check the top neighbor
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # Check the bottom neighbor
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1

                # Check the left neighbor
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1

                # Check the right neighbor
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
