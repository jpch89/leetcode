# LCP 01. 猜数字

---

## 题目描述

小 `A` 和 小 `B` 在玩猜数字。小 `B` 每次从 1, 2, 3 中随机选择一个，小 `A` 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小 `A` 猜对了几次？


输入的 `guess` 数组为小 `A` 每次的猜测，`answer` 数组为小 `B` 每次的选择。`guess` 和 `answer` 的长度都等于 `3`。

**示例 1：**

> 输入：guess = [1,2,3], answer = [1,2,3]
> 输出：3
> 解释：小A 每次都猜对了。

**示例 2：**

> 输入：guess = [2,2,3], answer = [3,2,1]
> 输出：1
> 解释：小A 只猜对了第二次。

限制：

1. `guess` 的长度 = 3
2. `answer` 的长度 = 3
3. `guess` 的元素取值为 `{1, 2, 3}` 之一。
4. `answer` 的元素取值为 `{1, 2, 3}` 之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---

## 一行解

```python3
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return len([i for i in range(len(guess)) if guess[i] == answer[i]])
```

---

## 极简一行解

参考了 (louis-gui 的评论)[https://leetcode-cn.com/problems/guess-numbers/comments/164988]。

学到了在 `Python` 中：`True + True` 等于 `2`。

另外不带括号不行，会有运算符优先级问题。

```python3
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return (guess[0] == answer[0]) + (guess[1] == answer[1]) + (guess[2] == answer[2])
```

---

`2020.5.3`
