import matplotlib.pyplot as plt
import pandas as pd


seattle_weather = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/seattle_weather.csv", index_col=0)
seattle_weather_first_twelve = seattle_weather[:12]
austin_weather = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/austin_weather.csv", index_col=0)

medalist_weights = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/summer2016.csv", index_col=0)
mens_rowing = medalist_weights[(medalist_weights["Sex"] == "M") & (medalist_weights["Sport"] == "Rowing")]
mens_gymnastics = medalist_weights[(medalist_weights["Sex"] == "M") & (medalist_weights["Sport"] == "Gymnastics")]


# errorbar
fig1, ax1 = plt.subplots()

ax1.errorbar(seattle_weather_first_twelve["DATE"], seattle_weather_first_twelve["MLY-TAVG-NORMAL"], yerr=seattle_weather_first_twelve["MLY-TAVG-STDDEV"])
ax1.errorbar(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

ax1.set_ylabel("Temperature (Fahrenheit)")
plt.show()

# boxplot
fig2, ax2 = plt.subplots()

ax2.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

ax2.set_xticklabels(["Rowing", "Gymnastics"])
ax2.set_ylabel("Height (CM)")

plt.show()





