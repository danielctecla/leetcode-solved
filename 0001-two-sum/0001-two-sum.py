class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            rest = target- nums[i]
            if rest in hashMap:
                return [i, hashMap[rest]]
            hashMap[nums[i]] = i