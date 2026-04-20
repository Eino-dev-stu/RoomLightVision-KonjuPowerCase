## Test plan

1. Enviroment: Python 3.11.31, windows
2. Method: pytest automated tests

3. SCOPE:
   Room Logic: Verify that toggle() and set_all() correctly update the dictionary states.
   Floor Logic: Verify that switch_room() updates the current_room pointer correctly.
   Logging: Verify that every state change creates a new entry in usage_log.

Results: [Report](https://github.com/Eino-dev-stu/RoomLightVision-KonjuPowerCase/blob/main/Images/Screenshot%202026-04-20%20175021.png)

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
