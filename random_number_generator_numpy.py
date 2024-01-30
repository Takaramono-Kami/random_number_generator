# in the name of ALLAH

# import library that we need

import numpy as np
# import matplotlib.pyplot as plt
from random_number_generator import linear_congruential_generator

# get 100 random number by uniform distribution
print(np.random.uniform(0,1,100))

# get 1000 random number with normal distribution
mu = 0
sigma = 1
random_list = np.random.normal(mu, sigma, 1000)
print(random_list)

# count, bins, ignored = plt.hist(random_list, 30, density=True)

# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')

# plt.show()
