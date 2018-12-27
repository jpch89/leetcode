"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        res = 0
        sign = 1
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        stripped = str.lstrip()

        # 判断是否为空字符串
        if stripped == '':
            return 0

        # 判断第一个字符是否不属于正负号或者数字
        if stripped[0] not in ('+', '-') and not stripped[0].isdigit():
            return 0

        # 更改整数符号
        if stripped[0] == '+':
            stripped = stripped[1:]
        elif stripped[0] == '-':
            sign = -1
            stripped = stripped[1:]

        # 拿去符号是否为空字符串
        if stripped == '':
            return 0

        for i, d in enumerate(stripped):
            if not d.isdigit():
                break
        else:  # 全部都是数字
            res = sign * int(stripped)
            if INT_MIN <= res <= INT_MAX:
                return res
            elif res < INT_MIN:
                return INT_MIN
            elif res > INT_MAX:
                return INT_MAX

        # 截取数字部分
        stripped = stripped[:i]
        # 截取后为空字符串，对应 '+-2' 此类情况
        if stripped == '':
            return 0

        # 转换为整数
        res = sign * int(stripped)
        if INT_MIN <= res <= INT_MAX:
            return res
        elif res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX


s = Solution()
print(s.myAtoi('+-2'))
