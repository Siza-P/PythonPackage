from my_first_package import myModule

def test_top_n():
    """
    testing if top_n funtction works correctly
    """

    assert myModule.top_n([7, 9, 4, 5, 2, 3, 0], 3) == [9, 7, 5], "Incorrect"
    assert myModule.top_n([8, 4, 5, 7, 2], 2) == [8, 7], "Incorrect"
    assert myModule.top_n([11, 6, 3, 7, 1, 4, 1], 4) == [11, 7, 6, 4], "Incorrect"