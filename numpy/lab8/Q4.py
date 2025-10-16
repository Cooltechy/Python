import numpy as np


dt = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
student = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=dt)
print(student['name'])
print(student['age'])
print(student['marks'])