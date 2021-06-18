from typing import List
from collections import Counter
'''
    Python：使用Counter进行计数统计及collections模块
    https://www.huaweicloud.com/articles/fc3ed46ed01daa562c768e40e91e3941.html
'''


class Solution:
    def numRabbits1(self, answers: List[int]) -> int:
        ans_dict = {}
        for a in answers:
            if a in ans_dict:
                ans_dict[a] += 1
            else:
                ans_dict[a] = 1
        rabbits_num = 0
        for k, v in ans_dict.items():
            k_group = v//(k+1)
            k_remainder = 0 if v % (k+1) == 0 else 1
            rabbits_num = rabbits_num + (k_group + k_remainder)*(k+1)
        return rabbits_num

    def numRabbits2(self, answers: List[int]) -> int:
        answers_set = set(answers)
        answers_dict = {}
        for a in answers_set:
            answers_dict[a] = answers.count(a)
        rabbits_num = 0
        for k, v in answers_dict.items():
            k_group = v//(k+1)
            k_remainder = 0 if v % (k+1) == 0 else 1
            rabbits_num = rabbits_num + (k_group + k_remainder)*(k+1)
        return rabbits_num

    def numRabbits(self, answers: List[int]) -> int:
        # rabbits_num = 0
        # for k, v in Counter(answers).items():
        #     rabbits_num += (v//(k+1) + (0 if v%(k+1) == 0 else 1)) * (k + 1)
        rabbits_num = sum((v//(k+1) + (0 if v % (k+1) == 0 else 1)) * (k + 1)
                          for k, v in Counter(answers).items())
        return rabbits_num


if __name__ == '__main__':
    s = Solution()
    print(s.numRabbits(answers=[2, 2, 1, 0, 0]))
