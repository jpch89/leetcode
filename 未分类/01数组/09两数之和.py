# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午11:01

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for num in nums:
            if target - num in nums:
                i = nums.index(num)
                try:
                    j = nums.index(target - num, i + 1)
                except:
                    continue
                return [i, j]
