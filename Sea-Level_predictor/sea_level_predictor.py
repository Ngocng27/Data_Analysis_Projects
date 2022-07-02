import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

   def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(df['Year'].min(),2050,1)
    y = x*line.slope + line.intercept

    plt.plot(x,y)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    line2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2050,1)
    y2 = x2*line2.slope + line2.intercept

    plt.plot(x2,y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
