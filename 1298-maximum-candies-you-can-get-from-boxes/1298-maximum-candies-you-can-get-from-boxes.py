from collections import deque

class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        # base case if the len of the given boxes is zero 
        #   return 0
        # 

        #todo: base case

        boxes = deque(initialBoxes)
        found_keys = set()
        opened_boxes = True
        total_candies = 0

        while boxes and opened_boxes:
            opened_boxes = False

            for _ in range(len(boxes)):
                i_box = boxes.popleft()

                # checking if the box is open or if i have the key
                if status[i_box] == 1 or i_box in found_keys:
                    total_candies += candies[i_box]

                    # add the boxes to the queue
                    for box in containedBoxes[i_box]:
                        boxes.append(box)
                    
                    # add the keys to the set
                    for key in keys[i_box]:
                        found_keys.add(key)
                    
                    opened_boxes = True
                    
                else:
                    boxes.append(i_box)

        return total_candies