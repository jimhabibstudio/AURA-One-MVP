# backend/procedural_generator.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from helpers import calculate_grid_dimensions, assign_colors  # simplified imports after sys.path fix

def generate_floor_plan(rooms):
    fig, ax = plt.subplots(figsize=(8, 6))
    n = len(rooms)
    rows, cols = calculate_grid_dimensions(n)
    colors = assign_colors(n)

    width, height = 10, 8
    room_w = width / cols
    room_h = height / rows

    for idx, room in enumerate(rooms):
        row = idx // cols
        col = idx % cols
        x = col * room_w
        y = height - (row + 1) * room_h
        rect = patches.Rectangle((x, y), room_w, room_h, linewidth=1, edgecolor='black', facecolor=colors[idx % len(colors)])
        ax.add_patch(rect)
        ax.text(x + room_w / 2, y + room_h / 2, room, fontsize=9, ha='center', va='center')

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig
