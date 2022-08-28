"""
This program takes the raw data, organizes it into a dataframe,
and creates a plot chart of the data.

Note: Final line can be edited to display chart in a pop-up or
save as a .png file.
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the diamonds CSV file and build a Dataframe from the data
df = pd.read_csv('diamonds.csv')

carat = df.carat
clarity = df.clarity
plt.scatter(clarity, carat)
plt.show() # or plt.savefig('clarity_vs_carat.png')
