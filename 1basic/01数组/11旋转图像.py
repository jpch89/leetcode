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

        # 左上角锚点初始坐标
        i0 = j0 = cnt = 0

        # 最外圈循环
        while size > 1:
            i0 = j0 = cnt

            # 每圈移动 size - 1 轮
            for m in range(size - 1):
                # 每轮重新计算锚点坐标
                i0, j0 = i0, j0 + m
                i, j = i0, j0
                # 移动 4 次
                for n in range(4):

                    # 计算目标点 i, j
                    if i == i0:
                        j += (size - 1)
                        if j > size - 1:
                            i = i0 + j - (size - 1)
                            j = j0 + size - 1
                        tmp = matrix[i][j]
                        matrix[i][j] = matrix[i0][j0]
                        continue
                    if j == j0 + size - 1:




                # 暂存

                # 移动

            size -= 2
            cnt += 1