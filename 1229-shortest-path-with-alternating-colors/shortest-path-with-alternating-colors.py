class Solution:
    def shortestAlternatingPaths(self,n, redEdges, blueEdges):
        red_adj = [[] for _ in range(n)]
        blue_adj = [[] for _ in range(n)]
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        res = [-1] * n
        
        visited = [[False, False] for _ in range(n)]
        queue = deque()
        queue.append((0, 0)) 
        queue.append((0, 1))  
        visited[0][0] = visited[0][1] = True
        steps = 0

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if res[node] == -1:
                    res[node] = steps
                next_color = 1 - color
                next_adj = blue_adj if next_color == 1 else red_adj
                for neighbor in next_adj[node]:
                    if not visited[neighbor][next_color]:
                        visited[neighbor][next_color] = True
                        queue.append((neighbor, next_color))
            steps += 1

        return res

            