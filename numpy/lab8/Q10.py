import numpy as np




print(np.random.rand(3,2))


print(np.random.randint(1,10,size=(3,2)))


print(np.random.randn(3,2))


arr = np.array([1,2,3,4,5])
print(np.random.choice(arr, size=(3,2)))    


np.random.seed(42)
print(np.random.rand(3,2))
