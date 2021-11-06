from typing import List
class Solution:
    # 空间O(N),时间O(N)
    def findRepeatNumber(self, nums: List[int]) -> int:
        temp_set = set()
        # repeat = -1
        for index, num in enumerate(nums):
            temp_set.add(num)
            if len(temp_set) < index + 1:
                return num
    # 空间O(1),时间O(N^2):用插入排序或选择排序进行排序，之后判断连续的两个元素是否相等
    # 不可以使用Python内置排序，因为python内置的list.sort()/sorted()是空间复杂度O(N),时间复杂度O(NlogN)的timesort
    def findRepeatNumber2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
            

if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatNumber2([1,2,3,2,4]))