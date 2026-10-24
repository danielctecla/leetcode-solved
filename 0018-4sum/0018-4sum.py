class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        if n < 4:
            return []

        answer = []
        nums.sort()

        for a in range(n - 3):
            if a >= 1 and nums[a - 1] == nums[a]:
                continue
            for b in range(a + 1, n - 2):
                if b >= a + 2 and nums[b - 1] == nums[b]:
                    continue
                for c in range(b + 1, n - 1):
                    if c >= b + 2 and nums[c - 1] == nums[c]:
                        continue
                    for d in range(c + 1, n):
                        
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            answer.append([nums[a],nums[b],nums[c],nums[d]])
                            break

        return answer