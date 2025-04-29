class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-num for num in piles ]
        heapq.heapify(maxHeap)
        i = 0
        while i < k:
            temp = heapq.heappop(maxHeap)
            j = temp//2
            heapq.heappush(maxHeap,j)
            i += 1
            
        return -sum(maxHeap)