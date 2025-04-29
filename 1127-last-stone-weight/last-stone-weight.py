class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapify(heap)
        while len(heap) > 1:
            y,x  = heappop(heap), heappop(heap)
            if x  > y:
                heappush(heap, y-x)
        if heap:
            return -heap[0]
        
        return 0