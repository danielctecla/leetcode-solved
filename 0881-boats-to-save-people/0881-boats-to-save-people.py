class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1

        total_boats = 0

        while left <= right:
            if left != right:

                weight = people[left] + people[right]

                if weight <= limit:
                    left += 1

            total_boats += 1
            right -= 1
        
        return total_boats