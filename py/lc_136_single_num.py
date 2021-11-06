from typing import List
from collections import defaultdict
class Solution:
    # hash
    def singleNumber1(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for i in nums:
            nums_dict[i] += 1
            if nums_dict[i] == 2:
                del nums_dict[i]
        key, _ = nums_dict.popitem()
        return key
    # bit
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in nums:
            single = single ^ i
        return single 


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber(nums=[2, 2, 1, 3, 1]))
