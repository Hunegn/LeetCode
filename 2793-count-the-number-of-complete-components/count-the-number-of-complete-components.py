class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        result = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    n_nodes, n_edges = dfs(neighbor)
                    nodes += n_nodes
                    edge_count += n_edges
            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)
                
                if edge_count == nodes * (nodes - 1):
                    result += 1

        return result