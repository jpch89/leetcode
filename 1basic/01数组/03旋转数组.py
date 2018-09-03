# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午8:47

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
说明：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        k = k % length
        new_nums = nums[-k:] + nums[:length - k]
        for i in range(length):
            nums[i] = new_nums[i]
