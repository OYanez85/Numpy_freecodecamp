# Load the Dataset:

import pandas as pd
data_url = 'https://raw.githubusercontent.com/OYanez85/Numpy_freecodecamp/develop/epa-sea-level.csv'
df = pd.read_csv(data_url)

# Create a Scatter Plot

import matplotlib.pyplot as plt
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Linear Regression Analysis

from scipy.stats import linregress
regression_result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the Line of Best Fit:

import numpy as np
years_extended = np.arange(df['Year'].min(), 2051)
sea_level_predicted = regression_result.intercept + regression_result.slope * years_extended
plt.plot(years_extended, sea_level_predicted, 'r')

# Analyze Data from Year 2000 Onwards

new_df = df[df['Year'] >= 2000]
new_regression_result = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
new_years_extended = np.arange(2000, 2051)
new_sea_level_predicted = new_regression_result.intercept + new_regression_result.slope * new_years_extended
plt.plot(new_years_extended, new_sea_level_predicted, 'g')

# Save the plot

plt.savefig('sea_level_plot.png')
