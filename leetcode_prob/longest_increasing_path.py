def longest_increasing_path(mat):
    if not mat or not mat[0]:
        return 0

    m, n = len(mat), len(mat[0])
    memo = [[-1] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y):
        if memo[x][y] != -1:
            return memo[x][y]
        max_len = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] > mat[x][y]:
                max_len = max(max_len, 1 + dfs(nx, ny))

        memo[x][y] = max_len
        return max_len

    max_path = 0
    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(i, j))
    return max_path


mat = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print(longest_increasing_path(mat))
