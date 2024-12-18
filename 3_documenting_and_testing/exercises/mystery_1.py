def mystery_1(a,b):
    """Adds two inputs, and returns the result.

    Parameters:
        a (any type): The first operand.
        b (any type): The second operand.

    Returns -> any type: The type returned depends on the input types.

    Behavior:
        - If `a` and `b` are numbers, their numerical sum is returned.
        - If `a` and `b` are strings, they are concatenated.
        - If `a` and `b` are lists, they are concatenated.
    
    Raises:
        TypeError: if `a` and `b` are incompatible for the `+` operator.

        >>> mystery_1(6, 5)
        11

        >>> mystery_1(3.5, 4.5)
        8

        >>> mystery_1("MIT", "talent!")
        'MITtalent!'

        >>> mystery_1([1, 2], [3, 4])
        [1, 2, 3, 4]

    """
    return a + b
