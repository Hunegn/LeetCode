class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, m in edges:
            graph[i].append(m)
        print(graph)
        count = 0
        def dfs(node, visited):
            nonlocal count
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count +=1
                    
                    dfs(neighbor,visited) 
        for i in range(n):
            count = 0
            dfs(i,set())
            print(i,count)
            if count == n-1:
                return i
        return -1