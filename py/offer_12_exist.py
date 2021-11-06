from typing import List
import copy


class Solution:
    # out of time
    def exist1(self, board: List[List[str]], word: str) -> bool:
        row_n = len(board)
        col_n = len(board[0])
        board_used = [([0] * (col_n+2)) for _ in range(row_n+2)]

        for i in range(row_n + 2):
            for j in range(col_n + 2):
                if i == 0 or j == 0 or i == (row_n+1) or j == (col_n+1):
                    board_used[i][j] = 1
        board_used_copy = copy.deepcopy(board_used)
        for bi in range(row_n):
            for bj in range(col_n):

                board_used = copy.deepcopy(board_used_copy)
                if board[bi][bj] == word[0]:
                    board_used[bi+1][bj+1] = 1
                    if self.build_word1(board, word, board_used, bi, bj, 0):
                        return True

        return False

    def build_word1(self, board, word, board_used, bi, bj, word_i):
        word_i += 1
        if word_i < len(word):
            # 0: up
            # 1: down
            # 2: right
            # 3: left
            board_used_copy = copy.deepcopy(board_used)
            flag = False
            for i in range(4):
                board_used = copy.deepcopy(board_used_copy)
                if i == 0 and board_used[bi+1-1][bj+1] != 1:
                    if board[bi-1][bj] == word[word_i]:
                        board_used[bi][bj+1] = 1
                        flag = self.build_word1(
                            board, word, board_used, (bi-1), bj, word_i)
                    if flag == True:
                        break
                elif i == 1 and board_used[bi+1+1][bj+1] != 1:
                    if board[bi+1][bj] == word[word_i]:
                        board_used[bi+1+1][bj+1] = 1
                        flag = self.build_word1(
                            board, word, board_used, (bi+1), bj, word_i)
                    if flag == True:
                        break
                elif i == 2 and board_used[bi+1][bj+1+1] != 1:
                    if board[bi][bj+1] == word[word_i]:
                        board_used[bi+1][bj+1+1] = 1
                        flag = self.build_word1(
                            board, word, board_used, bi, (bj+1), word_i)
                    if flag == True:
                        break
                elif i == 3 and board_used[bi+1][bj+1-1] != 1:
                    if board[bi][bj-1] == word[word_i]:
                        board_used[bi+1][bj+1-1] = 1
                        flag = self.build_word1(
                            board, word, board_used, bi, (bj-1), word_i)
                    if flag == True:
                        break
                elif i == 3:
                    return False
        else:
            flag = True

        return flag
    
    # 答案
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 内嵌函数就不用传参了
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            # 用''来表示遍历过，就不用另外开辟空间了
            board[i][j] = ''
            # 从下、上、右、左依次进行搜索
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 还原，因为如果res == False，后续还要使用该元素
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False



if __name__ == '__main__':
    s = Solution()
    # print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
    #       ['A', 'D', 'E', 'E']], 'ABCCED'))
    # print(s.exist([["F", "Y", "C", "E", "N", "R", "D"], ["K", "L", "N", "F", "I", "N", "U"], ["A", "A", "A", "R", "A", "H", "R"], [
    #       "N", "D", "K", "L", "P", "N", "E"], ["A", "L", "A", "N", "S", "A", "P"], ["O", "O", "G", "O", "T", "P", "N"], ["H", "P", "O", "L", "A", "N", "O"]], "INDIA"))
    print(s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
    