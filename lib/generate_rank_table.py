import pandas as pd

# Replace 'file1.csv', 'file2.csv', 'file3.csv', and 'gene_file.csv' with your actual file names
file1_path = 'PEDIA Rank_output.csv'
file2_path = 'Face Rank_output.csv'
file3_path = 'Combined Rank_output.csv'
gene_file_path = '/media/meghna/Samsung_T5/TNAMSE_2/TNAMSE_cases.csv'

# Read CSV files into Pandas DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)
gene_df = pd.read_csv(gene_file_path, usecols=['VCF', 'DG'])

# Merge DataFrames based on 'Case Name' column
merged_df = pd.merge(df1, df2, on='Case Name')
merged_df = pd.merge(merged_df, df3, on='Case Name')

# Merge gene names based on 'VCF' column
final_df = pd.merge(merged_df, gene_df, left_on='Case Name', right_on='VCF', how='left')

# Drop duplicate 'VCF' column from gene_df
final_df = final_df.drop('VCF', axis=1)

# Create a new CSV file with the combined data
output_file_path = 'combined_table_with_genes.csv'
final_df.to_csv(output_file_path, index=False)

print(f"Data from {file1_path}, {file2_path}, {file3_path}, and {gene_file_path} combined and saved to {output_file_path}")