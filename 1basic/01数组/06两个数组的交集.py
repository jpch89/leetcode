# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 上午10:03

"""
给定两个数组，编写一个函数来计算它们的交集。

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 < len2:
            for i in nums1:
                if i in nums2:
                    intersect.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    intersect.append(i)
                    nums1.remove(i)
        return intersect
