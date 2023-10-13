import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#read the DataFrame from csv file
world_happiness = pd.read_csv("/Users/yusragokcecelikel/Downloads/archive/2015.csv")


#sns.scatterplot(x=life)

#print(world_happiness.columns)

sns.scatterplot(x = "Health (Life Expectancy)", y = "Happiness Score", data = world_happiness)
plt.show()