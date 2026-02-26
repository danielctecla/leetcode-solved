class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2,len(nums)):
            current = nums[i]
            maxCurrent = 0
            for j in range(i - 2,-1,-1):
                if current + nums[j] > maxCurrent:
                    maxCurrent = current + nums[j]
            nums[i] = maxCurrent
            ans = max(ans, nums[i])
        return ans