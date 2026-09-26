class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_nums = []
        max_number =  -10**5-1

        for i in range(len(nums)):
            heapq.heappush(min_nums,(nums[i][0],(i,0)))
            max_number = max(max_number,nums[i][0])
        
        min_range = [min_nums[0][0], max_number]

        while True:
            _,(k, index) = heapq.heappop(min_nums)

            if index + 1 >= len(nums[k]):
                break

            new_num = nums[k][index + 1]
            max_number = max(max_number,new_num)
            heapq.heappush(min_nums,(new_num,(k, index + 1)))
            
            
            ba = max_number - min_nums[0][0]
            dc = min_range[1] - min_range[0]
            if ba < dc or (min_nums[0][0] < min_range[0] and ba == dc): 
                min_range = [min_nums[0][0],max_number]

        return min_range