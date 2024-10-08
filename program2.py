import os
import re


def check_the_validity_of_password():
    input_file_path = os.path.abspath("inputs\\program2_input.txt")
    input_str = get_input_string(file_path=input_file_path)
    passwords_list = input_str.split(',')
    correct_passwords = []
    for pwd in passwords_list:
        if not 6 <= len(pwd) <= 12:
            continue
        check_special_char = re.search(r"[$#@]", pwd)
        check_numbers = re.search(r"[0-9]", pwd)
        check_lower_case = re.search(r"[a-z]", pwd)
        check_upper_case = re.search(r"[A-Z]", pwd)
        if check_special_char and check_numbers and check_lower_case and check_upper_case:
            correct_passwords.append(pwd)
    valid_passwords = ','.join(correct_passwords)
    print(valid_passwords)


def get_input_string(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
