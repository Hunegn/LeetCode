class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        new_graph = [[] for i in range(len(graph))]
        incoming = {i:len(row) for i, row in enumerate(graph)}
        for i in range(len(graph)):
            for  num in graph[i]:
                new_graph[num].append(i)
        queue = deque([])
        for key, val in incoming.items():
            if val== 0:
                queue.append(key)
        order = []
        while queue:
            safe = queue.popleft()
            order.append(safe)
            for edge in new_graph[safe]:
                incoming[edge]-=1
                if incoming[edge] == 0:
                    queue.append(edge)
        return sorted(order)