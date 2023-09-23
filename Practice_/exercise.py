monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings * num_months

# Print the type of year_savings
print(type(year_savings))

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)

print("-------------------------------------------------")

# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

print("\n-------------------------------------------------\n")


import numpy as np
m = np.array([6, 2, 4])
n = 2
print(m + n)

print("\n-------------------------------------------------\n")

import numpy as np
np_arr1 = np.array([1,2,3,4])
np_arr2 = np.array([5,6,7,8])
print(np.column_stack((np_arr1, np_arr2)))