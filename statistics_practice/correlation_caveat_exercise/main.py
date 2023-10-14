import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mammal_sleep_data = pd.read_csv("/Users/yusragokcecelikel/Downloads/msleep.csv")

#print(mammal_sleep_data.columns)

# visualize your data
sns.scatterplot(x="bodywt", y="awake", data=mammal_sleep_data)
plt.show()

cor1 = mammal_sleep_data["bodywt"].corr(mammal_sleep_data["awake"])
print(cor1)


# perform log transformation to make your data more linear
mammal_sleep_data["log_bodywt"] = np.log(mammal_sleep_data["bodywt"])

# review the scatter plot of transformed data
sns.scatterplot(x="log_bodywt", y="awake", data=mammal_sleep_data)
plt.show()

# see the correlation of transformed data
cor2 = mammal_sleep_data["log_bodywt"].corr(mammal_sleep_data["awake"])
print(cor2)