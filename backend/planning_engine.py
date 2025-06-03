# backend/planning_engine.py

import random

class Room:
    def __init__(self, name, min_size, max_size, adjacency=None):
        self.name = name
        self.size = random.randint(min_size, max_size)
        self.adjacency = adjacency or []

class FloorPlan:
    def __init__(self, rooms):
        self.rooms = rooms
        self.layout = []

    def generate_layout(self):
        placed = []
        for room in self.rooms:
            if not placed:
                self.layout.append((room.name, (0, 0)))  # place first room at origin
                placed.append(room.name)
            else:
                # Try to place adjacent to any existing room
                ref_room = random.choice(placed)
                x, y = self._find_next_location()
                self.layout.append((room.name, (x, y)))
                placed.append(room.name)

    def _find_next_location(self):
        # Naive version for now
        return (random.randint(1, 10) * 3, random.randint(1, 10) * 3)

    def export_layout(self):
        return self.layout

# Step 1: Define architectural zoning rules
def classify_zones(room_list):
    public = ['living room', 'dining room']
    private = ['bedroom', 'study']
    service = ['kitchen', 'bathroom', 'store']

    zones = {'Public': [], 'Private': [], 'Service': []}

    for room in room_list:
        rl = room.lower()
        if rl in public:
            zones['Public'].append(room)
        elif rl in private:
            zones['Private'].append(room)
        else:
            zones['Service'].append(room)

    return zones

# Step 2: Build rooms with logic
def build_room_objects(zones):
    room_objects = []
    for zone, rooms in zones.items():
        for room in rooms:
            min_size = 9 if 'bath' in room.lower() else 12
            max_size = 25 if 'living' in room.lower() else 16
            room_objects.append(Room(room, min_size, max_size))
    return room_objects

# Step 3: Plan and export layout
def plan_floor_plan(user_prompt):
    # Parse and classify
    room_names = [r.strip() for r in user_prompt.split(',')]
    zones = classify_zones(room_names)
    room_objs = build_room_objects(zones)

    # Generate layout
    plan = FloorPlan(room_objs)
    plan.generate_layout()
    return plan.export_layout()
