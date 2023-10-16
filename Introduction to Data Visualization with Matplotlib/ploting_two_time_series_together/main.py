import matplotlib.pyplot as plt
import pandas as pd

# parse the date column as date and set date column as index
climate_change = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/climate_change.csv", parse_dates=["date"], index_col="date")
ninety_eight = climate_change["1998-01-01" : "1998-12-31"]

fig, ax = plt.subplots()

ax.plot(climate_change.index, climate_change["co2"])
#ax.plot(ninety_eight.index, ninety_eight["co2"])

ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)")

#define ax2
ax2 = ax.twinx()

ax2.plot(climate_change.index, climate_change["relative_temp"])

# Since same x-axes different y-axes
ax2.set_ylabel("Relative temperature (Celsius)")

plt.show()