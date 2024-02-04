import pandas as pd
import os
import sys

def generate_combined_csv(input_directory, disease_genes_csv, output_csv):
    # Read the disease-causing gene CSV
    gene_data = pd.read_csv(disease_genes_csv)

    # Create an empty DataFrame to store results
    result_df = pd.DataFrame(columns=['Case Name', 'Disease Gene', 'PEDIA Rank', 'PEDIA Score','Face Rank', 'Face Score', 'Pathogenicity Rank', 'Pathogenicity Score', 'Phenotype Rank', 'Phenotype Score', 'Pheno+Patho Rank', 'Pheno+Patho Score'])

    # Iterate through each XLSX file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.xlsx'):
            case_name = os.path.splitext(filename)[0]  # Extract case name from file name
            print(case_name)
            file_path = os.path.join(input_directory, filename)

            # Search for the case name in the disease-causing gene CSV
            try:
                xlsx_data = pd.read_excel(file_path)
                print(gene_data[gene_data['VCF'] == case_name]['DG'].values)
                case_gene = gene_data[gene_data['VCF'] == case_name]['DG'].values[0].split('/')
                
                # Initialize a dictionary to store rank values for the current case
                rank_values = {'Case Name': case_name, 'Disease Gene': gene_data[gene_data['VCF'] == case_name]['DG'].values[0]}

                for rank_column in result_df.columns[2:]:
                    # Find the rank for the disease-causing gene based on the given column
                    if len(case_gene) > 0:
                        rank_value = xlsx_data[xlsx_data['Gene Symbol'] == case_gene[0]][rank_column].values
                        if len(rank_value) > 0:
                            rank_values[rank_column] = rank_value[0] if len(rank_value) > 0 else None
                        elif len(case_gene) > 1:
                            rank_value = xlsx_data[xlsx_data['Gene Symbol'] == case_gene[1]][rank_column].values
                            rank_values[rank_column] = rank_value[0] if len(rank_value) > 0 else None
                    else:
                        rank_values[rank_column] = 999

                # Append the case name and rank values to the result DataFrame
                result_df = result_df._append(rank_values, ignore_index=True)

            except IndexError as e:
                print(f"IndexError: {e} for case & {rank_column}: {case_name}")
            except KeyError as e:
                 print(f"KeyError: {e} for case & {rank_column}: {case_name}")

    # Save the result DataFrame to a single combined CSV file
    result_df.to_excel(output_csv, index=False)
    print(f"Combined data saved to '{output_csv}'.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py input_directory disease_genes_csv output_combined_csv")
    else:
        input_dir = sys.argv[1]
        disease_genes_file = sys.argv[2]
        output_combined_csv = sys.argv[3]

        # Generate a single combined CSV file for all ranks
        generate_combined_csv(input_dir, disease_genes_file, output_combined_csv)

