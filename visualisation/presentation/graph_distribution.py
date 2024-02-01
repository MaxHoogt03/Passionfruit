import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ultraimport
theoretical_optimum = ultraimport('__dir__/theoretical_optimum.py', 'theoretical_optimum', recurse = True)

def make_graphs(filename, text="", theoretopt = 0 ,x_range=None,):
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
        sns.kdeplot(dataframe['solution'], fill=True, label=name, color=color)
    
    if theoretopt == 1:
        plt.axvline(x=theoretical_optimum(), color='black', linestyle='--', linewidth=2, label=f'Theoretical optimum at {theoretical_optimum()}')
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


make_graphs("shared_graph", "shared")
make_graphs("shared_graph_zoomedin","shared", x_range=(35000, 37500))


make_graphs("own_graph", theoretopt= 1)
make_graphs("own_graph_zoomedin", x_range=(53000, 58000), theoretopt = 1)


