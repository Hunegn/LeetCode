class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)-1
        for i in range(n):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)

        return nums
        
            