import hw1


def test_arabic_to_roman():
    # Tests that will pass
    assert hw1.arabic_to_roman(1) == "I"
    assert hw1.arabic_to_roman(49) == "XLIX"
    assert hw1.arabic_to_roman('a') == ''
    assert hw1.arabic_to_roman(467) == "CDLXVII"
    assert hw1.arabic_to_roman(1999) == "MCMXCIX"
    assert hw1.arabic_to_roman(2.5) == ''
    assert hw1.arabic_to_roman('3') == ''
    assert hw1.arabic_to_roman(-1) == ''
    assert hw1.arabic_to_roman(2.5) == ''
