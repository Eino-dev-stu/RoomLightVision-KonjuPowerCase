from classes import Room, Floor



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
        print("  exit with q")

        cmd = input(">> ").lower()

        if cmd == "q":
            print(f"\n[LOGOUT] Session for '{user}' ended.") ## REQ-id3: secure Logout functionality for both admins and guests, ensuring secure access control and session management.
            print("Access Terminated. Returning to login screen...")
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
        print("  exit with q")

        cmd = input(">> ").lower()

        if cmd == "q":
            print(f"\n[LOGOUT] Session for '{user}' ended.") ## REQ-id3: secure Logout functionality for both admins and guests, ensuring secure access control and session management.
            print("Access Terminated. Returning to login screen...")
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
if __name__ == "__main__":
    floor = Floor()
    while True: # Keep the system running for the next user
        
        user, info = None, None   ## reset user info for new login attempt REQ-id3: secure Logout functionality for both admins and guests, ensuring secure access control and session management.
        while not user: ## user authentication loop, keeps asking for login until successful
            user, info = login()

        ## choose interface based on user role
        
        if info["role"] == "admin":  
            admin_loop(floor, user, info) # REQ-id4: Admin can control all rooms, guest can only control their room.
        else:
            guest_loop(floor, user, info) # REQ-id1: Guest can only control their assigned room, not the entire floor or the other rooms.
        