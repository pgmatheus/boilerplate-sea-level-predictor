import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df2 = df[(df['Year']>=2000)]

    # Create scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(data= df, x = 'Year', y = 'CSIRO Adjusted Sea Level').set_title('Rise in Sea Level')
    slope, intercept, r_value, p_value, slope_std_error = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope2, intercept2, r_value2, p_value2, slope_std_error2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    yvalues = list(range(1880,2051)*slope + intercept)

    # Create second line of best fit
    yvalues2 = list(range(2000,2051)*slope2 + intercept2) 

    # Plot labels 
    plt.plot(list(range(1880,2051)), yvalues)
    plt.plot(list(range(2000,2051)), yvalues2)
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()