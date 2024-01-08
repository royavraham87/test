# tools/simp.py

# Flag to track whether simp module functions were activated
simp_flag = {'activated': False}

def add_numbers(num1, num2):
    simp_flag['activated'] = True
    return num1 + num2

def subtract_numbers(num1, num2):
    simp_flag['activated'] = True
    return num1 - num2
