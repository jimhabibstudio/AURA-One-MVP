# utils/helpers.py

"""
Helper utilities for geometric layout and spacing.
Useful for extending the procedural layout generation with reusable functions.
"""

def calculate_grid_dimensions(n_rooms):
    """
    Calculate an approximate square layout (rows x cols) for N rooms.

    Args:
        n_rooms (int): Total number of rooms

    Returns:
        (int, int): rows, cols
    """
    import math
    cols = math.ceil(math.sqrt(n_rooms))
    rows = math.ceil(n_rooms / cols)
    return rows, cols


def assign_colors(n):
    """
    Generate distinct colors for each room.

    Args:
        n (int): Number of rooms

    Returns:
        List[str]: List of color hex codes or names
    """
    import matplotlib.pyplot as plt
    return plt.cm.tab20.colors[:n]
