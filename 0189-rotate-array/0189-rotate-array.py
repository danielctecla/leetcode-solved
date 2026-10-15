class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity O(n)
        # Space complexity O(n)
        nums_size = len(nums)
        copy_nums = nums.copy()
        k = k % nums_size
        
        for i in range(nums_size):
            index = (i + k) % nums_size
            nums[index] = copy_nums[i]

        return None
            

        
# [1,2,3,4,5,6,7]
# nums_size = 7
# copy [1,2,3,4,5,6,7]
# k = 3 % 7 = 3
# index = 5 + 3 % 7 = 0
# [5,6,7,1,2,3,4]
