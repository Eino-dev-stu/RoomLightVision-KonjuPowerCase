import pytest
from classes import Room, Floor
from hotel import admin_loop, guest_loop, login

#setup for testing
@pytest.fixture
def room():
    return Room("TestRoom")

@pytest.fixture
def floor():
    return Floor()

#test ability to toggle individual lights REQ-id4

def test_room_toggle_light():
    "Verify toggling a specific light changes its state (REQ-id4, REQ-id1)."
    room = Room("test_room")
    assert room.lights["bedroom"] is False
    
    room.toggle("bedroom")
    assert room.lights["bedroom"] is True
    
    room.toggle("bedroom")
    assert room.lights["bedroom"] is False

def test_room_set_all():
    "Verify all lights in a room can be turned on/off at once (REQ-id4, REQ-id1)."
    room = Room("test_room")
    room.set_all(True)
    assert all(state is True for state in room.lights.values())
    
    room.set_all(False)
    assert all(state is False for state in room.lights.values())

# REQ-id4: Floor Controls & Room Switching

def test_floor_switch_room():
    "Verify switching between rooms updates the active room (REQ-id4)."
    floor = Floor()
    assert floor.current_room == "room1"
    
    floor.switch_room("room2")
    assert floor.current_room == "room2"
    assert floor.current().name == "room2"

def test_floor_set_all_lights():
    """Verify admin can turn on/off every light on the floor (REQ-id4)."""
    floor = Floor()
    floor.set_all_floor(True)
    
    for room in floor.rooms.values():
        assert all(state is True for state in room.lights.values())

# REQ-id5: Status Display

def test_room_show_output(capsys):
    """Verify the status of all lights is displayed correctly (REQ-id5)."""
    room = Room("room1")
    room.lights["bedroom"] = True  # Set one to ON
    
    room.show()
    captured = capsys.readouterr()
    
    assert "bedroom: ON" in captured.out
    assert "bathroom: OFF" in captured.out


#test login functionality
def test_admin_login(monkeypatch):
    "Verify login returns correct user type and info (REQ-id8)."
    # Mock input for admin login
    inputs = iter(["admin", "admin"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    username, info = login()
    assert username == "admin"
    assert info["role"] == "admin"
def test_guest_login(monkeypatch,capsys):
    "Verify login returns correct user type and info (REQ-id8)."
    "Verify guest can only control their assigned room (REQ-id1)."
    # Mock input for guest login
    inputs = iter(["guest1", "guest1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    username, info = login()
    assert username == "guest1"
    assert info["role"] == "guest"
    assert info["room"] == "room1"

    captured = capsys.readouterr()
    assert captured.out != "room2" ## Ensure guest1 cannot control or see room2 REQ id1
    assert captured.out != "guest2" ## Ensure guest1 cannot control or see room2 REQ id1

def test_invalid_login(monkeypatch,capsys):
    "Verify invalid login is handled correctly (REQ-id11)."
    inputs = iter(["invalid_user", "wrong_pass"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    username, info = login()
    assert username is None
    assert info is None
    assert (result := "Invalid login, unauthorized access denied." in capsys.readouterr().out)



    