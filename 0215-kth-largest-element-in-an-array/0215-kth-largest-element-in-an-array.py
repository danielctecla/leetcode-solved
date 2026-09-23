class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # nums maximum length? 10^4
        # exist negative numbers? Yes
        # can I receive an empty array? No
        # array[numbers] -> kth largest element
        # array [1,2,100] -> k = 1 -> output: 100

        # sorting the array nlog(n) time complexity
        # first step is sort the array. Decrease mode
        # return (index - 1)
        
        # heap
        # k bigger elements
        # time complexity - O(nlog(k))
        # memory complexity - O(k)
        
        # create heap max
        # for element in nums
        #   add to the heap
        # navigate to get the minum element

        k_largest = []
        heapq.heapify(k_largest)

        for element in nums:
            if len(k_largest) < k:
                heapq.heappush(k_largest,element)
            elif element > k_largest[0]:
                if len(k_largest) == k:
                    heapq.heapreplace(k_largest, element)
                else:
                    heapq.heappush(k_largest,element)

        return k_largest[0]

        # [2,1]

        #[2,]
        #