class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        def dfs(course) -> bool:
            status_courses[course] = IN_PROGRESS
            
            temp = need_courses.get(course,[])

            for next_course in temp:
            	
            	if status_courses[next_course] == IN_PROGRESS:
            		return False	
            	
            	if status_courses[next_course] == ENDED:
            		continue
            	
            	if not dfs(next_course):
            		return False
            
            status_courses[course] = ENDED
            result.append(course)
            
            return True
        
        
        NOT_VISITED, IN_PROGRESS, ENDED = 0, 1, 2
        status_courses = [NOT_VISITED] * numCourses

        # Creation of the graph
        need_courses = {}
        for key, item in prerequisites:
            if key in need_courses:
                need_courses[key].append(item)
            else:
                need_courses[key] = [item]

        result = []
        for course in range(numCourses):
            # if course not in need_courses:
            #     result.append(course)
            #     continue
            if status_courses[course] == ENDED:
                continue

            if not dfs(course):
                return []

        
        return result