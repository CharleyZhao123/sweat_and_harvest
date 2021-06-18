from typing import List


class Solution:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        if len(nums1) > len(nums2):
            for i in nums1:
                if (i in nums2) and (not i in inter):
                    inter.append(i)
        else:
            for i in nums2:
                if (i in nums1) and (not i in inter):
                    inter.append(i)
        return inter

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        inter = []
        index1 = index2 = 0
        while index1 < nums1_len and index2 < nums2_len:
            n1 = nums1[index1]
            n2 = nums2[index2]
            if n1 < n2:
                index1 += 1
                continue
            elif n1 > n2:
                index2 += 1
            else:
                if not inter or n1 != inter[-1]:
                    inter.append(n1)
                index1 += 1
                index2 += 1
        return inter


if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
