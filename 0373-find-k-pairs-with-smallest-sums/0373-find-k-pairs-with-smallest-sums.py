class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        # order matters
        # we are going to check all the solutions
        # max hip = []
        # iterate in all nums1:
        #   iterate in all nums2:
        #       check ui with v1 ... vm-1
        #       if len(heap) <  k:
        #           add directly to heap
        #       if is minimum 
        #           replace heap
        #       else
        #           break


        # time complexity O(n*m) where n is the size of nums1 and m is the size of nums2

        # Initially, for each nums1[i], create the pair:
        # nums1[i] + nums2[0]
        #
        # Put those candidates in a min-heap.
        #
        # Pop the minimum candidate and append its pair to the result.
        #
        # If that candidate came from nums1[i] and nums2[j],
        # push the next candidate from the same row:
        # nums1[i] + nums2[j + 1]
        #
        # Repeat until we have k pairs.

        array = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            array.append((nums1[i]+nums2[0],(i,0)))

        heapq.heapify(array)

        result = []

        for _ in range(k):
            total, (i, j) = heapq.heappop(array)
            result.append([nums1[i],nums2[j]])
            j += 1
            if j < m:
                heapq.heappush(array,(nums1[i] + nums2[j],(i,j)))
        
        return result
