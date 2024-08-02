import os

def write_dict_to_files_with_suffix(data, output_folder, suffix):
    for key, value in data.items():
        filename = os.path.join(output_folder, f"{key}_{suffix}.txt")
        with open(filename, 'w') as file:
            for i, item in enumerate(value):
                file.write(f"{item} ")
                if (i + 1) % 20 == 0:
                    file.write("\n")
            file.write("\n")  # Ensure the last line ends with a newline
        print(f"{key}_{suffix}.txt in {output_folder}")