def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_string = ""
    for char in phrase:
        if char == to_swap.lower() or char == to_swap.upper():
            char_to_add = char.lower() if char.isupper() else char.upper()
            flipped_string+=char_to_add
        else:
            flipped_string+=char
    return flipped_string