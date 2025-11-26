class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [0] * numCourses  

        def dfs(node):
            if visited[node] == 1:
                return False       
            if visited[node] == 2:
                return True          

            visited[node] = 1         

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2         
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
