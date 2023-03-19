# Summary: Module Layout

The standard layout for modules is,

    # filename.py
    # ...
    ''' Module docstring '''

    # import statements
    import ...
    import ...
    ...

    # Function definitions
    def name( args ):
        ''' Function docstring '''
        ...

    def name( args ):
        ''' Function docstring '''
        ...

    ...

    if __name__ == '__main__':
        # Unit tests
        ...
