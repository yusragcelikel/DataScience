import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#read the DataFrame from csv file
world_happiness_2015 = pd.read_csv("/Users/yusragokcecelikel/Downloads/archive/2015.csv")


#sns.scatterplot(x=life)

#print(world_happiness.columns)

without_trendline = sns.scatterplot(x = "Health (Life Expectancy)", y = "Happiness Score", data = world_happiness_2015)

with_trendline = sns.lmplot(x = "Health (Life Expectancy)", y = "Happiness Score", data = world_happiness_2015, ci = None)

plt.show()

#calculate of the correlation
cor = world_happiness_2015["Health (Life Expectancy)"].corr(world_happiness_2015["Happiness Score"])
print(cor)