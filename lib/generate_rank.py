import pandas as pd
import os
import sys

def generate_rank_csv(input_directory, disease_genes_csv, rank_column):
    # Read the disease-causing gene CSV
    gene_data = pd.read_csv(disease_genes_csv)

    # Create an empty DataFrame to store results
    result_df = pd.DataFrame(columns=['Case Name', rank_column])

    # Iterate through each XLSX file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.xlsx'):
            case_name = os.path.splitext(filename)[0]  # Extract case name from file name
            print(case_name)
            file_path = os.path.join(input_directory, filename)

            # Search for the case name in the disease-causing gene CSV
            try:
                xlsx_data = pd.read_excel(file_path)
                case_gene = gene_data[gene_data['VCF'] == case_name]['DG'].values[0].split('/')
                #print(case_gene)
                # Find the rank for the disease-causing gene based on the given column
                score_column = rank_column.split(' ')[0] + ' Score'
                if 0 == xlsx_data[xlsx_data['Gene Symbol'] == case_gene[0]][score_column].values[0] or \
                    -1 == xlsx_data[xlsx_data['Gene Symbol'] == case_gene[0]][score_column].values[0]:
                    rank_value = [999]
                else:
                    rank_value = xlsx_data[xlsx_data['Gene Symbol'] == case_gene[0]][rank_column].values

                if len(rank_value) > 0:
                    # Append the case name and rank value to the result DataFrame
                    result_df = result_df._append({'Case Name': case_name, rank_column: rank_value[0] if len(rank_value) > 0 else None}, ignore_index=True)
                elif len(case_gene) > 1:
                    # Find the rank for the disease-causing gene based on the given column
                    rank_value = xlsx_data[xlsx_data['Gene Symbol'] == case_gene[1]][rank_column].values
                    if len(rank_value) > 0:
                        # Append the case name and rank value to the result DataFrame
                        result_df = result_df._append({'Case Name': case_name, rank_column: rank_value[0] if len(rank_value) > 0 else None}, ignore_index=True)
                    else:
                        result_df = result_df._append({'Case Name': case_name, rank_column: 999}, ignore_index=True)
                        print(f"'{case_gene}' gene not found for case: {case_name}")
                else:
                    result_df = result_df._append({'Case Name': case_name, rank_column: 999}, ignore_index=True)
                    print(f"'{case_gene}' gene not found for case: {case_name}")
            except IndexError:
                result_df = result_df._append({'Case Name': case_name, rank_column: 999}, ignore_index=True)
                print(f"'{rank_column}' column not found for case: {case_name}")
            except KeyError:
                result_df = result_df._append({'Case Name': case_name, rank_column: 999}, ignore_index=True)
                print(f"'{rank_column}' column not found for case: {case_name}")



    # Save the result DataFrame to a CSV file
    result_df.to_csv(f'{rank_column}_output.csv', index=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py input_directory disease_genes_csv")
    else:
        input_dir = sys.argv[1]
        disease_genes_file = sys.argv[2]

        # Generate separate CSV files for different ranks
        ranks = ['PEDIA Rank', 'Face Rank', 'Pathogenicity Rank', 'Phenotype Rank', 'Pheno+Patho Rank']
        for rank in ranks:
            generate_rank_csv(input_dir, disease_genes_file, rank)
