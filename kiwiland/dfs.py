def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        adjacents = graph[vertex]
        for next in adjacents - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
