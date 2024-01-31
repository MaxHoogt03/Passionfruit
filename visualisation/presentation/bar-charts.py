import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def make_graphs(filename, text=""):
    # File paths for the CSV files
    if text != "":
        text = text + "_"

    file_paths = [
        f'{text}heuristic_hill_1000.csv',
        f'{text}hillclimber_1000.csv',
        f'{text}random_1000.csv',
        f'{text}simulated_annealing_1000.csv',
        f'{text}random_greedy_1000.csv'
    ]

    # Create a dictionary to hold the dataframes, with algorithm names as keys
    datasets = {}

    # Load each dataset and add it to the dictionary
    for file_path in file_paths:
        # Extract the name of the algorithm from the file path, excluding '1000'
        name = file_path.split('/')[-1].replace('.csv', '').replace('_', ' ').replace('1000', '').title().strip()
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
    solution_bars = ax1.bar(indices - width/2, average_solutions, width, label='Average Costs', color='b', alpha=0.6)

    # Labeling and visual adjustments for the first y-axis
    ax1.set_xlabel('Algorithm')
    ax1.set_ylabel('Average Costs', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title('Comparison of Average Costs and Duration for Each Algorithm')

    # Instantiate a second axes that shares the same x-axis
    ax2 = ax1.twinx()

    ax2.set_yscale('log')
    # Plot bars for average times
    time_bars = ax2.bar(indices + width/2, average_times, width, label='Average Duration', color='r', alpha=0.6)

    # Labeling and visual adjustments for the second y-axis
    ax2.set_ylabel('Average Duration (seconds)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    # Set the x-axis tick labels with a multiline approach
    ax1.set_xticks(indices)
    ax1.set_xticklabels([name.replace(' ', '\n') for name in datasets.keys()])

    # Legends
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Save the figure
    plt.savefig(f'{filename}')

# Example usage without specifying x-axis range (uses default)
make_graphs("own_barchart")
make_graphs("shared_barchart", "shared")


