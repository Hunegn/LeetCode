class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for i,n in edges:
            graph[i].append(n)
            graph[n].append(i)
        def dfs(source,visited):
            if source == destination:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    found =  dfs(neighbor,visited)
                    if found:
                        return found
            return False
            
        
        return dfs(source,set())
        
       

        