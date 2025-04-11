class Solution:
    def numOfMinutes(self, n: int, head: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = [[] for _ in range(n)]
        for i, num in enumerate(manager):
            if num != -1:
                adj_list[num].append(i)
        total_time = informTime[head]
        print(total_time)
        def dfs(node,visited):
            if node in visited:
                return 0
            visited.add(node)
            max_time = 0
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    max_time = max(max_time,dfs(neighbor,visited))
            return informTime[node] + max_time
        print(adj_list)
        
        return dfs(head,set())
