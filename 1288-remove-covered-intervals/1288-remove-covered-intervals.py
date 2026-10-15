class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        
        for i in range(len(intervals)):
            covered = False
            a,b = intervals[i]
            for j in range(len(intervals)):
                c,d = intervals[j]
                
                if i != j and c <= a and b <= d:
                    covered = True
                    break
            
            if not covered:
                count += 1

        return count