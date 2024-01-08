# app.py

from tools.numbers.simp import simp_flag, add_numbers, subtract_numbers
from tools.numbers.comp import sum_of_digits, is_palindrome
from tools.col import myzip

def Myzip_fun(list1, list2):
    # Using the custom myzip function
    result = list(myzip(list1, list2))
    print(result)

def Comp_calc(number):
    if not simp_flag['activated']:
        raise ValueError("Error: You can't access comp before you used simp!")
    else:
        result_sum_of_digits = sum_of_digits(number)
        result_is_palindrome = is_palindrome(number)

        print("Sum of digits:", result_sum_of_digits)
        print("Is palindrome:", result_is_palindrome)
        print("simp was activated Successfully")

def Simp_calc(num1, num2):
    result_add = add_numbers(num1, num2)
    result_subtract = subtract_numbers(num1, num2)

    print("Result of adding:", result_add)
    print("Result of subtracting:", result_subtract)

def main():
    # Define lists for Myzip_fun
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c']

    # Activate functions with specific numbers and lists
    Simp_calc(5, 3)
    Comp_calc(12321)
    Myzip_fun(list1, list2)

if __name__ == "__main__":
    main()
