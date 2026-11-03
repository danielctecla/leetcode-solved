class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        inc_prefix = [1] * n
        dec_prefix = [1] * n
        
        for i in range(1,n):
            if security[i] <= security[i-1]:
                dec_prefix[i] += dec_prefix[i-1]
        
        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                inc_prefix[i] += inc_prefix[i+1]
        
        good_days = []
        for i in range(time,n):
            if dec_prefix[i] > time and inc_prefix[i] > time:
                good_days.append(i)
        
        return good_days