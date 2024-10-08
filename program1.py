def check_frequency_of_words(input_str):
    words_list = input_str.split()
    freq = {}
    for i in words_list:
        freq[i] = freq.get(i, 0) + 1
    aplhanumeric_sorted_output = dict(sorted(freq.items()))
    for key, value in aplhanumeric_sorted_output.items():
        print(f"('{key}': {value})")


check_frequency_of_words(input_str="which is better python 2 or python 3")
