class Solution:
    def isValidSudoku(self,board):

        #initialize data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        #validate a board
        for a in range(9):
            for b in range(9):
                num = board[a][b]
                if num != '.':
                    num = int(num)
                    box_index = (a//3)*3 + b//3

                    #populate dictionaries inside cells of rows, columns and boxes
                    rows[a][num] = rows[a].get(num,0) + 1
                    columns[b][num] = columns[b].get(num,0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num,0) + 1

                    #check if duplicates exist
                    if rows[a][num] > 1 or columns[b][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True
        
O(1) time
O(1) space
