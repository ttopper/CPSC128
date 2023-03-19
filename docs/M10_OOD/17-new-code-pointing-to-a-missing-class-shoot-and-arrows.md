# New code (pointing to a missing class): `shoot` and `Arrow`s

Some detail has been added to the `Player.shoot` method compared to the
pseudocode. First, inside the `Player` class we have the method,

        def shoot(self):
            roomlist = input('What rooms [a, b, c]? ')
            self.arrows = self.arrows - 1
            print 'Shooting...'
            # Uncomment the next line when you are ready to add the code it requires.
            # The return below it is a temporary statement to allow the program
            # to execute.
            # return Arrow(self.location, roomlist).fly()
            return MISS

The `shoot` method will get the list of rooms for the arrow to fly
through from the user, decrement the number of arrows left by 1 and then
create an `Arrow` object and tell it to `fly`. Note that the
line `Arrow(self.location, roomlist).fly()` does two things. It first
creates an `Arrow` object with `Arrow(self.location, roomlist)` and then
it immediately sends it the message to fly with the appended `.fly()`.
This line is commented out at the moment since it would just throw an
error because there is no class `Arrow` (you will be creating it as part
of the assignment). To make the code runnable I have simply added an
artificial `return` statement that returns a legal value of `MISS`.

`MISS` is one of three values that the `fly` method can return; the
other two are `HIT` and `OOPS`. These three values correspond to the
three possible outcomes of shooting an arrow: you could hit the wumpus
(`HIT`), miss the wumpus (`MISS`), or shoot yourself (`OOPS`). Shooting
yourself can happen either if you include your current room in your
flight path (not too likely) or if you include unconnected rooms in your
flight path. In the latter case the arrow will begin to fly randomly and
may come back at you and hit you.

The constants are assigned by the statement,

    (HIT, OOPS, MISS) = range(3) # Possible outcomes of shooting an arrow.

The section of the main routine handling shooting was expanded to deal
with each possible return value appropriately,

        elif action == 's':
            outcome = player.shoot()
            
            if outcome == HIT:
                print('You hit the wumpus! You win!')
                game_over = True
                
            elif outcome == OOPS:
                print('Ouch! You shot yourself!')
                game_over = True
                
            elif outcome == MISS:
                print('I'm afraid the Wumpus wasn't in any of those rooms.')
                print('You wasted your arrow.')
            
