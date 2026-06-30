class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        lastTime = 0
        for pos, spd in pairs:
            currentTime = (target - pos) / spd
            if currentTime > lastTime:
                fleets += 1
                lastTime = currentTime

        return fleets