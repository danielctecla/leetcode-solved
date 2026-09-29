class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        
        if len(intervals) == 0:
            return result
        
        intervals.sort(key=lambda interval: interval[0])

        initial = intervals[0][0]
        end = intervals[0][1]
        
        
        for i in range(1,len(intervals)):
        
            if intervals[i][0] <= end:
                end = max(end,intervals[i][1])
                continue
                
            result.append([initial,end])
            initial = intervals[i][0]
            end = intervals[i][1]
        
        result.append([initial,end])
        
        return result