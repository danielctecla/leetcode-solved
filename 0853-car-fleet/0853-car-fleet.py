class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, reverse = True)
        
        print(pairs)
        answer = 0
        lastTime = 0
        for position, speed in pairs:
            currentTime = (target - position) / speed
            if currentTime > lastTime:
                answer += 1
                lastTime = currentTime

        return answer