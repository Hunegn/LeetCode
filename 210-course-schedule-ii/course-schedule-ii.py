class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = [[] for i in range(numCourses)]
        incoming = {i:0 for i in range(numCourses)}
        for course, pre in prerequisites:
            pres[pre].append(course)
            incoming[course]+=1
        queue = deque([])
        for key, val in incoming.items():
            if val == 0:
                queue.append(key)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for edge in pres[course]:
                incoming[edge]-=1
                if incoming[edge] == 0:
                    queue.append(edge)
        if len(order) != numCourses:
            return []
        return order

        