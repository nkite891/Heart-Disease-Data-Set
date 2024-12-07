# Chace Kirwan 12.7.24
# COMSC.230 Final Project
# Prof. Omar Morales
# DO THE GOSH DARN LINEAR REGRESSION
from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

heart_disease = fetch_ucirepo(id=45) 

X = heart_disease.data.features
y = heart_disease.data.targets

y = np.array(y)

data = pd.DataFrame(X)
data['target'] = y

data = data.dropna()
X = data.drop(columns=['target'])
y = data['target']

print("Columns in dataset:", X.columns)

for column in X.columns:
    print(f"Processing column: {column}")  
    X_column = X[[column]].values  
    
    model = LinearRegression()
    model.fit(X_column, y)
    
    y_pred = model.predict(X_column)
    
    plt.figure(figsize=(6, 4))
    plt.scatter(X_column, y, color='blue', alpha=0.3, s=30, label='Data points')  # Scatter plot
    plt.plot(X_column, y_pred, color='black', linestyle='dotted', linewidth=1.5, label='Regression line')  # Dotted black regression line
    plt.title(f'{column} vs Target', fontsize=12)
    plt.xlabel(column, fontsize=10)
    plt.ylabel('Target', fontsize=10)
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)
    plt.legend(fontsize=9)
    plt.show()
