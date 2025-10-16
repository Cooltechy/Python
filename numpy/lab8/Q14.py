import numpy as np


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)  
