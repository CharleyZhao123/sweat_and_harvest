from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        index = (nums1_len + nums2_len) // 2
        if (nums1_len + nums2_len) % 2 == 0:
            # 偶数
            flag = 1
        else:
            # 奇数
            flag = 0
        i = i_1 = i_2 = 0
        end = end_1 = end_2 = 0
        while i < index - flag + 2:
            if i_1 < nums1_len:
                y_1 = nums1[i_1]
            else:
                y_1 = 10e6 + 1
            if i_2 < nums2_len:
                y_2 = nums2[i_2]
            else:
                y_2 = 10e6 + 1
            if y_1 < y_2:
                end = y_1
                i_1 += 1
            else:
                end = y_2
                i_2 += 1
            if(i == index - flag):
                end_1 = end
            elif(i == index - flag + 1):
                end_2 = end
            i += 1
        if flag == 1:
            return ((end_1+end_2)/2)
        else:
            return end_1


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 3, 5], [2, 4]))
