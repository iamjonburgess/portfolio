"""
This program takes the raw data, creates a Dataframe,
and creates a bar graph to show the number of diamonds in
each clarity type.

Note: Final line can be edited to display chart in a pop-up or
save as a .png file.
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the diamonds CSV file and build a Dataframe from the data
df = pd.read_csv('diamonds.csv')

clarityindexes = df['clarity'].value_counts().index.tolist()
claritycount = df['clarity'].value_counts().values.tolist()

print(clarityindexes)
print(claritycount)

plt.bar(clarityindexes, claritycount)
plt.show() # or plt.savefig('plot_count_clarity.png')
