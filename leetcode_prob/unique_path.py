def unique_path(m, n):
    matrix = [[1] * n for _ in range(m)]
    print(matrix)
    for i in range(1,m):
        for j in range(1,n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[m-1][n-1]


result = unique_path(3, 7)
print(result)
