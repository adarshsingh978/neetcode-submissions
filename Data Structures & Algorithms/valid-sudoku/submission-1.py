class Solution:
    def isValidCol(self, board: List[List[str]]) -> bool:
        n = len(board)
        hashSet = set()
        for i in range(n):
            hashSet = set()
            for j in range(n):
                if board[j][i] != '.':
                    if (board[j][i]) not in hashSet:
                        hashSet.add(board[j][i])
                    else:
                        return False
        return True


    def isValidRow(self, board: List[List[str]]) -> bool:
        n = len(board)
        hashSet = set()
        count = 0
        for i in range(n):
            hashSet = set()
            for j in range(n):
                if board[i][j] != '.':
                    if (board[i][j]) not in hashSet:
                        hashSet.add(board[i][j])
                    else:
                        return False
        return True


    def isValidBox(self, arr: List[List[str]]) -> bool:
        n = len(arr)
        count = 0
        d = {} 

        for i in range(n):
            # print("---")
            for j in range(n):
                if (arr[i][j] != "."):
                    key = (i//3,j//3)
                    # print(f'{i=} , {j=}, {key=}')
                    if key not in d:
                        value = set()
                        value.add(arr[i][j])
                        d[key] =  value
                        # print(f"d in 1 {d=}")
                    elif (arr[i][j] not in d[key]):
                        d[key].add(arr[i][j])
                        # print(f"d in 2 {d=}")
                    else:

                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(self.isValidCol(board))
        print(self.isValidRow(board))
        # print("boxxxx")
        print(self.isValidBox(board))
        return self.isValidCol(board) and self.isValidRow(board) and self.isValidBox(board)
        