class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = max(piles)

        left = 1
        right = min_k

        while left <= right:
            mid_k = (right + left) // 2

            total_hours = 0
            valid = True
            
            for pile in piles:  
                
                total_hours += math.ceil(pile / mid_k)

                if total_hours > h:
                    valid = False
                    break
            
            if valid == True:
                print(total_hours)
                min_k = min(min_k, mid_k)
            
            if valid:
                right = mid_k - 1
            else:
                left = mid_k + 1
        
        return min_k
                
                
