class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        graph_counter = {i:edge for i,edge in enumerate(graph)}
        white = 0
        black = 1
        gray = 2
        is_bipartite = True
        color = {i:gray for i in range(len(graph))}
        def dfs(node, visited):
            nonlocal is_bipartite
            visited.add(node)
            for neighbor in graph_counter[node]:
                if color[neighbor] == color[node]:
                    is_bipartite = False
                    return
                elif neighbor not in visited:
                    if color[node]:
                        color[neighbor] = white
                    else:
                        color[neighbor] = black
                    dfs(neighbor,visited)
        for i, g in enumerate(graph):
            if color[i] == gray:
                color[i] = white
                dfs(i,set())
        return is_bipartite

        