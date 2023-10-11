from scipy.stats import binom

# winning 3 out of three with 30% of winning chance
prob_3_out_of_3 = binom.pmf(3, 3, 0.3)
print("\nwinning 3 out of three with 30% of winning chance:", prob_3_out_of_3)

# winning <= 1 out 3  with 30% of winning chance
prob_less_than_or_equal = binom.cdf(1, 3, 0.3)
print("\nwinning <= 1 out 3  with 30% of winning chance:", prob_less_than_or_equal)

# winning > 1 out 3  with 30% of winning chance
prob_greater_than = 1 - binom.cdf(1, 3, 0.3)
print("\nwinning > 1 out 3  with 30% of winning chance:", prob_greater_than)

