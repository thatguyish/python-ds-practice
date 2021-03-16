def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    mode_value = 0
    for num in nums:
        mode = num if nums.count(num)>mode_value else mode_value
        mode_value = mode

    return mode_value