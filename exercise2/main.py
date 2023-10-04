import numpy as np
np.random.seed(123)
tails = [0]
for x in range(10) :
    print("x:", x)
    coin = np.random.randint(0, 2)
    print("coin:", coin)
    print("tails[x] :", tails[x])
    tails.append(tails[x] + coin)
    print("tails list:", tails )
    print("tails[x] + coin :", tails[x] + coin)
    print("tails list after one loop:", tails)
print("final tails:", tails)
count = 0
for item in tails:
    count = count + 1
print(count)