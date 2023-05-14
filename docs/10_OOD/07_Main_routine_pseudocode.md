# Main Routine Pseudocode

Let's use the class, attribute and method names we've identified so
far and try to write the main routine of our program. Doing so should
reveal any missing objects, or missing attributes or methods of objects.
First we'll say what we want to do as plainly as we can in English.

```plaintext
While the game isn't over
    Display the game state
    Display the menu of possible actions
    Get the user's choice of action
    If the action is move
        Display the choices (connected rooms)
        Get the user's choice
        Move the player
        If the room has a bat
            Have the bat snatch the player
        Otherwise if the room has a pit
            Have the pit swallow the player
        Otherwise if the room has a Wumpus
            Wake the Wumpus up
    Otherwise if the action is shoot
        Get the path for the arrow to follow from the user
        Tell the arrow to fly that path
    Otherwise if the action is quit
        Quit the game
```

There's one subtlety here that may escape your notice at first glance
and that is the significance of the ordering of the three possibilities
in reaction to a movement. This pseudocode says that if there is both a
bat and a pit in the room the player moves to, the bat will snatch the
player before they can fall into the pit, making a bat snatch a good
thing in this circumstance! Likewise if there is a pit and a Wumpus the
player will fall into the pit before the Wumpus is woken up. The
instructions we are basing this on do not say what should happen in
these cases, so I have made some arbitrary but reasonable (I think!)
decisions.

Now let's try to match these English phrases with our object methods
and attributes, and introduce some Python where the equivalent Python
commands are obvious (e.g. the main while loop control is something
we've seen before):

```python
 1 while not game_over:
 2     print(cave_system)
 3     print(player.location)
 4     action = input('Shoot, move or quit (s/m/q)? ')
 5     if action == 'm':
 6         print('Choose from: ', cave_system.rooms[player.location].tunnels)
 7         room_choice = int(input('Your choice? '))
 8         player.move(room_choice)
 9         new_room = cave_system.rooms[player.location] # Note simplifying alias.
10         if new_room.has_bat():
11             new_room.bat.snatch()
12         elif new_room.has_pit():
13             new_room.pit.swallow()
14             game_over = True
15         elif new_room.has_wumpus():
16             game_over = room.wumpus.wake_up()
17     elif action == 's':
18         player.shoot()
19     elif action == 'q':
20         game_over = True
```

Take some time to study this code. There are numerous things to note:

→ line 3
:   Displaying the player's `location` attribute (see the dot notation?)

→ line 6
:   `cave_system.rooms[player.location]`.tunnels is a relatively complex
    expression for us, so let's deconstruct it carefully.
    -   cave_system.rooms is the rooms attribute of `cave_system`
    -   the square brackets of `cave_system.rooms[]` indicate that the
        `rooms` attribute is a list of `room`s
    -   we use the player's `location` attribute, `player.location`, to
        access the current room
    -   we display the tunnels leading from the current `room` by printing
        the `tunnels` attribute of the current room

→ line 8
:   `player.move(room_choice)` calls the player's `move` method with
    `room_choice` as a parameter (or equivalently, sends the `player` object
    the message to `move` to `room_choice`)

→ line 9
:   the player is now in `room` `cave_systems.rooms[player.location]` but
    that is a mouthful to say or type so we will introduce a simplifying
    alias for it and refer to it as `new_room`. Note that `new_room`
    is _exactly_ `cave_systems.rooms[player.location]` because it is a
    reference to that object.

→ line 10
:   we call `new_room`'s `has_bat` method to find out if the room contains
    a `bat`.

→ line 11
:   we call the `bat` in `new_room`'s `snatch` method (or equivalently, send
    the `bat` object in `new_room` the message to `snatch`).

→ line 12-15
:   similarly to lines 10 and 11

→ line 16
:   we don't just tell the Wumpus to `wake_up`, we ask it to report back
    to us if the game is over. We need to do this because the game may
    or may not end depending on what the wumpus does, whereas in line 13
    we know the game ends when the player falls in a pit. This is why
    the `swallow` method does not report back: its outcome is a foregone
    conclusion.

→ line 18
:   to keep things short I just called the player's `shoot` method here.
    It may in fact be better to get the arrow's desired path here, like
    we did for the movement destination, than inside the `shoot` method.

That didn't reveal any objects, attributes or methods we had missed,
which gives me enough confidence that we have a reasonable object model
to continue developing our objects. Next we'll flesh out the class
definitions and then return to our main line code.
