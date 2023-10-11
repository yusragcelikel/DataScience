import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

np.random.seed(334)

wait_times = uniform.rvs(0, 30, size=1000)

plt.hist(wait_times)
plt.show()

