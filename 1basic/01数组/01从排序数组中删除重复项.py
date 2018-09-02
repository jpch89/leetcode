# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-2 下午11:56

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i + 1 < length:
            if nums[i] == nums[i + 1]:
                del (nums[i])
                length -= 1
                i -= 1
            i += 1
        return length


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3]
    length = Solution().removeDuplicates(nums)
    print(nums)
