from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if 0 <= numCourses <= 1:
            return True

        visited_courses = 0
        adj_list = [[] for _ in range(numCourses)] # adjlist
        in_degree = [0] * numCourses

        for pre in prerequisites:
            c1,c2 = pre
            adj_list[c2].append(c1) # going outward
            in_degree [c1] += 1
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            visited_courses += 1
            for nei in adj_list[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return visited_courses == numCourses        
