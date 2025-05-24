class Solution:
    def kidsWithCandies(self, candies: List[int], ex: int) -> List[bool]:
        max_ = max(candies)
        ans = []
        for candy in candies:
            if ex+ candy >= max_:
                ans.append(True)
            else:
                ans.append(False)
        return ans