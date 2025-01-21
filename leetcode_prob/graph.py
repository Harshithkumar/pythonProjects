def longestcycle(edges):
    n = len(edges)
    visited = [-1] * n
    max_cycles_len = -1

    for start_node in range(n):
        if visited[start_node] != -1:
            continue
        current_node = start_node
        index_map = {}
        step = 0

        while current_node != -1:
            if visited[current_node] != -1:
                if current_node in index_map:
                    cycle_len = step - index_map[current_node]
                    max_cycles_len = max(max_cycles_len, cycle_len)
                break
            visited[current_node] = start_node
            index_map[current_node] = step
            step += 1
            current_node = edges[current_node]
    return max_cycles_len


edges = [3, 3, 4, 2, 3]
print(longestcycle(edges))
