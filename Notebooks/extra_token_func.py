import os

def remove_keys_from_nested_dict(main_dict, words_to_remove):
    """
    Removes specified keys from all sub-dictionaries inside a nested dictionary.
    Args:
        main_dict (dict): The input nested dictionary.
        words_to_remove (list): List of words (keys) to be removed from the sub-dictionaries.
    Returns:
        dict: The modified nested dictionary with the specified keys removed.
    """
    # Create a copy of the main dictionary to avoid modifying the original during iteration
    modified_dict = main_dict.copy()

    # Iterate over each sub-dictionary
    for corpus, sub_dict in modified_dict.items():
        # Remove specified keys from the sub-dictionary
        for word in words_to_remove:
            sub_dict.pop(word, None)

    return modified_dict


def print_first_n_items(data, n):
    for key, subdict in data.items():
        print(f"First {n} items in {key}:")
        for item, count in subdict.most_common(n):
            print(f"{item}: {count}")
        print()