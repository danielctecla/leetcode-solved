class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        
        k = piles[-1]
        right = piles[-1]
        left = 1

        while left <= right:
            k = (left + right) // 2
            
            n = len(piles)

            hours_taken = 0
            for i in range(n - 1, -1, -1):
                if hours_taken > h:
                    break

                if piles[i] < k:
                    hours_taken += i + 1
                    break
                
                curr_hours = math.ceil(piles[i] / k)
                hours_taken += curr_hours

            if hours_taken <= h:
                right = k - 1
            else:
                left = k + 1
        return left