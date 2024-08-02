from collections import Counter

def convert_strings_to_counts(string_grams):
    """Converts a Counter of n-grams into a dictionary"""
    counter_of_grams = Counter(string_grams)
    dict_of_grams = dict(counter_of_grams)
    counter_dict = Counter(dict_of_grams)
    return counter_dict