import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# File paths for the CSV files
file_paths = [
    'heuristic_hill.csv',
    'hill_climber.csv',
    'random.csv',
    'simulated_annealing.csv',
    'random_to_greedy.csv'
]

# Create a dictionary to hold the dataframes, with algorithm names as keys
datasets = {}

# Load each dataset and add it to the dictionary
for file_path in file_paths:
    # Extract the name of the algorithm from the file path
    name = file_path.split('/')[-1].replace('.csv', '').replace('_', ' ').title()
    # Load the dataset and add it to the dictionary
    datasets[name] = pd.read_csv(file_path)

# Calculate the mean values for 'solution' and 'time' for each algorithm
average_solutions = [df['solution'].mean() for df in datasets.values()]
average_times = [df['time'].mean() for df in datasets.values()]

# Set up the figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Set the positions of the bars on the x-axis and width of a bar
indices = np.arange(len(datasets))
width = 0.35

# Plot bars for average solutions
solution_bars = ax1.bar(indices - width/2, average_solutions, width, label='Average Solution', color='b', alpha=0.6)

# Labeling and visual adjustments for the first y-axis
ax1.set_xlabel('Algorithm')
ax1.set_ylabel('Average Solution', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_title('Comparison of Average Solution Values and Times for Each Algorithm')

# Instantiate a second axes that shares the same x-axis
ax2 = ax1.twinx()

# Plot bars for average times
time_bars = ax2.bar(indices + width/2, average_times, width, label='Average Time', color='r', alpha=0.6)

# Labeling and visual adjustments for the second y-axis
ax2.set_ylabel('Average Time (seconds)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set the x-axis tick labels
ax1.set_xticks(indices)
ax1.set_xticklabels(datasets.keys())

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Save the plot
plt.savefig('bar-chart.png')