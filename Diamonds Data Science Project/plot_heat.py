"""
This program takes the raw data, creates a Dataframe,
and creates a heat plot to show the number of diamonds in
each clarity type.

Note: Final line can be edited to display chart in a pop-up or
save as a .png file.
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Diamonds CSV file and Build a DataFrame
df = pd.read_csv('diamonds.csv')

# Drop the index column
df = df.drop('Unnamed: 0', axis = 1)

f, ax = plt.subplots(figsize = (10, 8))
corr = df.corr()
print(corr)
sns.heatmap(corr, mask = np.zeros_like(corr, dtype = bool),
    cmap = sns.diverging_palette(220, 10, as_cmap = True),
        square = True, ax = ax)

plt.show() # or plt.savefig('plot_heat.png')
