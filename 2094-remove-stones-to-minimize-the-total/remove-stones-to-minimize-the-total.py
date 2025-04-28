class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []
        
        for i in range(len(piles)):
            heapq.heappush(maxHeap, -piles[i])

        i = k
        while i > 0:
            temp = heapq.heappop(maxHeap)
            j = temp//2
            heapq.heappush(maxHeap,j)
            i -= 1
            
        return -sum(maxHeap)