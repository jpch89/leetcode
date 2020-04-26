"""
字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}.fromkeys(s, 0)
        for i in s:
            d[i] += 1
        unique = [k for k, v in d.items() if v == 1]
        for index, char in enumerate(s):
            if char in unique:
                return index
        return -1


res = Solution().firstUniqChar('leetcode')
print(res)

# 如果字典是有序的话（Python 3.7 以上），更简单
# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         d = {}.fromkeys(s, 0)
#         for i in s:
#             d[i] += 1
#         unique = [k for k, v in d.items() if v == 1]
#         for index, char in enumerate(s):
#             if char in unique:
#                 return index
#         return -1
