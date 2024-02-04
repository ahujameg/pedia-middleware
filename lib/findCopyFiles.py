import os
import pandas as pd
import shutil

# Input CSV file and directories
csv_file = "/media/meghna/Samsung_T5/TNAMSE_2/TNAMSE_cases.csv"
input_directory = "/media/meghna/Samsung_T51/TNAMSE_CADD_CADA_new/All"
output_directory = "/media/meghna/Samsung_T51/TNAMSE_CADD_CADA_new/Final"

# Read CSV file
df = pd.read_csv(csv_file)

# Function to find corresponding file in the input directory
def find_vcf_file(vcf_entry):
    for filename in os.listdir(input_directory):
        if vcf_entry.split('_hg')[0] in filename:
            return os.path.join(input_directory, filename)
    return None

# Iterate over each entry in the VCF column
for vcf_entry in df['VCF']:
    vcf_file = find_vcf_file(vcf_entry)
    if vcf_file:
        # Construct output file path
        output_file = os.path.join(output_directory, os.path.basename(vcf_file))
        # Copy file to output directory
        shutil.copy2(vcf_file, output_file)
        print(f"Copied {vcf_file} to {output_file}")
    else:
        print(f"No VCF file found for entry {vcf_entry}")
