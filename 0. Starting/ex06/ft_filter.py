
def ft_filter(function, iterable):
    """filter elements based on function
    Args:
        function (_type_): function to apply on each item in iterable
        iterable (_type_): iterable to apply function on
    Returns:
        pass: iterator with items of iterable for which function(item) is True
    """
    if function is None or callable(function) is False:
        return (item for item in iterable if item)
    if hasattr(iterable, '__iter__') is False:
        raise TypeError(f"{type(iterable)} is not iterable") 
    return (item for item in iterable if function(item))

if __name__ == '__main__':
    # values = ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    values = ft_filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(values))