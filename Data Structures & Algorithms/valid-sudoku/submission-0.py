class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box_num(r, c):
            return 3*(r//3) + c//3 + 1
        
        valid = True
        hash = {i:[set() for j in range(3)] for i in range(1,10)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    if i in hash[n][0]:
                        # print(f'row issue, number: {n}, {hash[n]} already present in board')
                        # print(f'row:{i}, col:{j}')
                        valid = False
                        break
                    if j in hash[n][1]:
                        # print(f'col issue, number: {n}, {hash[n]} already present in board')
                        # print(f'row:{i}, col:{j}')
                        valid = False
                        break
                    hash[n][0].add(i)
                    hash[n][1].add(j)
                    t = box_num(i, j)
                    if t in hash[n][2]:
                        # print(f'box issue, number: {n}, {hash[n]} already present in board')
                        # print(f'row:{i}, col:{j}')
                        valid = False
                        break
                    hash[n][2].add(t)

            if not valid:
                break
        return valid