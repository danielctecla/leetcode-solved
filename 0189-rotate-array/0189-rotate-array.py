class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        for i in range(len(nums)):
            index = (i + k)%len(nums)
            nums[index] = temp[i]
            

        