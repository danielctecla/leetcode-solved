class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        drop_off = []
        trips.sort(key=lambda trip:trip[1])

        for trip in trips:
            passengers, pick_km, drop_km = trip
            
            while drop_off and drop_off[0][0] <= pick_km:
                km, drop_people = heapq.heappop(drop_off)
                capacity += drop_people
            
            capacity -= passengers

            if capacity < 0:
                return False
            
            heapq.heappush(drop_off,(drop_km,passengers))

        return True
