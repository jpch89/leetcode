# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-4 上午7:25

"""
编写一个函数，其作用是将输入的字符串反转过来。
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = []
        for i in range(len(s) - 1, -1 , -1):
            str_list.append(s[i])
        return ''.join(str_list)
