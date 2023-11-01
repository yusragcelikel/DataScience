import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/seattle_weather.csv", index_col=0)
austin_weather = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/austin_weather.csv", index_col=0)
seattle_weather_first_twelve = seattle_weather[:12]

plt.style.use("Solarize_Light2")

fig, ax = plt.subplots()

ax.plot(seattle_weather_first_twelve["DATE"], seattle_weather_first_twelve["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"])

ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degree)")

plt.show()