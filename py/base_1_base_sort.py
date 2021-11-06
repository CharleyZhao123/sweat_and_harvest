from typing import List
from random import randint

# 默认从小到大排序


class Solution:
    # 基础冒泡
    def bubbleSort(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        for i in range(0, arr_len-1):
            for j in range(0, arr_len-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # 优化冒泡
    def bubbleSortPlus(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        for i in range(0, arr_len-1):
            # 当某次循环没有进行交换，可以判定整个数列已经有序，则退出结束
            flag = True
            for j in range(0, arr_len-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = False
            if flag == True:
                break
        return arr
    
    # 选择排序
    def selectSort(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        for i in range(0, (arr_len-1)):
            max_index = 0
            for j in range(1, (arr_len-i)):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[arr_len-1-i], arr[max_index] = arr[max_index], arr[arr_len-1-i]
        return arr
    
    # 插入排序
    def insertSort(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        i = 1
        while i < arr_len:
            j = i
            # 交换次数多
            while arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                if j > 1:
                    j -= 1
                else:
                    break
            i += 1
        return arr
    
    # 插入排序改良
    def insertSortPlus(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        i = 1
        while i < arr_len:
            j = i
            i_num = arr[i]
            while arr[j-1] > i_num and j >= 1:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = i_num
            i += 1
        return arr
    
    # 希尔排序
    # 增量1，2，4，8，16....不一定比O(N^2)快，比如2，1，5，3，7，6，9，8
    # 其他的快速增量：
    # Hibbard增量：2^k-1:1,3,7,15，最坏O(N^(3/2))
    # Segdgewick增量：9*4^k - 9*2^k + 1 或者 4^k - 3*2^k + 1，最坏时间复杂度是O(n^(4/3))
    def shellSort(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        gap = arr_len // 2
        while gap > 0:
            arr = self.insertSortShell(arr, gap)
            gap = gap // 2
        return arr
    
    def insertSortShell(self, arr: List[int], gap: int) -> List[int]:
        arr_len = len(arr)
        i = 0
        while i < gap:
            j = i + gap
            while j < arr_len:
                j_now = arr[j]
                k = j
                while j_now < arr[k - gap] and k >= i + gap:
                    arr[k] = arr[k-gap]
                    k -= gap
                arr[k] = j_now

                j += gap
            i += 1

        return arr

# https://zhuanlan.zhihu.com/p/40695917





    @staticmethod
    def generateRandArray(min, max, n):
        array = []
        array = [randint(min, max) for x in range(n)]
        return array

    @staticmethod
    def generateNearlyOrderedArray(n, swapTimes):
        arr = []
        for i in range(n):
            arr.append(i)
        for j in range(swapTimes):
            pos_i = randint(0, n-1)
            pos_j = randint(0, n-1)
            arr[pos_i], arr[pos_j] = arr[pos_j], arr[pos_i]

        return arr


if __name__ == '__main__':
    s = Solution()
    # arr = s.generateNearlyOrderedArray(10, 1)
    arr = s.generateRandArray(2, 100, 10)
    print(arr)
    # print(s.bubbleSort(arr))
    print(s.shellSort(arr))
