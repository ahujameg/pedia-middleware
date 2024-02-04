import os
import pandas as pd
import matplotlib.pyplot as plt

def count_variants(directory):
    variant_counts = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".xlsx"):  # Assuming the files are in Excel format
            excel_file = pd.ExcelFile(os.path.join(directory, filename))
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                variants = len(df) - 1  # Assuming each row represents a variant
                variant_counts.append(variants)
                filenames.append(filename)
    return variant_counts, filenames

# Input directories for the two groups
directory1 = "/media/meghna/Samsung_T51/TNAMSE_CADD_CADA_new/Final"
directory2 = "/home/meghna/Downloads/main_validation_1.0.9_boxplot"

# Count variants in each directory and get filenames
variants_group1, filenames_group1 = count_variants(directory1)
variants_group2, filenames_group2 = count_variants(directory2)

# Create a boxplot
plt.figure(figsize=(16, 12))
plt.boxplot([variants_group1, variants_group2], labels=['Old Version', 'New Version'])

# Set y-axis limits
#plt.ylim(1800, -400)

# Set labels and title
#plt.xlabel('Groups', fontsize=14)
plt.ylabel('Number of Variants', fontsize=14)
plt.title('Boxplot of Number of Variants', fontsize=16)

# Label data points with variant counts more than 60000 with filenames
# for i, count in enumerate(variants_group1):
#     if count > 1000:
#         plt.text(1, count, filenames_group1[i], fontsize=8, color='blue', horizontalalignment='left')
# for i, count in enumerate(variants_group2):
#     if count > 1000:
#         plt.text(2, count, filenames_group2[i], fontsize=8, color='blue', horizontalalignment='left')

# Show plot
plt.grid(True)
plt.savefig("boxplot.png")

