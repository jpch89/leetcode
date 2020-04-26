# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午11:03

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

        for i in range(len(nums)):
            other = target - nums[i]
            if other in nums:
                if nums[i] == other:
                    try:
                        j = nums.index(other, i + 1)
                    except:
                        continue
                else:
                    j = nums.index(other)
                return [i, j]
