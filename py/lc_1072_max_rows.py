from collections import defaultdict
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_num = len(matrix)
        row_mode_dict = defaultdict(int)

        for i in range(row_num):
            if matrix[i][0] == 0:
                row_i_list = [str(x) for x in matrix[i]]
                row_i_str = "".join(row_i_list) 
            else:
                row_i_list = [str(1-x) for x in matrix[i]]
                row_i_str = "".join(row_i_list) 
            row_mode_dict[row_i_str] = row_mode_dict[row_i_str] + 1

        return max(row_mode_dict.values())




if __name__ == '__main__':
    s = Solution()
    print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))