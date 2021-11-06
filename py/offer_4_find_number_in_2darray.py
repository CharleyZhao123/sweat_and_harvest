from typing import List


class Solution:
    # 方法一：从上到下逐行查找，每行是二分查找
    def findNumberIn2DArray1(self, metrix: List[List[int]], target: int) -> bool:
        row_num = len(metrix)
        if row_num > 0:
            col_num = len(metrix[0])
            if col_num == 0:
                return False
        else:
            return False
        flag = False
        row_i = 0
        while row_i < row_num and metrix[row_i][0] <= target:
            list_i = metrix[row_i]
            if list_i[col_num-1] >= target:
                if self.findNumberInArray(list_i, target, col_num):
                    flag = True
                    break
            row_i += 1

        return flag
    
    def findNumberInArray(self, list_i: List[int], target: int, col_num: int) -> bool:
        i = 0
        j = col_num - 1
        if list_i[i] == target or list_i[j] == target:
            return True
        while j-i > 1:
            mid = (i+j)//2
            if list_i[mid] < target:
                i = mid
            elif list_i[mid] > target:
                j = mid
            else:
                return True
        return False
    # 方法一：end

    # 方法二：由于给定的二维数组具备每行从左到右递增以及每列从上到下递增的特点，当访问到一个元素时，可以排除数组中的部分元素。
    # 从二维数组的右上角开始查找。如果当前元素等于目标值，则返回 true。如果当前元素大于目标值，则移到左边一列。如果当前元素小于目标值，则移到下边一行。
    # (同理也可从左下角开始)
    def findNumberIn2DArray(self, metrix: List[List[int]], target: int) -> bool:
        row_num = len(metrix)
        if row_num > 0:
            col_num = len(metrix[0])
        else:
            return False
        i = 0
        j = col_num - 1
        while i < row_num and j >= 0:
            if metrix[i][j] < target:
                i += 1
            elif metrix[i][j] > target:
                j -= 1
            else:
                return True
        
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20
                                ))
