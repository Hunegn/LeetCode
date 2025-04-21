# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        queue = deque([(root,level)])
        ans = defaultdict(list)
        while queue:
            node, l = queue.popleft()
            if node:
                if l%2:
                    ans[l].insert(0,node.val)
                    
                else:
                    ans[l].append(node.val)
                queue.append((node.left,l+1))
                queue.append((node.right,l+1))
        return list(ans.values())


