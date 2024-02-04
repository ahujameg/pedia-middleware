import os
import csv


def remove_extension(file_name):
    # Split the file name and extension
    base_name, extension = os.path.splitext(file_name)
    return base_name


def check_entries_exist(source_directory, target_directory):
    # Get a list of entries (files and directories) in the source directory
    source_entries = os.listdir(source_directory)

    # Get a list of entries (files and directories) in the target directory
    target_entries = os.listdir(target_directory)

    # Remove file extensions from entries in both directories
    source_entries_no_ext = [remove_extension(entry) for entry in source_entries]
    target_entries_no_ext = [remove_extension(entry) for entry in target_entries]

    # Check if each entry in the source directory (without extension) exists in the target directory
    all_entries_exist = True
    for entry in source_entries_no_ext:
        if entry not in target_entries_no_ext:
            print(
                f"Entry '{entry}' from '{source_directory}' does not exist in '{target_directory}' without extension.")
            all_entries_exist = False

    if all_entries_exist:
        print("All entries from the source directory exist in the target directory without extension.")
    else:
        print("Not all entries from the source directory are present in the target directory without extension.")


# Example usage:
source_directory = '/media/meghna/Daten10/git-repo/PEDIA/GM Arc Service Branch/TNAMSE-Images'
target_directory = '/media/meghna/Daten10/git-repo/PEDIA/classifier/output_combined_copy'

#target_directory = '/home/meghna/Downloads/TNAMSE Cases VarFish Export1'

check_entries_exist(source_directory, target_directory)