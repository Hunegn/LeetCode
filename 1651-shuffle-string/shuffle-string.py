class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0 for i in range(len(indices))]
        for i, char in enumerate(s):
            ans[indices[i]] = char
        return "".join(ans)
        