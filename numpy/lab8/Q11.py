import numpy as np

rarr = np.random.randint(1, 1000, size=100)


count_div_by_3 = np.sum(rarr % 3 == 0)

print("Count of numbers divisible by 3:", count_div_by_3)