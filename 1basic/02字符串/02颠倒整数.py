# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-4 上午7:29

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
根据这个假设，如果反转后的整数溢出，则返回 0。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            numli = list(str(x))
            neg = True
        else:
            numli = list(str(x))

        resli = []

        if neg:
            numli.append('-')
            for i in range(len(numli) - 1, 0, -1):
                resli.append(numli[i])
        else:
            for i in range(len(numli) - 1, -1, -1):
                resli.append(numli[i])

        res = int(''.join(resli))
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0
