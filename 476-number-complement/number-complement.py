class Solution:
    def findComplement(self, num: int) -> int:
        x = num
        bit_length = x.bit_length()
        mask = (1 << bit_length) - 1  
         
        return x ^ mask 