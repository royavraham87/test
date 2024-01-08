# tools/comp.py

from tools.numbers.simp import simp_flag

def sum_of_digits(number):
    if not simp_flag['activated']:
        raise ValueError("Error: You can't access comp before you used simp!")
    return sum(int(digit) for digit in str(abs(number)))

def is_palindrome(number):
    if not simp_flag['activated']:
        raise ValueError("Error: You can't access comp before you used simp!")
    str_number = str(abs(number))
    return str_number == str_number[::-1]
