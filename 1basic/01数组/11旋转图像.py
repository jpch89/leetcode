# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-3 下午12:51

"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)

        # 记录第几圈
        cnt = 0

        # 最外圈循环
        while size > 1:
            i = j = cnt

            # 每圈移动 size - 1 轮
            for m in range(size - 1):
                # 暂存
                top = matrix[i][j + m]
                right = matrix[j + m][i + size - 1]
                bottom = matrix[j + size - 1][i + size - 1 - m]
                left = matrix[j + size - 1 - m][i]

                # 赋值
                matrix[i][j + m] = left
                matrix[j + m][i + size - 1] = top
                matrix[j + size - 1][i + size - 1 - m] = right
                matrix[j + size - 1 - m][i] = bottom

            size -= 2
            cnt += 1
