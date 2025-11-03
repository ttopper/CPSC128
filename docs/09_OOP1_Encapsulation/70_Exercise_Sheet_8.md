# Tutorial 8

1.  ### Write a class describing a specific monster (vampire, zombie, Sith, etc.)

    The class should have an `__init__` method with at least one attribute.

    The class should have at least one other method that describes the signature 
    attack of that monster (bite, shamble, force choke, etc.). It can be as simple
    as printing a description of the attack.

    Create a well commented module of your monster and submit it on the Moodle.
    We are going to come back to these in a few weeks.



2.  ### Coins

    Write a Coin class that will enable this code to run,


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
        

    Of course due to their random selection the exact coins that end up
    in the purse will vary from run to run, though the first coin
    created in the test above should always be a Penny, i.e. the default
    Coin to create is a Penny.


