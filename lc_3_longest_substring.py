# from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_l = 0
        l_begin = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict:
                # 收缩窗口
                # 判断重复字符的位置是否已经在起始位置之前了
                if char_dict[s[i]] >= l_begin:
                    l = i - l_begin
                    if l > longest_l:
                        longest_l = l
                    # 更新新窗口起始位置
                    l_begin = char_dict[s[i]] + 1
                    # 更新Hash Set值
                    char_dict[s[i]] = i
                    continue
            l = i - l_begin + 1
            if l > longest_l:
                longest_l = l
            char_dict[s[i]] = i
        return longest_l

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcbadbcbb'))