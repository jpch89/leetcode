# 剑指 Offer 11. 旋转数组的最小数字

## 题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 `[3,4,5,1,2]` 为 `[1,2,3,4,5]` 的一个旋转，该数组的最小值为 `1`。

**示例 1：**

> 输入：[3,4,5,1,2]
> 输出：1

**示例 2：**

> 输入：[2,2,2,0,1]
> 输出：0

注意：本题与主站 154 题相同：<https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/>

> 来源：力扣（LeetCode）  
> 链接：<https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof>  
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---

## 暴力一行解

没有利用局部有序的特性，所以时间复杂度为 `O(n)`。

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return min(numbers)
```

---

`2020.7.22`
