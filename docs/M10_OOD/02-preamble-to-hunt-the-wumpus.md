# Preamble to Hunt the Wumpus

In our playing card example it was fairly obvious what the objects would
need to be, and there was relatively little communication between them.
This is not typical. In most non-trivial problems there are usually
several equally plausible decompositions which would each lead to quite
different looking programs. Furthermore the pattern of communication can
be quite complicated and depend on subtle conditions. In this module we
will consider a problem with more objects and a less obvious analysis
than the playing cards, and with considerably more communication between
objects. Our problem will be to implement the game [Hunt the Wumpus](https://en.wikipedia.org/wiki/Hunt_the_Wumpus).
