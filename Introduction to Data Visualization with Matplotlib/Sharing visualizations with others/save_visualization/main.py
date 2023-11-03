import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/medals_by_country_2016.csv", index_col=0)

fig, ax = plt.subplots()

ax.bar(medals.index, medals["Gold"])

ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")

fig.set_size_inches([5, 4])

#lfig.savefig("gold_medals.jpg", quality=50)

plt.tight_layout()

fig.savefig("gold_medals_2.png")
fig.savefig("gold_medals_dpi300.png", dpi=300)




