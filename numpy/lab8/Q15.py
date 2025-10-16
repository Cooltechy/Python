import numpy as np



a = np.random.randint(1, 100, size=(4,4))
symmetric_a = (a + a.T)/2
print("Symmetric Matrix:\n", symmetric_a)
print("Median of all elements:", np.median(symmetric_a))
print("Median along rows:", np.median(symmetric_a, axis=1))
print("Median along columns:", np.median(symmetric_a, axis=0))  
