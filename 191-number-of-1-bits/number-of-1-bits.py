class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        num = n
        while num:
            if num%2:
                count+=1
            num = num//2
        return count
