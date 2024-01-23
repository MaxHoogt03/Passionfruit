import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File paths for the CSV files
file_paths = [
    'iterative.csv',
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

# Now, let's plot all the KDEs on one graph
plt.figure(figsize=(14, 8))

# Colors for the different plots
colors = ['red', 'blue', 'green', 'orange', 'purple']

# Plot each dataset
for (name, dataframe), color in zip(datasets.items(), colors):
    sns.kdeplot(dataframe['solution'], shade=True, label=name, color=color)

# Title and labels
plt.title('Smoothed Histograms of Solution Values')
plt.xlabel('Solution Value')
plt.ylabel('Density')

# Legend and grid
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig('combined_kde_plot.png')

# Show the plot
plt.show()