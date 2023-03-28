# The Cave System Object(s)

The cave system is the lynchpin of this system of objects because all
the simple objects are situated in and/or move through it. It is also
the most complex of the objects because it is a *compound object*: the
cave system consists of_multiple_rooms connected
by_multiple_tunnels. This means that it will have to be a container
type of some sort.

-   Attributes: **20 caves**; the **pattern of connections** between
    caves.
-   Methods: Should be able to tell us **where you can go from
    here** (i.e. what rooms are connected to this one); if a room **has
    a bat**; if a room **has a pit**; if the **player is in** a room.

The cave system contains 20 Room objects which as objects have their own
attributes and methods:

-   Attributes: **3 tunnels**, possibly **a bat**, possibly **a pit**,
    possibly **a wumpus**.
-   Methods: Should be able to tell us if it **has a bat**, **has a
    pit**, or **has a wumpus**.
