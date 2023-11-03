import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/medals_by_country_2016.csv", index_col=0)

fig, ax = plt.subplots()

ax.bar(medals.index, medals["Gold"])

ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")

fig.savefig("gold_medals.png")



plt.show()