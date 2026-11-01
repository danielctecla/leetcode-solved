class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []

        def bactraking(index: int):
            if index == len(nums):
                ans.append(current.copy())
                return
            
            current.append(nums[index])
            bactraking(index + 1)

            current.pop()
            bactraking(index + 1)
        
        bactraking(0)

        return ans