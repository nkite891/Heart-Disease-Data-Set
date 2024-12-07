# Chace Kirwan 12.7.24
# COMSC.230 Final Project
# Prof. Omar Morales
#parallel processing or whatevr

#for plot
import matplotlib.pyplot as plt
# get data
from ucimlrepo import fetch_ucirepo
# for PP
from multiprocessing import Pool
# used to find speedup
import time
start = time.time()

# Create list of names to cycle through, already implemented into X through pandas
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# get the dataset and set to var
heart_disease = fetch_ucirepo(id=45)

# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 

# variable information 
print(X)
print("") 
print(y)
print("") 

# Group the indices by diagnosis so that it uhhgh works
diagnosis_level = {i: [] for i in range(5)}

for index, value in y['num'].items():
    if value in diagnosis_level:
        diagnosis_level[value].append(index)

# Function to compute stats for each diagnosis and print them to the terminal
def compute_stats(locations):
    filtered_X = X.loc[locations]
    stats = {}
    for column in filtered_X.columns:
        column_data = filtered_X[column]
        min_value = column_data.min()
        max_value = column_data.max()
        stats[column] = {
            'range': f"{min_value} to {max_value}",
            'average': column_data.mean()
        }
    return stats

# Function for parallel processing
def parallel_compute(locations_dict):
    with Pool(processes=4) as pool:
        results = pool.map(compute_stats, locations_dict.values())
    return results

# Main block to run the parallel buisness
if __name__ == '__main__':
    stats_list = parallel_compute(diagnosis_level)
    stats_dict = {i: stats_list[i] for i in range(5)}

    #  Function to print the stats cutely for use
    def print_stats(stats, label):
        print(f"\nStats for {label}'s:")
        for column, values in stats.items():
            print(f"{column.capitalize()}:")
            print(f"  Range: {values['range']}")
            print(f"  Average: {values['average']:.2f}")

    # Print stats to terminal
    for diagnosis, stats in stats_dict.items():
        print_stats(stats, diagnosis)

    # ------------------------------------------------------------------------------------------------------------------

    # averages for plotting
    averages_by_diagnosis = [
        [stats_dict[d][cat]['average'] for cat in column_names] for d in range(5)
    ]

    # Plotting
    fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(20, 12), constrained_layout=True)
    axes = axes.flatten()

    for i, category in enumerate(column_names):
        averages = [averages_by_diagnosis[d][i] for d in range(5)]
        axes[i].bar(['0', '1', '2', '3', '4'], averages, color=['greenyellow', 'yellow', 'orange', 'coral', 'red'])
        axes[i].set_title(category.capitalize())
        axes[i].set_xlabel('Target Value')
        axes[i].set_ylabel('Average')

    # remove extra values 
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    #print plot to new window
    plt.show()

# Save timestamp
end = time.time()

print(end - start)
# 70 percent speedup
