def top_n(items, n):
    """
    Arguments:
        items (arr): list or array object
        n (int): number of items to return

    Returns:
        The top n items in an array in descending order

    Examples:
        >>> top_n([7,9,4,5,2,3,0], 3)
    """

    for i in range(n):  #keep sorting until we have the last n items
        for j in range(len(items) - 1 - i):

            if items[j] > items[j + i]: #if this item is greater than the next item
                items[j], items[j + 1] = items[j + 1], items[j] #swap the items
    
    #get last two items
    top_n = items[-n:]

    #return itemms in descending order
    return top_n[::-1]