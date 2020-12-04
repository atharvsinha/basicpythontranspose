import numpy as np
m, n = input('Enter 2 space separated integers as dimensions of an m.n 2D matrix:').split()
m, n = int(m), int(n)
matrix = np.array(list(map(int, input('Enter m.n values to be inserted in the matrix').split())))
matrix = np.reshape(matrix, (m, n))
print(matrix)
transposed =[]
[[transposed.append(matrix[j][i]) for j in range(m)] for i in range(n)]
print(np.reshape(np.array(transposed), (n, m)))
