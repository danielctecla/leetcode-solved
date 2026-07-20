class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((timestamp,value))
        else:
            self.hashMap[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        left = 0
        right = len(self.hashMap[key]) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2
            midTimestamp, midValue = self.hashMap[key][mid]

            if midTimestamp == timestamp:
                return midValue
            elif midTimestamp < timestamp:
                left = mid + 1
                ans = midValue
            else:
                right = mid - 1
                
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)