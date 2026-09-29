class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        right = 0
        left = 0
        min_size = 10**5 + 1

        while right < len(nums):
            total += nums[right]

            while total >= target:
                min_size = min(right - left + 1, min_size)
                total -= nums[left]
                left += 1
            
            right += 1

        return min_size if min_size != 10**5 + 1 else 0          
