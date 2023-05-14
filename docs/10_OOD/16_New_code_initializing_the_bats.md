# New code: Initializing the bats

```python
# Initialize Bats.
NUMBATS = 2
for bat in range(NUMBATS):
    room = random.choice(cave_system.rooms)
    # Now check if we have already put a bat in this room,
    while room.has_bat():
        # and if we have pick another room.
        room = random.choice(cave_system.rooms)
    room.bat = Bat(room.number)
```

You'll notice there's some new code to initialize the bats. Its job is
to place two bats in two different randomly chosen rooms. It does this
by choosing a room at random and checking to see if there is already a
bat in it. If there is, it chooses another and keeps on doing so until it
finds a room unoccupied by a bat. Once it has a room without a bat, it
creates a bat and places it there.

Notes:

-   The "magic number" 2 has been assigned to the symbolic
    constant `NUMBATS` so the number of bats can be changed by changing
    a single line of code. The jargon for this is to say that the number
    of bats has been _parameterized_.

-   The method `random.choice` may be new to you (I can't remember if I
    have used it before). It chooses an item at random from a list. It
    offers a compact alternative to:

```python
room = cave_system.rooms[random.randint(0, len(cave_system.rooms) - 1)]
```