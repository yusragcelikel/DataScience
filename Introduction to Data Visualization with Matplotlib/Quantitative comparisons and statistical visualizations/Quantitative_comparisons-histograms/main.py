import matplotlib.pyplot as plt
import pandas as pd

medalist_weights = pd.read_csv("/Users/yusragokcecelikel/Downloads/CSV files/8. Introduction to Data Visualization with Matplotlib/summer2016.csv", index_col=0)

mens_rowing = medalist_weights[(medalist_weights["Sex"] == "M") & (medalist_weights["Sport"] == "Rowing")]
mens_gymnastics = medalist_weights[(medalist_weights["Sex"] == "M") & (medalist_weights["Sport"] == "Gymnastics")]

fig, ax = plt.subplots()

ax.hist(mens_rowing["Height"], label="Rowing", bins=[150, 160, 170, 180, 190, 200, 210], histtype="step")
ax.hist(mens_gymnastics["Height"], label="Gymnastics", bins=[150, 160, 170, 180, 190, 200, 210], histtype="step")

ax.set_xlabel("Height (cm)")
ax.set_ylabel("Number of observations")

ax.legend()
plt.show()
