# RoomLightVision-KonjuPowerCase

### One RoomLightVision to rule them all

### [Project press release](https://github.com/Eino-dev-stu/RoomLightVision-KonjuPowerCase/blob/main/Documents/PressRelease.pdf)

2. Prototype file structure

src
├── classes.py -> Core Logic (Room & Floor classes)
├── hotel.py -> Main App (Login & UI loops)
├── test_hotel.py -> Pytest suite
└── requirements.txt

3. app work logic

### login phase Login as admin or guest1 or guest2, here admin is used:

=== Login ===
Username: admin
Password: admin
Logged in as admin

### Admin interface Shows available commands:

[ADMIN] admin

=== FLOOR ===
Active room: room1

> > Room: room1

    bedroom: OFF
    bathroom: OFF
    livingroom: OFF

Room: room2
bedroom: OFF
bathroom: OFF
livingroom: OFF

Commands:
switch room1/room2
bedroom / bathroom / livingroom
room_on / room_off
floor_on / floor_off
exit with q

> >
