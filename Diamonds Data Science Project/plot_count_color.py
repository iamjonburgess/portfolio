"""
This program takes the raw data, creates a Dataframe,
and creates a bar graph to show the number of diamonds in
each color type.

Note: Final line can be edited to display chart in a pop-up or
save as a .png file.
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the diamonds CSV file and build DataFrame
df = pd.read_csv('diamonds.csv')

# Count the number of each textual type of color

colorindexes = df['color'].value_counts().index.tolist()
colorcount = df['color'].value_counts().values.tolist()

print(colorindexes)
print(colorcount)

plt.bar(colorindexes, colorcount)
plt.show() # or plt.savefig('plot_count_color.png')
