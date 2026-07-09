class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            
            while left < right:
                result = nums[i] + nums[left] + nums[right]

                if result == 0:
                    lastI = nums[i]
                    triplets.append([nums[i],nums[left],nums[right]])
                    
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right-= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif result > 0:
                    right -= 1
                else:
                    left += 1

        return triplets


# after found a triplet, order it and then check if it's in the ans

# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]
# i = 0 
# -1

# j = i + 1 -> j = 1
# 0

# k = j + 1  -> k = 2
# 1
#if found pass to the next number (break this loop)