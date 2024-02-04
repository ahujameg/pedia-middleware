import csv
import shutil
import os

# Replace 'file_list.csv' and 'destination_folder' with your actual file and folder names
csv_file_path = '/media/meghna/Samsung_T5/TNAMSE_2/TNAMSE_cases.csv'
input_folder = '/media/meghna/Daten10/git-repo/PEDIA/classifier/output_combined'
destination_folder = '/media/meghna/Daten10/git-repo/PEDIA/classifier/output_combined_main'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Read the CSV file to get the list of file paths
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    file_paths = [row[1] for row in csv_reader]

# Cut (move) files to the destination folder
for index, file_path in enumerate(file_paths[1:95]):  # Assuming the CSV list is from 1 to 95
    try:
        shutil.move(os.path.join(input_folder, file_path + '.csv'), os.path.join(destination_folder, file_path + '.csv'))
        print(f"File {file_path} moved to {destination_folder}")
    except FileNotFoundError:
        shutil.move(os.path.join(input_folder, file_path.split('DE')[1] + '.csv'), os.path.join(destination_folder, file_path + '.csv'))
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission error moving {file_path}.")

print("File moving completed.")
