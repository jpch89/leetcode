"""
有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
说明:
你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        set_s = set(s)
        set_t = set(t)

        if set_s != set_t:
            return False

        for i in set_s:
            if s.count(i) != t.count(i):
                return False
        return True

res = Solution().isAnagram('anagram', 'nagaram')
print(res)
