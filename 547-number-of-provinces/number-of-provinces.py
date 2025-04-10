class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        adj_list = [[] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    adj_list[i+1].append(j+1)
        def dfs(node, visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        count = 0
        for i in range(1,n+1):
            if i not in visited:
                count += 1
                dfs(i, visited)
        return count
