import os

# Takes a word and returns a cleaned up version of the word
def wordcleaner(someword):
    cleanword = someword.casefold()
    while cleanword and not cleanword[-1].isalnum():
        cleanword = cleanword[:-1]
    while cleanword and not cleanword[0].isalnum():
        cleanword = cleanword[1:]
    return cleanword

def write_words_to_file(word_list, output_file, words_per_line=20):
    with open(output_file, "w") as outfile:
        for i in range(0, len(word_list), words_per_line):
            line = " ".join(word_list[i:i + words_per_line])
            outfile.write(line + "\n")

def dictionary_to_file(dictionary, output_folder, name):
    """
    Saves each nested subdictionary in a dictionary as a separate .csv file
    named after the key of the subdictionary.
    Args:
        dictionary (dict): The input dictionary containing subdictionaries.
        output_folder (str): The directory where the .csv files will be saved.
    """
    for key, subdict in dictionary.items():
        # Define the .csv file path
        csv_file_path = os.path.join(output_folder, f"{key}_{name}.csv")
        output_table = [['token_', 'count']]
        # Sort the subdictionary by count in descending order and fill out the table
        for word, count in sorted(subdict.items(), key=lambda item: item[1], reverse=True):
            new_row = [word, count]
            output_table.append(new_row)
        
        with open(csv_file_path, 'w') as output_file:
            for row in output_table:
                str_version = [str(i) for i in row]
                output_str = ",".join(str_version)
                output_file.write(output_str + "\n")
        print(f"Saved {key}_{name}.csv in {output_folder}")

def convert_tuple_bigrams(tuples_to_convert):
    """Converts NLTK tuples into bigram strings"""
    string_grams = []
    for tuple_grams in tuples_to_convert:
        first_word = tuple_grams[0]
        second_word = tuple_grams[1]
        if first_word and second_word:
            gram_string = f'{first_word} {second_word}'
            string_grams.append(gram_string)
    return string_grams

def convert_tuple_trigrams(tuples_to_convert):
    """Converts NLTK tuples into trigram strings"""
    string_grams = []
    for tuple_grams in tuples_to_convert:
        if len(tuple_grams) < 3:
            continue  # Skip tuples that don't have at least three elements
        first_word = tuple_grams[0]
        second_word = tuple_grams[1]
        third_word = tuple_grams[2]
        if first_word and second_word and third_word:
            gram_string = f'{first_word} {second_word} {third_word}'
            string_grams.append(gram_string)
    return string_grams