from Multiple import Multiple

def test_Multiple_of_3():
    mult = Multiple()
    assert mult.of_3(2) == False
    assert mult.of_3(3) == True