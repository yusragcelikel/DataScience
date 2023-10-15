import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd

dict = {"DATE":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "MONTH":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "MLY_TAVG_NORMAL":[42.1, 43.4, 46.6, 50.5, 56.0, 61.0, 65.9, 66.5, 61.6, 53.3, 46.2, 41.1]}

seattle_weather = pd.DataFrame(dict).set_index("DATE")

print(seattle_weather["MONTH"])
#fig, ax = plt.subplots()