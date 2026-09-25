from collections import deque

class Solution:
  def canMeasureWater(self, x: int, y: int, target: int) -> bool:

    queue = deque()
    queue.append((0,0))
    visited_state = set()

    while queue:
        x_jug,y_jug = queue.popleft()
        
        if (x_jug,y_jug) in visited_state:
            continue
        visited_state.add((x_jug,y_jug))

        if x_jug + y_jug == target:
            return True
        
        #fill left and right
        if x_jug != x:
            queue.append((x,y_jug))
        if y_jug != y:
            queue.append((x_jug,y))

        #empty left and right
        if x_jug != 0:
            queue.append((0,y_jug))
        if y_jug != 0:
            queue.append((x_jug,0))
        
        #transfer water
        queue.append((
            min(x_jug+y_jug, x),
            max(y_jug-(x - x_jug), 0)
        ))
        queue.append((
            max(0,x_jug - (y - y_jug)), 
            min(y_jug+x_jug, y)
        ))
        
    return False