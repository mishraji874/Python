"""
FUNCTIONS WITH OUTPUTS

def my_function():
    result = 3 * 2
    return result

def my_function():
    return 3 * 2
"""

def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{f_name.title()} {l_name.title()}")
    return f"{formated_f_name} {formated_l_name}"

format_name("angela", "ANGELA")