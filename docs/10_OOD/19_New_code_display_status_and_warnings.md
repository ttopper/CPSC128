# New code: Display status and warnings

It wasn't shown in the pseudocode to save space, but we need to display
the status of the game after each move so the player can plan what to
do, and we need to issue the appropriate warnings when we get close to a
hazard. This is done by this code just inside the main event loop:

```python
# Display status:
print(cave_system)
print('You are in room', player.location)
print('You have', player.arrows, 'arrows left.')

# Display warnings:
for room_number in cave_system.rooms[player.location].tunnels:
    if cave_system.rooms[room_number].has_pit():
        print('I feel a draft!')
    if cave_system.rooms[room_number].has_wumpus():
        print('I smell a wumpus!')
    if cave_system.rooms[room_number].has_bat():
        print('Bats nearby!')
```

It displays the whole cave system and reminds the player where they are
and how many arrows they have left. The warnings code loops through the
rooms connected by tunnels to this one. It checks whether each one has a
pit, a wumpus, or a bat and displays the appropriate warning. Note that
since a room can have more than one hazard this code needs to use
separate `if` statements rather an `if` followed by `elif`s.
