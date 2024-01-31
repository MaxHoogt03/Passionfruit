import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def make_graphs(filename, text="", x_range=None):
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
    plt.axvline(x=53188, color='black', linestyle='--', linewidth=2, label='Theoretical optimum at 53188')
    # Title and labels
    plt.title(f'Smoothed Histograms of {text} Costs')
    plt.xlabel('Costs')
    plt.ylabel('Density')

    # Legend and grid
    plt.legend()
    plt.grid(True)

    # Set x-axis limits if specified
    if x_range:
        plt.xlim(x_range)

    # Save the figure
    plt.savefig(f'{filename}')

# Example usage with specified x-axis range
make_graphs("shared_graph", "shared")
make_graphs("own_graph_zoomedin", x_range=(53000, 58000))

# Example usage without specifying x-axis range (uses default)
make_graphs("own_graph")
make_graphs("shared_graph_zoomedin","shared", x_range=(35000, 37500))

