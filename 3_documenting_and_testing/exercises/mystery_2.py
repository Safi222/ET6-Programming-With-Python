def mystery_2(a):
    """Return the length of `a` if exist, otherwise it returns none

    Parameters:
        a (any type): The only operand.
    

    Returns -> any type: The type returned depends on the input types.

    Behavior:
        - If `a` is a number it returns its returns it's length. 
        - If `a` is a string it returns it's length
        - If `a` is a list it returns it's length
        - If `a` is none it returns nothing.
    
    >>> mystery_2("Hello")
    5
    
    >>> mystery_2([2, 4, 5])
    3
    
    >>> mystery_3("")
    
    """
    if len(a) == 0:
        return None

    return len(a)
