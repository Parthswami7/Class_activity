import numpy as np

a = [('name', 'S15'), ('class', int), ('height', float)]

s = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]

students = np.array(s, dtype=a)
print("Original Array :")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))