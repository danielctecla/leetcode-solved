class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP = 0
        rightP = len(numbers) - 1

        while leftP < rightP:
            resultOp = numbers[rightP] + numbers[leftP]
            
            if resultOp > target:
                rightP -= 1
            elif resultOp < target:
                leftP += 1
            else:
                break
        
        return [leftP + 1,rightP + 1]