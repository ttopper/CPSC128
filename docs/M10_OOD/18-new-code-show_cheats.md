# New code: `show_cheats()`

You'll also notice that a stand alone function called `show_cheats` has
been added. Hunt the Wumpus is **very** time-consuming to debug efficiently
unless you know where the hazards are so you can go straight to them and
see if your program handles them properly. `show_cheats` has been
included to give you that information. It tells you where the wumpus,
bats, and pits are so you can head toward (or away!) from them during
testing.

```python
    def show_cheats():
        '''Shows information about the cave system to ease debugging.
        Should be disabled in the final version.'''
        print 'Psst!'
        for room in cave_system.rooms:
            if room.has_bat(): print '   There's a bat in room', room.number
            if room.has_pit(): print '   There's a pit in room', room.number
            if room.has_wumpus(): print '   There's a wumpus in room', room.number
```