from scipy.stats import poisson

prob_4 = poisson.pmf(5, 4) #lambda is 4
print(prob_4)

prob_cowrkr = poisson.pmf(5, 5.5)
print(prob_cowrkr)

prob_3_or_less = poisson.cdf(3, 4) #lambda is 4
print(prob_3_or_less)

prob_over_11 = 1 - poisson.cdf(11, 4)
print(prob_over_11)
