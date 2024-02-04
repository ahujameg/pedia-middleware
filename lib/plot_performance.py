import matplotlib.pyplot as plt
import csv

import pandas as pd

# col=['#b42222', '#ffa347']
# lab=['PEDIA', 'Previous']
# filename = ["PEDIA Rank_output.csv", "rank.csv"]

col=['#0066FF', '#FFCC33','#b42222', '#FF681F', '#00CC99', '#FF00CC']
lab=['PEDIA(CADD+CADA+Gestalt)', 'Gestalt', 'CADD', 'CADA', 'CADA + CADD (from classifier)', 'CADD * CADA (from VarFish)']
filename = ["PEDIA Rank_output.csv", "Face Rank_output.csv", "Pathogenicity Rank_output.csv",
            "Phenotype Rank_output.csv",
            "Combined Rank_output.csv", "Pheno+Patho Rank_output.csv"]


plt.figure(figsize=(18, 12))
top_k_values = [1, 10, 100]
index = 0

# Initialize lists to store intersection points
xticks = []
yticks = []

for label in lab:

    result_df = pd.read_csv(filename[index])

    #print(result_df)

    # Count the occurrences of top-k PEDIA ranks
    count_list = []
    total_cases = len(result_df)
    for k in range(1, 101):
        score_type = filename[index].split(" ")[0] + " Rank"
        top_k_count = len(result_df[result_df[score_type] <= k])
        count_list.append((top_k_count / total_cases) * 100)

    # plt.plot(range(1, len(combined_performance) + 1), combined_performance[0:len(combined_performance)], color=col[index],
    #          alpha=0.6, label=lab[index], linewidth=3)

    plt.plot(range(1, 101), count_list, linewidth=3, color=col[index], label=lab[index])
    plt.scatter([1, 10, 100], [count_list[0], count_list[9], count_list[99]],
                color=col[index], alpha=0.6, marker='o', s=50)
    print(f"Performance for {label} with total case {total_cases}:")
    print(f"Top 1 = {count_list[0]}%")
    print(f"Top 10 = {count_list[9]}%")
    print(f"Top 100 = {count_list[99]}%")

    plt.yticks(range(0, 101, 10), fontsize=28)
    plt.xticks(range(0, 100), labels=[f"Top-{k}" for k in range(0, 100)], fontsize=28)
    plt.xscale('log') # Zoom in from top-1 to top-10

    # Dotted lines for top-1, top-10, top-100
    for value in top_k_values:
        plt.axvline(x=value, color='black', linestyle='--', linewidth=0.8)


    plt.axvline(x=30, color='red', linestyle='--', linewidth=0.8)

    index+=1



# Add intersection points to the plot
plt.scatter(xticks, yticks, color='red', marker='x', label='Intersection')

plt.ylim(0, 100.5)
plt.xlim(1, 100.5)
plt.grid(False)
plt.xlabel('top-k', fontsize=30)
plt.ylabel('Accuracy(%)', fontsize=30)
plt.title('Performance', fontsize=30)
plt.legend(loc='lower right', fontsize=30)
#path = os.path.join(path, 'figures')
#if not os.path.exists(path):
#    os.makedirs(path)
filename = "rank_3" + ".png"
plt.savefig(filename)
plt.close()
