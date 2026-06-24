class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        
        sortedMap = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        answer = []
        for i in range(k):
            answer.append(sortedMap[i][0])

        return answer