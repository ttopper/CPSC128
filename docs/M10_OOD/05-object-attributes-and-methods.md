# Object Attributes and Methods

Keeping the objects we've identified in mind we can re-read the game
description looking for verbs and adjectives to reveal the objects'
attributes and methods.

-   Player
    -   Attributes: At any instant the player has a **location** in the
        cave system and a **number of arrows** left.
    -   Methods: The player is able to **move** from room to room and
        to **shoot** arrows.
-   Bat
    -   Attributes: Like the player(s) each bat has a **location** in
        the cave system.
    -   Methods: A Bat's only action is to **snatch** the player and
        carry him or her away.
-   Pit
    -   Attributes: Like Players and Bats Pits have a **location**.
    -   Methods: Pits can **swallow** players who stumble into them.
-   Wumpus
    -   Attributes: **Location**, 'nuff said.
    -   Methods: All the wumpus does is **wake up** and either run off
        or eat a player.
-   Arrows
    -   Attributes: A **path** they will try and follow.
    -   Methods: An Arrow **flies** from room to room along the
        specified path.

So much for the simple objects.
