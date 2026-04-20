## Test plan

1. Enviroment: Python 3.11.31, windows
2. Method: pytest automated tests

## Requirement Mapping (REQ-ids) pytest

| ID       | Requirement         | Test Method                                              |
| -------- | ------------------- | -------------------------------------------------------- |
| REQ-id1  | Guest Restriction   | test_guest_login (Ensures guest is locked to their room) |
| REQ-id3  | Secure Logout       | test_logout (Verifies session termination)               |
| REQ-id4  | Light Control       | test_room_toggle_light & test_floor_set_all_lights       |
| REQ-id5  | Status Display      | test_room_show_output (Checks terminal print accuracy)   |
| REQ-id8  | Role Access         | test_admin_login (Verifies role assignment)              |
| REQ-id10 | Data Logging        | test_light_change_logging (Checks event recording)       |
| REQ-id11 | Unauthorized Access | test_invalid_login (Ensures bad credentials fail)        |
