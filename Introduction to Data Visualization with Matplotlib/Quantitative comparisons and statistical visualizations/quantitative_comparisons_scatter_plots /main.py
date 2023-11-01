import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/climate_change.csv", index_col=0)

eighties = climate_change["1980":"1989"]
nineties = climate_change["1990":"1999"]


fig1, ax1 = plt.subplots()

ax1.scatter(climate_change["co2"], climate_change["relative_temp"])

ax1.set_xlabel("CO2 (ppm)")
ax1.set_ylabel("Relative temperature (Celsius)")

plt.show()

fig2, ax2 = plt.subplots()

ax2.scatter(eighties["co2"], eighties["relative_temp"], color="red", label="eighties")
ax2.scatter(nineties["co2"], nineties["relative_temp"], color="blue", label="nineties")
ax2.legend()

ax2.set_xlabel("CO2 (ppm)")
ax2.set_ylabel("Relative temperature (Celsius)")


plt.show()
