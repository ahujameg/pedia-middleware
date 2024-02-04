import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from adjustText import adjust_text

# Define colors and labels
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#CBCDAF']
labels = ['PEDIA (CADD + CADA + Gestalt)', 'CADD + CADA', 'Gestalt', 'CADD', 'CADA']
filenames = ["PEDIA Rank_output.csv", "Pheno+Patho Rank_output.csv", "Face Rank_output.csv", "Pathogenicity Rank_output.csv",
            "Phenotype Rank_output.csv"]

# Set figure size
plt.figure(figsize=(12, 8))

# Initialize lists to store intersection points
intersection_points = []
texts = []

# Loop through each dataset
for index, label in enumerate(labels):
    # Read data
    result_df = pd.read_csv(filenames[index])
    total_cases = len(result_df)

    # Calculate percentage of top-k ranks
    top_k_percentages = [(len(result_df[result_df[f"{filenames[index].split()[0]} Rank"] <= k]) / total_cases) * 100 for k in range(1, 101)]

    # Plot data
    plt.plot(range(1, 101), top_k_percentages, linewidth=2, color=colors[index], label=labels[index])
    plt.scatter([1, 10, 100], [top_k_percentages[0], top_k_percentages[9], top_k_percentages[99]], color=colors[index], alpha=0.6, marker='o', s=50)

    # Print performance details
    print(f"Performance for {label} with total case {total_cases}:")
    print(f"Top 1 = {top_k_percentages[0]:.2f}%")
    print(f"Top 10 = {top_k_percentages[9]:.2f}%")
    print(f"Top 100 = {top_k_percentages[99]:.2f}%")



    # Annotate with performance numbers and arrows.
    # if label == 'CADD':
    #     plt.annotate(f'{top_k_percentages[0]:.2f}%', (1, top_k_percentages[0]),
    #                  arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3'),
    #                  textcoords="offset points", xytext=(15, -30), ha='center', fontsize=11)
    #     plt.annotate(f'{top_k_percentages[9]:.2f}%', (10, top_k_percentages[9]), textcoords="offset points",
    #                  arrowprops=dict(arrowstyle='->', connectionstyle='arc3', facecolor='blue'),
    #                  xytext=(15, -30), ha='center', fontsize=11)
    # else:
    #     plt.annotate(f'{top_k_percentages[0]:.2f}%', (1, top_k_percentages[0]),
    #                  arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3'),
    #                  textcoords="offset points", xytext=(15, 15), ha='center', fontsize=11)
    #     plt.annotate(f'{top_k_percentages[9]:.2f}%', (10, top_k_percentages[9]), textcoords="offset points",
    #                  arrowprops=dict(arrowstyle='->', connectionstyle='arc3', facecolor='blue'),
    #                  xytext=(15, 15), ha='center', fontsize=11)

    #texts.append((plt.text(1, top_k_percentages[0], f'{top_k_percentages[0]:.2f}%')))
    #texts.append((plt.text(10, top_k_percentages[9], f'{top_k_percentages[9]:.2f}%')))

    # Find intersection points with previous lines
    if index > 0:
        prev_line = np.array([range(1, 101), prev_top_k_percentages])
        curr_line = np.array([range(1, 101), top_k_percentages])
        intersection = np.intersect1d(prev_line[0], curr_line[0])
        for x in intersection:
            y1 = np.interp(x, prev_line[0], prev_line[1])
            y2 = np.interp(x, curr_line[0], curr_line[1])
            intersection_points.append((x, y1, y2))

    prev_top_k_percentages = top_k_percentages

# Plot intersection points as red crosses and annotate x-axis values
# for point in intersection_points:
#     plt.scatter(point[0], point[1], color='red', marker='x')
#     plt.scatter(point[0], point[2], color='red', marker='x')
#     plt.annotate(f'{point[0]}', (point[0], 0), textcoords="offset points", xytext=(0,-20), ha='center', fontsize=5)

# Adjust the positions of text annotations to avoid overlaps
#adjust_text(texts)

# Set axis labels and title
plt.xlabel('Top-k', fontsize=14)
plt.ylabel('Accuracy (%)', fontsize=14)
plt.title('Performance of different algorithms', fontsize=16)

# Set ticks and grid
plt.ylim(0, 100.5)
plt.xlim(1, 100.5)

plt.yticks(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xscale('log') # Zoom in from top-1 to top-10
plt.xticks([1, 10, 100], labels=['1', '10', '100'], fontsize=14)

#plt.axvline(x=32, color='red', linestyle='--', linewidth=0.8)
#plt.axvline(x=35, color='green', linestyle='--', linewidth=0.8)

# Add annotations
#for index, label in enumerate(labels):
#    plt.annotate(label, (100, top_k_percentages[index]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=12, color=colors[index])

# Set legend
plt.legend(loc='lower right', fontsize=12)

# Save the plot
#plt.tight_layout()
plt.savefig("rank_5.svg")
