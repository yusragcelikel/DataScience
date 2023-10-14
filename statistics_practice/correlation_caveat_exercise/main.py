import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

world_happiness_2019 = pd.read_csv("/Users/yusragokcecelikel/Downloads/archive/2019.csv")

#print(world_happiness_2019.columns)

# visualize your data
sns.scatterplot(x="Perceptions of corruption", y="GDP per capita", data=world_happiness_2019)
plt.show()

cor1 = world_happiness_2019["Perceptions of corruption"].corr(world_happiness_2019["GDP per capita"])
print(cor1)



