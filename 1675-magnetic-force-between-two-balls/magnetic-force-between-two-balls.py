class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        #magnetic
        pos.sort()
        n = len(pos)
        cost = [0 for i in range(n)]
        acc = 0
        for i in range(n):
            if not i:
                cost[i] = 0
                continue
            
            acc+= pos[i]-pos[i-1]
            cost[i] = acc
        def valid(k):
            nonlocal cost
            nonlocal m
            b = m-1
            p = 0
            for i in range(1,len(cost)):
                if cost[i] - cost[p] >= k:
                    b-=1
                    p = i
                if b<=0:
                    return True
            return False
        left , right = 1, max(pos)
        ans = 1
        while left <= right:
            mid = (left+right)//2
            if valid(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans

                



        