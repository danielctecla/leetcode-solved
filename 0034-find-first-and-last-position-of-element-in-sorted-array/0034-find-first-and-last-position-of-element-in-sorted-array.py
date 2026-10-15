# Time complexity O(log n)
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_limit = -1
        right_limit = -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            value = nums[mid]
            # print(f"{mid}: {value}")
            if value == target:
                left_limit = mid
            if target <= value:
                right = mid - 1
            else:
                left = mid + 1
        
        if left_limit == -1:
            return [left_limit,right_limit]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            value = nums[mid]

            if value == target:
                right_limit = mid
            
            if target >= value:
                left = mid + 1
            else:
                right = mid - 1
        
        return [left_limit,right_limit]