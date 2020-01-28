# Nadim El Helou - EC 500 C1 - HW1 Convert arabic numerals into roman numerals
# Reference: Geeks for Geeks - https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/


def arabic_to_roman(arabic):

    # Check input is an integer
    if not isinstance(arabic, int):
        print("Error. Enter an integer.")
        return ''

    # Check input is in range
    if arabic < 1 or arabic > 4000:
        print("Error. Enter an integer between 1 and 4000.")
        return ''

    # Setup numbers 'bank'
    numbs = [ 1,   4,    5,   9,    10,  40,   50,  90,  100,  400, 500,  900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = len(numbs) - 1
    roman_numeral = ""

    # Iterate through numbers bank in reverse order and factor them out from the input
    while arabic > 0:
        factor = arabic // numbs[i]
        arabic = arabic % numbs[i]
        while factor > 0:
            roman_numeral = roman_numeral + roman[i]
            factor = factor - 1
        i = i - 1

    return roman_numeral
