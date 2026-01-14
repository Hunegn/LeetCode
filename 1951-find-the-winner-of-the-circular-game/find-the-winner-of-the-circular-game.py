class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls = [i+1 for i in range(n)]
        i = 0
        while len(ls) > 1:
            n = len(ls)
            r=  (i+ k-1)% n
            print(r)
            ls.pop(r)
            i = r
        return ls[0]
