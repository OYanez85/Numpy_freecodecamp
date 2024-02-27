# Page View Time Series Visualizer project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Replace 'your_data_path/fcc-forum-pageviews.csv' with the actual path to your CSV file
url = "https://raw.githubusercontent.com/OYanez85/Numpy_freecodecamp/develop/fcc-forum-pageviews.csv"
data = pd.read_csv(url, parse_dates=['date'], index_col='date')

# Data Cleaning
data_cleaned = data[(data['value'] >= data['value'].quantile(0.025)) & (data['value'] <= data['value'].quantile(0.975))]

# Data visualization
import matplotlib.pyplot as plt

# Draw line plot
def draw_line_plot():
    plt.figure(figsize=(10, 5))
    plt.plot(data_cleaned.index, data_cleaned['value'], color='skyblue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('line_plot.png')  # Save the figure
    plt.show()

draw_line_plot()

# draw bar plot
import numpy as np

def draw_bar_plot():
    data_grouped = data_cleaned.groupby([data_cleaned.index.year, data_cleaned.index.month]).mean()
    data_grouped.index.names = ['Year', 'Month']
    data_grouped = data_grouped.unstack(level=0)

    data_grouped.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Daily Page Views by Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
    plt.tight_layout()
    plt.savefig('bar_plot.png')  # Save the figure
    plt.show()

draw_bar_plot()

# Draw box plot
import seaborn as sns

def draw_box_plot():
    data_box = data_cleaned.copy()
    data_box['Year'] = data_box.index.year
    data_box['Month'] = data_box.index.month_name()

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x='Year', y='value', data=data_box, ax=axes[0])
    sns.boxplot(x='Month', y='value', data=data_box, ax=axes[1], order=[calendar.month_name[i] for i in range(1, 13)])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.savefig('box_plots.png')  # Save the figure
    plt.show()

draw_box_plot()
