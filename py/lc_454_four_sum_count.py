from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    # defaultdict
    def fourSumCount1(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        num_len = len(nums1)
        a = defaultdict(int)
        b = defaultdict(int)
        for i in range(num_len):
            for j in range(num_len):
                a[nums1[i]+nums2[j]] += 1
                b[nums3[i]+nums4[j]] += 1
        count = 0
        for k, v in a.items():
            b_v = b[-k]
            if b_v != 0:
                # print(v, b_v)
                count += (v * b_v)
        return count

    # counter
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count12 = Counter(n1 + n2 for n1 in nums1 for n2 in nums2)
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                if -n3 - n4 in count12:
                    count += count12[-n3-n4]

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
