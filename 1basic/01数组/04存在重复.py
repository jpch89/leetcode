# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午8:56

"""
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) != len(nums):
            return True
        return False
