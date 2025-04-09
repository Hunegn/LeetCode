"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
       
        id_map = {row.id:[row.importance,row.subordinates] for row in employees}
        val = 0
       
        def dfs(visited,id):
            nonlocal val
            val += id_map[id][0]
            visited.add(id)
            for sub in id_map[id][1]:
                if sub not in visited:
                    dfs(visited,sub)
            
        dfs(set(),id)
        return val

        