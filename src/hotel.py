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



# --- USERS ---
users = {
    "admin": {"password": "admin", "role": "admin"},
    "guest1": {"password": "guest1", "role": "guest", "room": "room1"},
    "guest2": {"password": "guest2", "role": "guest", "room": "room2"},
}


 
# REQ-id8  password protected access and different levels of users: admin, guest. Admin can control all rooms, guest can only control their room.
#REQ-id11 prevents unauthorized access to the system, ensuring that only registered users can control the lights and manage the hotel rooms.
def login():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Logged in as {username}")
        return username, users[username]
    else:
        print("Invalid login, unauthorized access denied.")
        return None, None

# Running the hotel management system
# ADMIN INTERFACE 
def admin_loop(floor, user, info):
    while True:
        print(f"\n[ADMIN] {user}")
        floor.show()

        print("\nCommands:")
        print("  switch room1/room2")
        print("  bedroom / bathroom / livingroom")
        print("  room_on / room_off")
        print("  floor_on / floor_off")
        print("  q")

        cmd = input(">> ").lower()

        if cmd == "q":
            break
        elif cmd.startswith("switch"):
            _, room_name = cmd.split()
            floor.switch_room(room_name)

        elif cmd == "room_on":
            floor.current().set_all(True)
        elif cmd == "room_off":
            floor.current().set_all(False)

        elif cmd == "floor_on":
            floor.set_all_floor(True)
        elif cmd == "floor_off":
            floor.set_all_floor(False)

        elif cmd in floor.current().lights:
            floor.current().toggle(cmd)

        else:
            print("Invalid command")


#  GUEST INTERFACE 
def guest_loop(floor, user, info): 	## REQ-id1: Guest can only control their assigned room, not the entire floor or the other rooms.
    guest_room = info["room"]
    floor.switch_room(guest_room)

    while True:
        print(f"\n[GUEST] {user} (Room: {guest_room})")

    
        room = floor.current()
        room.show(is_active=True)

        print("\nCommands:")
        print("  bedroom / bathroom / livingroom")
        print("  room_on / room_off")
        print("  q")

        cmd = input(">> ").lower()

        if cmd == "q":
            break

        elif cmd == "room_on":
            room.set_all(True)
        elif cmd == "room_off":
            room.set_all(False)

        elif cmd in room.lights:
            room.toggle(cmd)

        else:
            print("Invalid command")


# --- RUN ---
floor = Floor()

user, info = None, None  ## user authentication loop, keeps asking for login until successful
while not user:
    user, info = login()

## choose interface based on user role
if info["role"] == "admin":  
    admin_loop(floor, user, info) # REQ-id4: Admin can control all rooms, guest can only control their room.
else:
    guest_loop(floor, user, info) # REQ-id1: Guest can only control their assigned room, not the entire floor or the other rooms.