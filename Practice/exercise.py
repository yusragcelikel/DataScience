# '+' concatenates the lists
x = [15, 10, 2, 84] + [1, 4, 8, 7, 9]
print("x = [15, 10, 2, 84] + [1, 4, 8, 7, 9] would be:", x)

# 'count()' method been used to count the number of times the first element
# of x appears in the list x. The result is '1'
x.count(x[0])
print("x.count(x[0]) would be:", x.count(x[0]))

# we are looking for the index of '1' in the list because
# 'x.count(x[0])' is '1'
x.index(x.count(x[0]))
print("x.index(x.count(x[0])) would be:", x.index(x.count(x[0])))

print("\n --------------------------------------------------------------\n ")

# Find the mean of the first column of costs
import numpy as np
costs = np.column_stack(([3, 2, 1, 3],
                         [7, 6, 6, 5]))
mean_costs = np.mean(costs[:,0])
print(mean_costs)

