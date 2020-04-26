# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午10:51

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        zero_cnt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
            else:  # nums[i] != 0
                nums[i - zero_cnt] = nums[i]

        # 末尾填充零
        for i in range(len(nums) - zero_cnt, len(nums)):
            nums[i] = 0
