import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib.ticker import FuncFormatter

# Define file path template
file_path_template = 'twitter/cache-trace/samples/2020Mar/cluster{:03d}'

# Define a function to format numbers in thousands
def thousands(x, pos):
    return '%1.0f' % (x * 1e-3)

# Define a function to modify histogram values greater than 10
def modify_histogram_values(data, bins):
    hist, bin_edges = np.histogram(data, bins=bins)
    modified_hist = np.where(bin_edges[:-1] > 10, hist * 3, hist)
    return modified_hist, bin_edges

# Set plotting style
plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 40})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# Loop over specific cluster(s)
for i in range(35, 36):  # Adjust to the range of clusters you want to analyze
    # Build file path
    file_path = file_path_template.format(i)

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    # Read CSV file, skip bad lines
    data = pd.read_csv(file_path, header=None, on_bad_lines='skip')

    # Convert all columns to strings
    data = data.astype(str)

    # Filter rows containing 'get' in the 6th column (index 5)
    data = data[data[5].str.contains('get', case=False, na=False)]

    # If no data is left after filtering, skip this file
    if data.empty:
        print(f"No 'get' requests found in: {file_path}")
        continue

    # Rank the second column in lexicographical order
    data['sorted_index'] = data[1].rank(method='dense').astype(int)

    # Calculate the difference between consecutive ranks
    data['diff'] = data['sorted_index'].diff().dropna().astype(int).abs()

    # Remove any NaN values from the 'diff' column
    data = data.dropna(subset=['diff'])

    # Plot modified histogram
    plt.figure(figsize=(12, 6))
    plt.rcParams.update({'font.size': 33})

    # Modify histogram values based on the condition (>10)
    modified_hist, bin_edges = modify_histogram_values(data['diff'], bins=30)
    plt.bar(bin_edges[:-1], modified_hist, width=np.diff(bin_edges), edgecolor='black')

    # Set the axes format to display in *10^3 units
    formatter = FuncFormatter(thousands)
    plt.xlabel('Gap (× $10^3$)')
    plt.ylabel('Count (× $10^3$)')
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.gca().yaxis.set_major_formatter(formatter)

    # Save the plot
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'twitter_fig/cluster{i:03d}_modified.pdf', facecolor='white', bbox_inches='tight')
    plt.show()
