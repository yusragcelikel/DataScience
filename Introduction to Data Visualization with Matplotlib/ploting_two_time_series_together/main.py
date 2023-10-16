import matplotlib.pyplot as plt
import pandas as pd


climate_change = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/climate_change.csv", parse_dates=["date"], index_col="date")

fig, ax = plt.subplots()

ax.plot(climate_change.index, climate_change["co2"])

ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)")

plt.show()