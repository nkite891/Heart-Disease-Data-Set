# Chace Kirwan 11.27.24
# COMSC.230 Final Project
# Prof. Omar Morales
#find the max and min values for each column



from ucimlrepo import fetch_ucirepo 
import pandas as dataAnalysis
# Create list of names to cycle through
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
print(heart_disease.metadata) 
  
# variable information 
print(heart_disease.variables)
print("") 
print(X)
print("") 
print(y)

for column_name in column_names:
    min_value = X[column_name].min()
    max_value = X[column_name].max()
    range_formatted = f"{min_value} to {max_value}"
    print(f"The range of the '{column_name}' column is: {range_formatted}\n")

print(y.min())
print(y.max())
