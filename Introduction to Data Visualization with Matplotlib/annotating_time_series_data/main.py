import matplotlib.pyplot as plt
import pandas as pd

#read the CSV file, parse the "date" column as datetime data, and set the "date" column as the index for the "climate_change" DataFrame
climate_change = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/climate_change.csv", parse_dates=["date"], index_col="date")

#define the time series function
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.tick_params("y", colors=color)

fig, ax = plt.subplots()

#Use the plot_timeseries function to plot CO2 levels against time in blue.
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

#Create ax2, as a twin of the first Axes
ax2 = ax.twinx()

#In ax2, use the plot_timeseries function to plot temperature against time in red.
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], 'red', "Time (years)", "Relative temp (Celsius)")

#Annotate the data.
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={"arrowstyle":"->"})
#ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={"arrowstyle":"->", "color":"gray"})

plt.show()