class Solution:
    def minimumSteps(self, s: str) -> int:
        total_operations = 0
        n = len(s)
        left = n - 1
        right = n - 1
        
        while left >= 0:
            
            if left == right and s[left] == "1":
                right -= 1
            elif s[left] == "1":
                total_operations += right - left
                right -= 1
            
            left -= 1
        
        return total_operations
        