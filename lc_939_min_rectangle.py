from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = 16e8
        change_flag = 0
        points_num = len(points)
        i = 0
        while i < points_num - 1:
            point_i = points[i]
            j = i + 1
            while j < points_num:
                point_j = points[j]
                if (point_i[0] != point_j[0]) and (point_i[1] != point_j[1]):
                    area = abs((point_i[0]-point_j[0])*(point_i[1]-point_j[1]))
                    if area < min_area:
                        if ([point_i[0], point_j[1]] in points) and ([point_j[0], point_i[1]] in points):
                            min_area = area
                            change_flag = 1
                j = j + 1
            i = i + 1
        if change_flag == 1:
            # print(min_area)
            return min_area
        else:
            # print(0)
            return 0



if __name__ == '__main__':
    point = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    s = Solution()
    s.minAreaRect(points=point)
