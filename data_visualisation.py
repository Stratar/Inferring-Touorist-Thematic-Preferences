import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def bar_charts(df):
    fig, axs = plt.subplots(2, 4, sharex=True, sharey=True)
    # Iterate over each column in the DataFrame
    i, j = 0, 0

    for column, ax in zip(df.columns, axs.flatten()):
        ax.grid(True)
        if j > 3: j = 0
        # Create a bar plot for the current column, colored by the grouped 'D Age' column
        sns.barplot(x=df.index, y=column, data=df, palette='viridis', ax=axs[i][j])
        # Set the title of the plot to the current column name
        plt.title(column)
        plt.legend(loc='upper right')
        # Rotate x-axis labels for better visibility
        plt.xticks(rotation=75)
        if j == 3: i += 1
        j += 1
        # Display the plot
    plt.show()

