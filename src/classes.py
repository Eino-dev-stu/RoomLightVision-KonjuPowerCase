from datetime import datetime

class Room:
    def __init__(self, name):
        self.name = name
        self.lights = {
            "bedroom": False,
            "bathroom": False,
            "livingroom": False
        }
        
        self.usage_log = [] #add logging for light changes requested in REQ-id10

    def toggle(self, light): #REQ-id4: Toggle a specific light in the room off or on
        if light in self.lights:
            self.lights[light] = not self.lights[light] 
            self._log_event(light, self.lights[light])  ##REQ-id10 collect data

    def set_all(self, state: bool): # REQ-id4: Toggle all lights in the room on or off
        for key in self.lights:
            self.lights[key] = state

    def show(self, is_active=False): 
        mark = ">> " if is_active else "   "
        print(f"{mark}Room: {self.name}")
        for name, state in self.lights.items(): # REQ-id5: Show the status of all lights in the room
            print(f"    {name}: {'ON' if state else 'OFF'}")
            

    def _log_event(self, light_name, state): ## REQ-id10: Internal logging of light changes for analytics
        """Internal helper to record usage."""
        self.usage_log.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "light": light_name,
            "action": "ON" if state else "OFF"
        })
    def get_report(self):  ##REQ-id 10 method to retrieve the usage log for light use
        
        return self.usage_log

class Floor:
    def __init__(self):
        self.rooms = {
            "room1": Room("room1"),
            "room2": Room("room2")
        }
        self.current_room = "room1"

    def switch_room(self, room_name): #REQ-id4: allows admin switching between rooms on the floor
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

        