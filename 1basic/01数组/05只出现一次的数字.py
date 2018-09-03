# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午8:59

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            single = nums[0]
            try:
                nums.remove(single)
                nums.remove(single)
            except:
                return single
        single=nums[0]
        return single
