class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((timestamp,value))
        else:
            self.hashMap[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        arr_time = self.hashMap.get(key,[])
        
        left = 0
        right = len(arr_time) - 1
        
        mid = -1
        ans = ""

        while left <= right:
            mid = (left + right) // 2
            if arr_time[mid][0] == timestamp:
                return arr_time[mid][1]
            elif timestamp < arr_time[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
                ans = arr_time[mid][1]
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)