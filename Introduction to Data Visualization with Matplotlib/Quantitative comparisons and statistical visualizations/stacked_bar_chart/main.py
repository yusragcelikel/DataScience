import matplotlib.pyplot as plt
import pandas as pd

#Read the data in from the CSV file and use the first column as the index for the DataFrame.
medals = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/medals_by_country_2016.csv", index_col=0)

#create a Figure and an Axes object
fig, ax = plt.subplots()

#call the Axes bar method to create a bar chart and visualize the data about gold medals
ax.bar(medals.index, medals["Gold"])
# Stack the Silver data on top of the gold data
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"])
#Rotate the x-axis labels to prevent overlapping
ax.set_xticklabels(medals.index, rotation=90)
# add label to y-axis
ax.set_ylabel("Number of medals")

# Adjust figure margins to make sure labels fit within the plot
plt.tight_layout()

# Display the plot
plt.show()
