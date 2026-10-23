from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        def dfs(node: int):
            if status[node] == VISITING:
                return False
            
            if status[node] == DONE:
                return True
            
            status[node] = VISITING
            for next in graph[node]:
                result = dfs(next)
                if not result:
                    return False
            
            status[node] = DONE
            
            return True
            
        graph = defaultdict(list)
        UNVISITED, VISITING, DONE = 0,1,2
        status = [UNVISITED] * numCourses
         
        for key, value in prerequisites:
            graph[key].append(value)
            
        for node in list(graph.keys()):
            
            result = dfs(node)
            if not result:
                return False

        return True