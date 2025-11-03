# Assignment 8

## Problems

1.  ### Extending a class 1

    Extend the code in [`playing_cards_4.py`](90_playing_cards_4.py) so we
    can find out if a five-card poker hand is a flush, i.e. all cards
    are from the same suit. Here's the specification code to add to the
    end of the module,

        if chris.is_flush():
            print 'That is a flush!'
        else:
            print 'Sorry, no flush.'

2.  ### Extending a class 2

    Sometimes during the course of a card game we might want or need to
    verify that the deck is not corrupted, for example that it does not
    have any extra Aces in it. Extend the code in
    [`playing_cards_4.py`](90_playing_cards_4.py) so we can check that a
    deck is fair.

    Here's the specification code to add to the end of the module,

        if d.is_fair():
            print 'The deck is fair.'
        else:
            print 'Uh oh, this deck is unfair.'


    Include the tests you used to determine that your method was working
    correctly in the code you submit.

3.  ### An alternative playing card representation

    Many OO programmers would look at the playing card classes developed
    in this module and shout,

    > "Wait a minute! Actual physical playing cards have two
    > attributes, their suit and their face value. That means your
    > `Card` objects should have two attributes too that match the
    > physical attributes, not this sketchy card number thing that
    > encodes the values of the actual attributes in an opaque way."

    And you know, they might be right. Modify the module
    [`playing_cards_4.py`](90_playing_cards_4.py) to use `Card` objects
    with a pair of attributes. Name the attributes `suit` and
    `face_value`.

   _Hint 1_: You shouldn't change _anything_ after the
    `if __name__ == '__main__':` statement. Remember that one of the
    goals of encapsulation is to be able drop in a new class
    implementation for an older one without having to rewrite any code
    that uses it.

   _Hint 2_: You don't have to rewrite that much of the code above
    the `if` either. Think carefully about what needs to change.

## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#*yourname`.py` . So problem 
    1 on this assignment will be named `a8p1bob.py`
    and your solution for problem will be named `a8p2bob.py` 
    (adjusted obviously to use your name) .

-   Please submit all your `.py` files to the Moodle dropbox.
