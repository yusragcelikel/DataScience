import matplotlib.pyplot as plt
import pandas as pd

#Read the data in from the CSV file and use the first column as the index for the DataFrame.
medals = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/medals_by_country_2016.csv", index_col=0)

#create a Figure and an Axes object
fig, ax = plt.subplots()

#call the Axes bar method to create a bar chart and visualize the data about gold medals
ax.bar(medals.index, medals["Gold"])

plt.show()