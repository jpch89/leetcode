"""
验证回文字符串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""


# 网站上的版本必须要改成
# filter(str.isalnum, str(s))
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        s = list(filter(str.isalnum, str(s))
        rs = s[::-1]
        if s == rs:
            return True
        return False


res = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(res)

# Python 3.6.6 测试通过
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """

#         s = s.lower()
#         s = list(filter(str.isalnum, s))
#         rs = s[::-1]
#         if s == rs:
#             return True
#         return False
