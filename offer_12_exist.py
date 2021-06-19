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
                    if self.build_word(board, word, board_used, bi, bj, 0):
                        return True

        return False

    def build_word(self, board, word, board_used, bi, bj, word_i):
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
                        flag = self.build_word(
                            board, word, board_used, (bi-1), bj, word_i)
                    if flag == True:
                        break
                elif i == 1 and board_used[bi+1+1][bj+1] != 1:
                    if board[bi+1][bj] == word[word_i]:
                        board_used[bi+1+1][bj+1] = 1
                        flag = self.build_word(
                            board, word, board_used, (bi+1), bj, word_i)
                    if flag == True:
                        break
                elif i == 2 and board_used[bi+1][bj+1+1] != 1:
                    if board[bi][bj+1] == word[word_i]:
                        board_used[bi+1][bj+1+1] = 1
                        flag = self.build_word(
                            board, word, board_used, bi, (bj+1), word_i)
                    if flag == True:
                        break
                elif i == 3 and board_used[bi+1][bj+1-1] != 1:
                    if board[bi][bj-1] == word[word_i]:
                        board_used[bi+1][bj+1-1] = 1
                        flag = self.build_word(
                            board, word, board_used, bi, (bj-1), word_i)
                    if flag == True:
                        break
                elif i == 3:
                    return False
        else:
            flag = True

        return flag


if __name__ == '__main__':
    s = Solution()
    # print(s.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
    #       ['A', 'D', 'E', 'E']], 'ABCCED'))
    # print(s.exist([["F", "Y", "C", "E", "N", "R", "D"], ["K", "L", "N", "F", "I", "N", "U"], ["A", "A", "A", "R", "A", "H", "R"], [
    #       "N", "D", "K", "L", "P", "N", "E"], ["A", "L", "A", "N", "S", "A", "P"], ["O", "O", "G", "O", "T", "P", "N"], ["H", "P", "O", "L", "A", "N", "O"]], "INDIA"))
    print(s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
