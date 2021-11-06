from typing import List
class Solution:
    def minArray1(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return arr[i]
        return arr[0]
    
    def minArray(self, arr: List[int]) -> int:
        low, high = 0, (len(arr) - 1)
        pivot = low + (high - low)//2
        while low < high:
            if arr[pivot] < arr[high]:
                high = pivot
            elif arr[pivot] > arr[high]:
                low = pivot + 1
            else:
                high -= 1
            pivot = low + (high - low)//2
        
        return arr[low]



if __name__ == '__main__':
    s = Solution()
    print(s.minArray([4, 5, 6, 1, 2, 3]))