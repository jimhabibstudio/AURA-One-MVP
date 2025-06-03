# backend/procedural_generator.py
"""
Procedural Room Generator for AURA One MVP.
Takes a list of room names and creates simple spatial layout data.
"""

ROOM_DATABASE = {
    "living_room": {"width": 4, "height": 5},
    "bedroom": {"width": 3, "height": 4},
    "kitchen": {"width": 3, "height": 3},
    "bathroom": {"width": 2, "height": 2},
    "dining_room": {"width": 3, "height": 3},
    "study": {"width": 3, "height": 3},
    "toilet": {"width": 1.5, "height": 2},
    "laundry": {"width": 2, "height": 2},
    "storage": {"width": 2, "height": 2},
    "corridor": {"width": 1, "height": 4}
}

def procedural_floorplan(room_list):
    """
    Accepts a list of room types (e.g., [\"living_room\", \"bedroom\", \"kitchen\"])
    Returns a layout plan with x/y coordinates and sizes.
    """
    layout = []
    x_cursor = 0
    y_cursor = 0
    row_height = 0
    max_width = 15

    for room in room_list:
        if room not in ROOM_DATABASE:
            continue

        room_data = ROOM_DATABASE[room]
        width = room_data["width"]
        height = room_data["height"]

        # Move to next row if current row is full
        if x_cursor + width > max_width:
            x_cursor = 0
            y_cursor += row_height + 1
            row_height = 0

        layout.append({
            "name": room,
            "x": x_cursor,
            "y": y_cursor,
            "width": width,
            "height": height,
            "area": width * height
        })

        x_cursor += width + 1  # Add gap between rooms
        row_height = max(row_height, height)

    return layout
