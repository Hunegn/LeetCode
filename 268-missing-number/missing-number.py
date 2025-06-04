class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_= 0
        total = 0
        n = len(nums)
        for num in nums:
            sum_^= num
        for i in range(n+1):
            total ^= i

        return total ^ sum_        
