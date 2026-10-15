class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            distance = right - left
            min_height = min(height[left], height[right])

            area = distance * min_height
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
