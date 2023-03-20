# Assignment 9

## Problems

1.  ### A little class of your own

    Write a Coin class that will enable this code to run,

    ```python
    # Your class goes here...
 
    if __name__ == '__main__':
        coin = Coin()
        print(f'Your first coin is a {coin}.')
    
        purse = [coin]
        print('Adding four more coins to your purse...')
        for i in range(4):
            coin = Coin(random.choice([5,10,25,100,200]))
            purse.append(coin)
    
        print('In your purse you now have:')
        for coin in purse:
            print('\ta', coin)
    
        total = 0
        for coin in purse:
            total += coin.value
        print('The total value of the coins in your purse is', total, 'cents.')
    
        print('Flipping your coins you get:',end=' ')
        for coin in purse:
            print(coin.flip(),end = ' ')
    and produce this output,

    >>> 
    Your first coin is a Nickle.
    Adding four more coins to your purse...
    In your purse you now have:
        a Nickle
        a Loonie
        a Penny
        a Dime
        a Quarter
    The total value of the coins in your purse is 137 cents.
    Flipping your coins you get: Tails Tails Tails Heads Tails

    ```

    and produce this output,

        >>> 
        Your first coin is a Penny.
        Adding four more coins to your purse...
        In your purse you now have:
              a Penny
              a Loonie
              a Penny
              a Dime
              a Quarter
        The total value of the coins in your purse is 137 cents.
        Flipping your coins you get: Tails Tails Tails Heads Tails
        >>> 

    Of course due to their random selection the exact coins that end up
    in the purse will vary from run to run, though the first coin
    created in the test above should always be a Penny, i.e. the default
    Coin to create is a Penny.

2.  ### Extending a class 1

    Extend the code in [`playing_cards_4.py`](90_playing_cards_4.py) so we
    can find out if a five card poker hand is a flush, i.e. all cards
    are from the same suit. Here's the specification code to add to the
    end of the module,

    ``` python
    if chris.is_flush():
        print 'That is a flush!'
    else:
        print 'Sorry, no flush.'
    ```

3.  ### Extending a class 2

    Sometimes during the course of a card game we might want or need to
    verify that the deck is not corrupted, for example that it does not
    have any extra Aces in it. Extend the code in
    [`playing_cards_4.py`](90_playing_cards_4.py) so we can check that a
    deck is fair.

    Here's the specification code to add to the end of the module,

    ``` python
    if d.is_fair():
        print 'The deck is fair.'
    else:
        print 'Uh oh, this deck is unfair.'
    ```

    Include the tests you used to determine that your method was working
    correctly in the code you submit.

4.  ### An alternative playing card representation

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

    *Hint*~1~: You shouldn't change *anything* after the
    `if __name__ == '__main__':` statement. Remember that one of the
    goals of encapsulation is to be able drop in a new class
    implementation for an older one without having to rewrite any code
    that uses it.

    *Hint*~2~: You don't have to rewrite that much of the code above
    the `if` either. Think carefully about what needs to change.

## Logistics

-   Use the following naming scheme for your program files:
    `a`*assignment#*`p`*problem#*yourname`.py` . So your first
    attempt at problem 1 on this assignment will be named `a9p1bob.py`
    and your solution for problem will be named `a9p2bob.py` (adjusted obviously to use your name) .

-   Please submit all your .py files to the Moodle dropbox.
