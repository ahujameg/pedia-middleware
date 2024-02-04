import csv

def extract_hpo_terms(line, separator):
    # Extract HPO terms from the line
    hpo_terms = set()
    parts = line.strip().split('\t')
    if len(parts) < 3:
        return hpo_terms
    hpo_list = parts[2].split(separator)
    for hpo in hpo_list:
        hpo_terms.add(hpo.strip())
    return hpo_terms

def main(csv_file, tsv_file):
    # Read HPO terms from CSV file
    csv_hpo_terms = []
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)  # Skip header if present
        for row in csv_reader:
            hpo_terms = extract_hpo_terms(row[2], ';')
            csv_hpo_terms.append(hpo_terms)

    print(csv_hpo_terms)

    # Read and compare HPO terms from TSV file
    with open(tsv_file, 'r') as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter='\t')
        for tsv_line in tsv_reader:
            tsv_hpo_terms = extract_hpo_terms(tsv_line[3], ',')
            #for i, csv_terms in enumerate(csv_hpo_terms):
                #if tsv_hpo_terms == csv_terms:
                    #print(f"Match found for patient in CSV line {i}: {tsv_line[0]}")

if __name__ == "__main__":
    csv_file = input("Enter path to CSV file: ")
    tsv_file = input("Enter path to TSV file: ")
    main(csv_file, tsv_file)
