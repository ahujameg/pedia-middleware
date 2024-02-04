import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define colors and labels
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
labels = ['PEDIA (CADD + CADA + Gestalt)', 'CADD + CADA', 'Gestalt', 'CADD', 'CADA']
filenames = ["PEDIA Rank_output.csv", "Pheno+Patho Rank_output.csv", "Face Rank_output.csv",
             "Pathogenicity Rank_output.csv",
             "Phenotype Rank_output.csv"]

# Set figure size
plt.figure(figsize=(12, 8))

# Initialize lists to store intersection points
intersection_points = []

# Initialize list to store cases where Gestalt out-performs PEDIA
gestalt_outperforms_pedia_cases = []

# Read data for 'PEDIA (CADD + CADA + Gestalt)'
result_df_pedia_gestalt = pd.read_csv(filenames[0])
total_cases_pedia_gestalt = len(result_df_pedia_gestalt)
prev_top_k_percentages_pedia_gestalt = [(len(result_df_pedia_gestalt[result_df_pedia_gestalt[
                                                                         f"{filenames[0].split()[0]} Rank"] <= k]) / total_cases_pedia_gestalt) * 100
                                        for k in range(1, 101)]

# Loop through each dataset
for index, label in enumerate(labels):
    # Skip the first dataset
    if index == 0:
        continue

    # Read data
    result_df = pd.read_csv(filenames[index])
    total_cases = len(result_df)

    # Calculate percentage of top-k ranks
    top_k_percentages = [(len(result_df[result_df[f"{filenames[index].split()[0]} Rank"] <= k]) / total_cases) * 100 for
                         k in range(1, 101)]

    # Plot data
    plt.plot(range(1, 101), top_k_percentages, linewidth=2, color=colors[index], label=labels[index])
    plt.scatter([1, 10, 100], [top_k_percentages[0], top_k_percentages[9], top_k_percentages[99]], color=colors[index],
                alpha=0.6, marker='o', s=50)

    # Print performance details
    print(f"Performance for {label} with total case {total_cases}:")
    print(f"Top 1 = {top_k_percentages[0]:.2f}%")
    print(f"Top 10 = {top_k_percentages[9]:.2f}%")
    print(f"Top 100 = {top_k_percentages[99]:.2f}%")

    # Find intersection points with 'PEDIA (CADD + CADA + Gestalt)'
    prev_line = np.array([range(1, 101), prev_top_k_percentages_pedia_gestalt])
    curr_line = np.array([range(1, 101), top_k_percentages])
    intersection = np.intersect1d(prev_line[0], curr_line[0])
    for x in intersection:
        y1 = np.interp(x, prev_line[0], prev_line[1])
        y2 = np.interp(x, curr_line[0], curr_line[1])
        intersection_points.append((x, y1, y2))

        # Check if Gestalt out-performs PEDIA for this case
        #if label == 'Gestalt' and y2 > y1:
        #    gestalt_outperforms_pedia_cases.append(result_df.iloc[x]['Case'])

    prev_top_k_percentages_pedia_gestalt = top_k_percentages

# Plot intersection points as red crosses and annotate x-axis values
for point in intersection_points:
    plt.scatter(point[0], point[1], color='red', marker='x')
    plt.scatter(point[0], point[2], color='red', marker='x')
    plt.annotate(f'{point[0]}', (point[0], 0), textcoords="offset points", xytext=(0, -20), ha='center', fontsize=10)

# Set axis labels and title
plt.xlabel('Top-k', fontsize=14)
plt.ylabel('Accuracy (%)', fontsize=14)
plt.title('Performance', fontsize=16)

# Set ticks and grid
plt.ylim(0, 100.5)
plt.xlim(1, 100.5)

plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xscale('log')  # Zoom in from top-1 to top-10
plt.xticks([1, 10, 100], labels=['Top-1', 'Top-10', 'Top-100'], fontsize=12)

# Set legend
plt.legend(loc='lower right', fontsize=12)

# Print cases where Gestalt out-performs PEDIA
if gestalt_outperforms_pedia_cases:
    print("Cases where Gestalt out-performs PEDIA:")
    for case in gestalt_outperforms_pedia_cases:
        print(case)

# Save the plot
plt.tight_layout()
plt.savefig("rank_5.png")
