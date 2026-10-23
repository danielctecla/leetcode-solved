class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        def searchWord(row: int, col: int, index: int) -> bool:
            visited.add((row,col))

            if index == len(word) - 1 and board[row][col] == word[index]:
                return True
            
            # dr - direction row
            for dr, dc in directions:
                # nr - next row
                nr, nc = row + dr, col + dc

                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] != word[index + 1] or (nr,nc) in visited:
                        continue
                    
                    find = searchWord(nr,nc, index+1)                

                    if find:
                        return True
                    
                    visited.remove((nr,nc))

            return False

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if board[row][col] != word[0]:
                    continue
                
                visited = set()
                found = searchWord(row,col,0)

                if found:
                    return True
        
        return False