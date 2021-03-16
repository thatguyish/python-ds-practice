def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.split(" ")
    new_phrase =[]
    for word in phrase:
        word = word.lower().capitalize()
        new_phrase.append(word)

    return " ".join(new_phrase)
