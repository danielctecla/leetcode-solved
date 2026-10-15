class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0],-x[-1]))
        count = 0
        end = 0

        for l,r in intervals:
            count += r > end
            end = max(end, r)
            

        return count