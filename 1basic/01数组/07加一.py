# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午10:23

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] += 1
        carry = True if digits[-1] == 10 else False
        if carry:
            digits[-1] = 0

        for i in range(len(digits) - 2, -1, -1):
            if carry:
                digits[i] += 1
                carry = False
                if digits[i] > 9:
                    digits[i] = 0
                    carry = True

        if carry:
            result = [1]
            result.extend(digits)
            return result
        else:
            return digits
