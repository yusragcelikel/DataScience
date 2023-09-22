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
