class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permuted = []
        def perm(nums, arr):
            if len(nums) == 1:
               
                arr.append(nums[0])
                permuted.append(arr)
                return
            for i, num in enumerate(nums):
                
                if i+1 < len(nums):
                    new_nums = nums[:i]+nums[i+1:]
                    
                else:
                    new_nums = nums[:i]
                    
                perm(new_nums,arr+ [num])
                
        perm(nums,[])
        return permuted
        