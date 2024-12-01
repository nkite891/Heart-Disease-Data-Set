# Chace Kirwan 11.27.24
# COMSC.230 Final Project
# Prof. Omar Morales
#find the max and min values for each column

import matplotlib.pyplot as plt
# 'pip install matplotlib' if not available
from ucimlrepo import fetch_ucirepo 
# Create list of names to cycle through
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
#print(heart_disease.metadata) 
  
# variable information 
#print(heart_disease.variables)
#print("") 
print(X)
print("") 
print(y)
print("") 
for column_name in column_names:
    min_value = X[column_name].min()
    max_value = X[column_name].max()
    range_formatted = f"{min_value} to {max_value}"
    print(f"The range of the '{column_name}' column is: {range_formatted}\n")

#print(y.min())
#print(y.max())

#make list of where each diagnosis is in y
locations_0 = []
locations_1 = []
locations_2 = []
locations_3 = []
locations_4 = []

# Iterate through y to find the locations of each diagnosis for comparison
for index, value in y['num'].items():
    if value == 0:
        locations_0.append(index)
    elif value == 1:
        locations_1.append(index)
    elif value == 2:
        locations_2.append(index)
    elif value == 3:
        locations_3.append(index)
    elif value == 4:
        locations_4.append(index)

# finds the range and average of each stat for the inputted list
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

# Compute stats for each value in y
stats_0 = compute_stats(locations_0)
stats_1 = compute_stats(locations_1)
stats_2 = compute_stats(locations_2)
stats_3 = compute_stats(locations_3)
stats_4 = compute_stats(locations_4)

# Prints the info in a way that doesnt make you want to puke
def print_stats(stats, label):
    print(f"\nStats for {label}'s:")
    for column, values in stats.items():
        print(f"{column.capitalize()}:")
        print(f"  Range: {values['range']}")
        print(f"  Average: {values['average']:.2f}")

print_stats(stats_0, 0)
print_stats(stats_1, 1)
print_stats(stats_2, 2)
print_stats(stats_3, 3)
print_stats(stats_4, 4)

# ------------------------------------------------------------------------------------------------------------------

# Create histograms for each category 
categories = column_names

# Extracting averages for plotting (evilly)
averages_0 = [stats_0[cat]['average'] for cat in categories]
averages_1 = [stats_1[cat]['average'] for cat in categories]
averages_2 = [stats_2[cat]['average'] for cat in categories]
averages_3 = [stats_3[cat]['average'] for cat in categories]
averages_4 = [stats_4[cat]['average'] for cat in categories]

# Plotting (evilly)
fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(20, 12), constrained_layout=True)
axes = axes.flatten()

for i, category in enumerate(categories):
    averages = [averages_0[i], averages_1[i], averages_2[i], averages_3[i], averages_4[i]]
    axes[i].bar(['0', '1', '2', '3', '4'], averages, color=['blue', 'orange', 'green', 'red', 'purple'])
    axes[i].set_title(category.capitalize())
    axes[i].set_xlabel('Target Value')
    axes[i].set_ylabel('Average')

# Removing extras 
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.show()
