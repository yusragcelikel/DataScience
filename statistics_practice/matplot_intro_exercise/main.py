import matplotlib.pyplot as plt
import pandas as pd

# create the data
dict1 = {"DATE":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "MONTH":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "MLY_TAVG_NORMAL":[42.1, 43.4, 46.6, 50.5, 56.0, 61.0, 65.9, 66.5, 61.6, 53.3, 46.2, 41.1]}
dict2 = {"DATE":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "MONTH":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "MLY_TAVG_NORMAL":[22.1, 23.4, 26.6, 30.5, 36.0, 41.0, 55.9, 56.5, 51.6, 33.3, 26.2, 21.1]}

# data from dictionary to DataFrame and set the index to the MONTH column
seattle_weather = pd.DataFrame(dict1).set_index("DATE")
austin_weather = pd.DataFrame(dict2).set_index("DATE")

# create figure object and axes object
fig, ax = plt.subplots()

# add data to axes
#ax.plot(seattle_weather["MONTH"], seattle_weather["MLY_TAVG_NORMAL"])


# add two data to axes
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY_TAVG_NORMAL"], color="b", marker="o", linestyle="--")
#ax.plot(austin_weather["MONTH"], austin_weather["MLY_TAVG_NORMAL"], color="r", marker="v", linestyle="--")

ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
ax.set_title("Weather in Seattle")

# show the plot
plt.show()