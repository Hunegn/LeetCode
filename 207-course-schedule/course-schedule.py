class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        no_cycle = True
        white = 1
        gray = 2
        black = 3
        courses = defaultdict(list)
        for course, pre in prerequisites:
            courses[course].append(pre)
        color = {course:white for course in range(numCourses)}
        def dfs(course):
            nonlocal no_cycle
            
            color[course] = gray
            if course in courses:
                for ng in courses[course]:
                    if color[ng] == white:
                        dfs(ng)
                    elif color[ng] == gray:
                        no_cycle = False
                        return
            color[course] = black
        for course in range(numCourses):
            if color[course] == white:
                dfs(course)
        return no_cycle


