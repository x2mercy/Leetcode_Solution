class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        test=['1','2','3','4','5','6','7','8','9']
        for i in range(len(board)):#line
            for j in test:
                if board[i].count(j)>1:
                    return False

        for i in range(0,10):#row
            row={}
            for j in range(len(board)):
                try:
                    int(board[j][i])
                except:
                    continue
                if board[j][i] not in row.keys():
                    row[board[j][i]]=1
                else:
                    return False
        box = [[{} for _ in xrange(3)] for __ in xrange(3)]
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == '.': continue
                if char in box[i/3][j/3]: return False
                else: box[i/3][j/3][char] = [i,j]
        return True
