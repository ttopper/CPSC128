# crud_controller_0.py
# Forever
over = False
while not over:

    # Display the possible actions
    print('''
    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit
    Your choice?''')

    # Get the user's choice of action
    choice = input()
    
    # Execute the code corresponding to the chosen action
    if choice == 'c':
        pass       
    elif choice == 'r':
        pass   
    elif choice == 'u':
        pass   
    elif choice == 'd':
        pass  
    elif choice == 'l':
        pass            
    elif choice == 'q':
        over = True       
    else:
        print('Not a valid choice!')
        
db.close()
