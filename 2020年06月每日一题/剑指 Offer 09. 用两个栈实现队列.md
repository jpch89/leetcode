# 剑指 Offer 09. 用两个栈实现队列

## 题目描述

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 `appendTail` 和 `deleteHead`，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，`deleteHead` 操作返回 `-1`)

**示例 1：**

```txt
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```

**示例 2：**

```txt
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```

**提示：**

- `1 <= values <= 10000`
- `最多会对 appendTail、deleteHead 进行 10000 次调用`

来源：力扣（LeetCode）
链接：<https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof>
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

---

## 每次入队出队都倒腾

自己的写法，每次入队出队都要倒腾，时间复杂度是 `O(n)`。

```python
class CQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def appendTail(self, value: int) -> None:
        while self.st2:
            self.st1.append(self.st2.pop())
        self.st1.append(value)

    def deleteHead(self) -> int:
        while self.st1:
            self.st2.append(self.st1.pop())
        return self.st2.pop() if self.st2 else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

**运行结果：**

> 执行结果：通过  
> 执行用时：1404 ms, 在所有 Python3 提交中击败了18.56% 的用户  
> 内存消耗：17.2 MB, 在所有 Python3 提交中击败了100.00% 的用户

---

## 只在出队的必要时刻倒腾

使用两个栈，一个只管进，一个只管出。
这是参考题解区的写法，最坏时间复杂度虽然还是 `O(n)`，但是比上面的方法好了很多。

```python
class CQueue:
    def __init__(self):
        self.sti = []
        self.sto = []

    def appendTail(self, value: int) -> None:
        self.sti.append(value)

    def deleteHead(self) -> int:
        if not self.sto:
            while self.sti:
                self.sto.append(self.sti.pop())
        return -1 if not self.sto else self.sto.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

**运行结果：**

> 执行结果：通过  
> 执行用时：560 ms, 在所有 Python3 提交中击败了70.21% 的用户  
> 内存消耗：17 MB, 在所有 Python3 提交中击败了100.00% 的用户

---

`2020.6.30`
