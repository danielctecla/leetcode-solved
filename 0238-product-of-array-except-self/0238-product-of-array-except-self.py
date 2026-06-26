class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMul = []
        rightMul = []

        accum = 1
        for num in nums:
            accum *= num
            leftMul.append(accum)

        accum = 1
        for num in nums[::-1]:
            accum *= num
            rightMul.append(accum)
        rightMul = rightMul[::-1]
        
        ans = [rightMul[1]]
        for i in range(1,len(nums) - 1):
            ans.append(leftMul[i - 1] * rightMul[i + 1])
        ans.append(leftMul[-2])

        return ans


        
        