# wumpus_4.py
#
# Hunt the Wumpus game.
# Version 0.4
#
# Tim Topper (updated by Kate Chatfield-Reed)
# CPSC 128
# Winter 2023
#
# Bugs:
# - Bat may end up in same room with player after snatch.
# - Wumpus position is not properly set after moving.
# - Player may start game in room with a pit or wumpus.
#
# Missing code:
# - class Arrow (called at line 75).
#
#
import random

class Room:
    '''e.g. r = Room(0,[1,7,4])'''
    def __init__(self, room_number, connections, b = None, p = None, w = None):
        self.number = room_number
        self.tunnels = connections
        self.bat = b
        self.pit = p
        self.wumpus = w
        
    def has_bat(self):
        if self.bat:
            return True
        else:
            return False
        
    def has_pit(self):
        if self.pit:
            return True
        else:
            return False
        
    def has_wumpus(self):
        if self.wumpus:
            return True
        else:
            return False

class Bat:
    def __init__(self, roomnumber):
        self.location = roomnumber
        
    def snatch(self, player):
        print()
        print('Aaah! A giant bat has snatched you!')
        print()
        # First we'll move the player.
        player.location = random.randint(0, len(cave_system.rooms) - 1)
        # Now we'll move the bat.
        # First we'll remove it from this room.
        cave_system.rooms[self.location].bat = None
        # Then we'll choose a new room for it,
        self.location = random.randint(0, len(cave_system.rooms) - 1)
        # and put it in the new room.
        cave_system.rooms[self.location].bat = self

class Pit:
    def __init__(self, room_number):
        self.location = room_number
        
    def swallow(self):
        # What a pit does when it swallows a player.
        print('AIEEEE! You\'re falling to your doom down the pit!')

class Wumpus:
    def __init__(self, roomnumber):
        self.location = roomnumber
        
    def wake_up(self):
        ''' Wake Wumpus up and see what happens.
        returns True if the Wumpus eats the player,
        and False otherwise.'''
        # 1 in 4 chance Wumpus eats the player,
        if random.randint(1,4) == 4:
            print('Uh oh the Wumpus got you!')
            return True
        # and 3 in 4 chance it runs to an adjacent room.
        else:
            print('Wheww! The Wumpus woke up but he ran away.')
            self.location = random.choice(cave_system.rooms[self.location].tunnels) # BUG!
            return False

def show_cheats():
    '''Shows information about the cave system to ease debugging.
    Should be disabled in the final version.'''
    print('Psst!')
    for room in cave_system.rooms:
        if room.has_bat(): print('   There\'s a bat in room', room.number)
        if room.has_pit(): print('   There\'s a pit in room', room.number)
        if room.has_wumpus(): print('   There\'s a wumpus in room', room.number)

INSTRUCTIONS = '''
Welcome to "Hunt the Wumpus"

The wumpus lives in a cave of 20 rooms. Each room has 3 has_tunnels_to to
other rooms. (Look at a dodecahedron to see how this works. If you
don't know what a dodecahedron is, ask someone.)

Hazards:
  Bottomless pits - Two rooms have bottomless pits in them. If you go
    there, you fall into the pit (& lose)!
  Super bats - Two other rooms have super bats. If you go there, a
    bat grabs you and takes you to some other room at random (which
    may be troublesome).

Wumpus:
   The wumpus is not bothered by hazards. (He has sucker feet and is
   Too big for a bat to lift.)  Usually he is asleep. Two things
   wake him up: Your shooting an arrow, or your entering his room.
   If the wumpus wakes, he moves (p=.75) one room or stays still
   (p=.25).  After that, if he is where you are, he eats you up and
   you lose!

You:
   Each turn you may move or shoot a crooked arrow.
   Moving:  You can move one room (Through one tunnel).
   Arrows:  You have 5 arrows.  You lose when you run out.  Each
      arrow can go from 1 to 3 rooms.  You aim by telling the
      computer the rooms to which you want the arrow to go.  If the
      arrow can't go that way (if no tunnel) it moves at random to
      the next room.
      If the arrow hits the wumpus, you win.
      If the arrow hits you, you lose.

Warnings:
   When you are one room away from a wumpus or hazard, the computer
   says:
   Wumpus:  "I smell a wumpus!"
   Bat   :  "Bats nearby!"
   Pit   :  "I feel a draft!"
'''

(HIT, OOPS, MISS) = range(3) # Possible outcomes of shooting an arrow.

TUNNELS = [[1,7,19], [0,2,14], [1,3,6], [2,4,13], [3,5,11],
           [4,6,9], [2,5,7], [0,6,8], [7,9,18], [5,8,10],
           [9,11,17], [4,10,12], [11,13,16], [3,12,14], [1,13,15],
           [14,16,19], [12,15,17], [10,16,18], [8,17,19], [0,15,18]
          ]

MAP ='''
     19 - - - - - - - - - - - - - - - -  15
    /   \                               /  \ 
   /     \     - - - - 1 - - - -       /    \ 
  /       \   /        |         \    /      \ 
 /         \ /         |          \  /        \ 
 |          0          2           14          |
 |         /          / \           \          |
 |        /         /     \          \         |
 |       /        /         \         \        |
 |      7 - - - 6             3 - - - 13       |
 |       \       \           /        /        |
 |        \       \         /        /         |
18 - - - - 8       5 - - - 4        12 - - - - 16
  \         \     /          \     /          /
   \         \  /              \  /          /
    \         9 - - - 10 - - -  11          /
     \                 |                   /
      \                |                  /
       \               |                 /
         - - - - - -  17 - - - - - - - -
'''

# cave_system is a global variable.
# Global variables are generally frowned on,
# but we don't have time to do justice to the
# alternative -- come back for NCIT 212!
cave_system = Cave_System(TUNNELS, MAP)

# Initialize Bats.
NUMBATS = 2
for bat in range(NUMBATS):
    room = random.choice(cave_system.rooms)
    # Now check that we haven't already put a bat in this room,
    while room.has_bat():
        # and if we have pick another room.
        room = random.choice(cave_system.rooms)
    room.bat = Bat(room.number)

# Initialize Pits.


# Initialize Wumpus.
room = random.choice(cave_system.rooms)
room.wumpus = Wumpus(room.number)

# Initialize Player.
player = Player(0, 5)



game_over = False
