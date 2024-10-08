import os


def check_frequency_of_words():
    input_file_path = os.path.abspath("inputs\\program1_input.txt")
    input_str = get_input_string(file_path=input_file_path)
    words_list = input_str.split()
    freq = {}
    for i in words_list:
        freq[i] = freq.get(i, 0) + 1
    aplhanumeric_sorted_output = dict(sorted(freq.items()))
    for key, value in aplhanumeric_sorted_output.items():
        print(f"('{key}': {value})")


def get_input_string(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
