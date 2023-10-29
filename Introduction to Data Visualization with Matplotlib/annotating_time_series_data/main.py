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

