from scipy.stats import expon

exp_1 = expon.cdf(1, scale=2.5) #less than 1 hour, scale is 2.5
print(exp_1)

exp_2 = 1 - expon.cdf(4, scale=2.5) #greater than 4 hour, scale is 2.5
print(exp_2)

exp_3 = expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5)
print(exp_3)