## 剑指 Offer（第 2 版）刷题记录

#### 动态规划

##### 题单：

1、[剑指 Offer 10- I. 斐波那契数列](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/)

2、







##### 题解：

## [剑指 Offer 10- I. 斐波那契数列](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/)

> 难度：简单 &emsp;&emsp; [牛客地址](https://www.nowcoder.com/practice/6fe361ede7e54db1b84adc81d09d8524?tpId=265&tqId=39207&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D13&difficulty=undefined&judgeStatus=undefined&tags=&title=) &emsp;&emsp; [LeetCode地址](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

### 题目描述

写一个函数，输入 `n` ，求斐波那契（Fibonacci）数列的第 `n` 项（即 `F(N)`）。斐波那契数列的定义如下：

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```

斐波那契数列由 `0` 和 `1` 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 `1e9+7（1000000007）`，如计算初始结果为：`1000000008`，请返回 `1`。

### 样例

**示例 1：**

```
输入：n = 2
输出：1
```

**示例 2：**

```
输入：n = 5
输出：5
```

### 限制
* `0 <= n <= 100`


----

### 算法

#### 法1）动态规划 / 递推

* 本题 动态转移方程 / 递推公式 已给出，直接跑就可以


##### 时间复杂度

* 从前往后，`i` 从 `2` 遍历到 `n`。每次求出一个 `F(i)` 的值，当 `i = n` 的时候，求得 `F(n)` 的值 。

* 故时间复杂度为 $O(n)$ 。

##### 空间复杂度

* 我们发现当前 `F(i)` 只与 `F(i - 2)` 、 `F(i - 1)` 有关。
* 因此，我们可以只定义3个变量，`last`、`pre` 和 `now` 分别代表 `F(i - 2)`、`F(i - 1)` 和 `F(i)`，这样空间复杂度可以优化成 `O(1)`。
* 额外空间复杂度为 $O(1)$ 。

##### C++ 代码

```cpp
class Solution {
public:
    int fib(int n) {
        int last = 0, pre = 1, now;
        if (n < 2) return n;
        for (int i = 2; i <= n; i++) {
            now = (last + pre) % 1000000007;
            last = pre, pre = now;
        }
        return now;
    }
};
```

##### Python3 代码

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            last = 0; pre = 1
            for i in range(2, n + 1):
                now = (last + pre) % 1000000007
                last = pre; pre = now
            return now
```





