class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r / 3, c / 3)

        #a nested loop to iterate through the whole 9x9 grid
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': 
                    continue
                if (board[r][c] in cols[c] or #checks for the set at the specific column
                    board[r][c] in rows[r] or #checks for the set at the specific row
                    board[r][c] in squares[(r // 3, c // 3)]): #checks for the set at that sub-box
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
