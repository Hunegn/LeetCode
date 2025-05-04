
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Append original indices to tasks
        for i, task in enumerate(tasks):
            task.append(i)
        
        # Sort tasks by enqueue time
        tasks.sort()
        
        result = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or heap:
            # If no tasks are in the heap, advance time to the next task's enqueue time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            
            # Add all tasks that are available by current time to the heap
            while i < n and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if heap:
                processing_time, index = heapq.heappop(heap)
                time += processing_time
                result.append(index)
        
        return result
