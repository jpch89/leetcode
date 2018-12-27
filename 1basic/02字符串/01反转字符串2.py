# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-4 上午7:31

"""
编写一个函数，其作用是将输入的字符串反转过来。
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        lists = list(s)
        for i in range(len(s) // 2):
            lists[i], lists[-i - 1] = lists[-i - 1], lists[i]
        return ''.join(lists)
