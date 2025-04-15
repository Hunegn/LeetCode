# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root,0)])
        level = defaultdict(list)
        while queue:
            node = queue.popleft()
            
            if node[0]:
                level[node[1]].append(node[0].val)
                if node[0].left: 
                    queue.append((node[0].left,node[1]+1))

                if node[0].right: 
                    queue.append((node[0].right, node[1]+1))
        
        levels = [val for key,val in level.items()]
        return levels


        