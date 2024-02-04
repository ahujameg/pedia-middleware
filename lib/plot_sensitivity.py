import matplotlib.pyplot as plt
import csv

import pandas as pd

# col=['#b42222', '#ffa347']
# lab=['PEDIA', 'Previous']
# filename = ["PEDIA Rank_output.csv", "rank.csv"]

col=['#b42222', '#ffa347','#0064c8', 'green', 'purple']
lab=['PEDIA', 'Gestalt', 'CADD', 'CADA', 'CADA + CADD']
filename = ["PEDIA Rank_output.csv", "Face Rank_output.csv", "Pathogenicity Rank_output.csv", "Phenotype Rank_output.csv", "Pheno+Patho Rank_output.csv"]


plt.figure(figsize=(18, 12))
index = 0
for label in lab:
    rank = []
    combined_performance = []
    total = 0
    with open(filename[index], 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            rank.append(int(row[1]))
            total += int(row[1])
    c_rank = 0
    for value in rank:
        c_rank += value
        combined_performance.append(c_rank / total)

    plt.plot(range(1, len(combined_performance) + 1), combined_performance[0:len(combined_performance)], color=col[index],
             alpha=0.6, label=lab[index], linewidth=3)
    plt.scatter([1, 10, 100], [combined_performance[0], combined_performance[9], combined_performance[99]], color=col[index],
                alpha=0.6, marker='o', s=50)
    #logger.info("%s 1:%f 2-10:%f 100:%f", lab, combined_performance[0], combined_performance[9], combined_performance[99])
    index+=1

plt.ylim(0, 1.01)
plt.xlim(0, 100.5)
plt.xlabel('top-k', fontsize=30)
plt.ylabel('Accuracy', fontsize=30)
plt.title('Performance', fontsize=30)
plt.legend(loc='lower right', fontsize=30)
#path = os.path.join(path, 'figures')
#if not os.path.exists(path):
#    os.makedirs(path)
filename = "rank_3" + ".svg"
plt.savefig(filename)
plt.close()
