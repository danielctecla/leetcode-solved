class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        def searchWord(row: int, col: int, index: int) -> bool:
            if index == len(word) - 1:
                return True

            temp = board[row][col]
            board[row][col] = "#"

            found = False
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[index + 1]:
                    if searchWord(nr, nc, index + 1):
                        found = True
                        break

            board[row][col] = temp
            return found

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                
                if board[row][col] != word[0]:
                    continue
                
                if searchWord(row,col,0):
                    return True
        
        return False