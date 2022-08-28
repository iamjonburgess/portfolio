"""
This program takes the raw data from diamonds.csv
and organizes it into a Dataframe.
"""

# Import libraries
import numpy as np
import pandas as pd

# Read the diamonds.csv and build a Dataframe from the data
df = pd.read_csv('diamonds.csv')

print(df.head(10))

# Calculate total value of diamonds
sum = df.price.sum()
print('Total $ Value of Diamonds: ${:0,.2f}'.format(sum))

# Calculate mean price of diamonds
mean = df.price.mean()
print('Mean $ Value of Diamonds: ${:0,.2f}'.format(mean))

# Summarize the data
descrip = df.carat.describe()
