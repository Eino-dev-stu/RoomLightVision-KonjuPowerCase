class Room:
    def __init__(self, name):
        self.name = name
        self.lights = {
            "bedroom": False,
            "bathroom": False,
            "livingroom": False
        }

    def toggle(self, light): #REQ-id4: Toggle a specific light in the room off or on
        if light in self.lights:
            self.lights[light] = not self.lights[light] 

    def set_all(self, state: bool): # REQ-id4: Toggle all lights in the room on or off
        for key in self.lights:
            self.lights[key] = state

    def show(self, is_active=False): 
        marker = "Give command:" if is_active else "  "
        print(f"\n{marker} {self.name}")
        for name, state in self.lights.items(): # REQ-id5: Show the status of all lights in the room
            print(f"    {name}: {'ON' if state else 'OFF'}")


class Floor:
    def __init__(self):
        self.rooms = {
            "room1": Room("room1"),
            "room2": Room("room2")
        }
        self.current_room = "room1"

    def switch_room(self, room_name): #REQ-id4: allows switching between rooms on the floor
        if room_name in self.rooms:
            self.current_room = room_name
        else:
            print("Room not found")

    def current(self):
        return self.rooms[self.current_room]

    def set_all_floor(self, state: bool): # REQ-id4: Toggle all lights in all rooms on the floor on or off
        for room in self.rooms.values():
            room.set_all(state)

    def show(self):
        print("\n=== FLOOR ===")
        print(f"Active room: {self.current_room}")

        for name, room in self.rooms.items():
            room.show(is_active=(name == self.current_room))

        print("\nCommands:")
        print("  switch room1 / room2")
        print("  bedroom / bathroom / livingroom")
        print("  room_on / room_off")
        print("  floor_on / floor_off")
        print("  q")