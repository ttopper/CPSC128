# OO Analysis

The OO analysis isn't too tricky in this problem because we have a
pretty good informal specification: the description of the game and its
rules that is displayed at the start of the game. Remembering that
objects often correspond to nouns in the problem domain, let's read
over the game description and highlight the objects (nouns) it
discusses:

    Welcome to "Hunt the Wumpus"
     
    The  wumpus  lives in a  cave  of 20  rooms . Each room has 3  tunnels  to
    other rooms. (Look at a dodecahedron to see how this works. If you
    don't know what a dodecahedron is, ask someone.)
     
    Hazards:
     Bottomless  pits  - Two rooms have bottomless pits in them. If  you  go
     there, you fall into the pit (& lose)!
     Super  bats  - Two other rooms have super bats. If you go there, a
     bat grabs you and takes you to some other room at random (which
     may be troublesome).
     
    Wumpus:
     The wumpus is not bothered by hazards. (He has sucker feet and is
     Too big for a bat to lift.) Usually he is asleep. Two things
     wake him up: Your shooting an  arrow , or your entering his room.
     If the wumpus wakes, he moves (p=.75) one room or stays still
     (p=.25). After that, if he is where you are, he eats you up and
     you lose!
     
    You:
     Each turn you may move or shoot a crooked arrow.
     Moving: You can move one room (Through one tunnel).
     Arrows: You have 5 arrows. You lose when you run out. Each
     arrow can go from 1 to 3 rooms. You aim by telling the
     computer the rooms to which you want the arrow to go. If the
     arrow can't go that way (if no tunnel) it moves at random to
     the next room.
     If the arrow hits the wumpus, you win.
     If the arrow hits you, you lose.
     
    Warnings:
     When you are one room away from a wumpus or hazard, the computer
     says:
     Wumpus: "I smell a wumpus!"
     Bat : "Bats nearby!"
     Pit : "I feel a draft!"
     
    You are in room 12.
    There are tunnels to rooms 11, 13, and 19.
    I feel a draft!
    Shoot, move, or quit (s/m/q)? m
    To which room (11, 13, or 19)? 13
    AEEEIIIIII! You fell into a pit!

The types of objects we have then are:

-   a wumpus;
-   a cave system of
-   rooms connected by
-   tunnels;
-   pits;
-   you, i.e. the player,
-   bats; and
-   arrows.

And from the rules we can tell what behaviours the objects will have.
The Wumpus mostly sleeps (as he digests the villagers he ate last
night), but does wake when disturbed and then has behaviour with a
random component to it. Bats grab players and fly them somewhere else.
You move from room to room and shoot arrows. And so on.
