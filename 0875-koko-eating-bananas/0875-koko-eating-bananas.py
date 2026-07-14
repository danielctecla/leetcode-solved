class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        right = k
        left = 1
        n = len(piles)
        
        while left <= right:
            k = (left + right) // 2
            hours_taken = 0

            for pile in piles:
                curr_hours = (pile + k - 1) // k
                hours_taken += curr_hours

                if hours_taken > h:
                    break

            if hours_taken <= h:
                right = k - 1
            else:
                left = k + 1
        
        return left