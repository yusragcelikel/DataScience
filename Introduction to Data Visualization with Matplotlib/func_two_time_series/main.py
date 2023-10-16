import matplotlib.pyplot as plt
import pandas as pd

#
climate_change = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/climate_change.csv", parse_dates=["date"], index_col="date")

#define the time series function
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.tick_params("y", colors=color)

fig, ax = plt.subplots()

# timeseries function use for ax
plot_timeseries(ax, climate_change.index, climate_change["co2"], "red", "Time", "CO2 (ppm)")

#define ax2
ax2 = ax.twinx()

# timeseries function use for ax2
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "blue", "Time", "Relative Temperature (Celsius)")

plt.show()

