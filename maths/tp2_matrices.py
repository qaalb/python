A = [[1, 0, 2], [-1, 3, 1], [2, 2, 1]]
B = [[3, 1, 4], [2, 0, 1], [0, 1, 5]]
resultat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            resultat[i][j] += A[i][k] * B[k][j]

print(resultat)
