# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        queue = deque([(root,level)])
        ans = defaultdict(list)
        while queue:
            node, l = queue.popleft()
            if node:
                if l%2:
                    ans[l].append(node.val)
                queue.append((node.left,l+1))
                queue.append((node.right,l+1))
        queue = deque([(root,level)])
        i = 0
        print(ans)
        while queue:
            node, l = queue.popleft()
            if node:
                if l%2:
                    node.val = ans[l].pop()
                queue.append((node.left,l+1))
                queue.append((node.right,l+1))
        return root


        