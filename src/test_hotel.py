import pytest
from classes import Room

#setup for testing
@pytest.fixture
def room():
    return Room("TestRoom")

#test ability to toggle individual lights REQ-id4
def test_toggle_light(room):
    # Testing initial state and toggle
    assert room.lights["bedroom"] is False
    room.toggle("bedroom")
    assert room.lights["bedroom"] is True

#test ability to toggle all lights in the room REQ-id4
def test_set_all(room):
    # Testing set_all functionality
    room.set_all(True)
    for state in room.lights.values():
        assert state is True

    room.set_all(False)
    for state in room.lights.values():
        assert state is False


