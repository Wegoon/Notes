## 剑指 Offer（第 2 版）刷题记录

#### 动态规划

##### 题单：

1、[剑指 Offer 10- I. 斐波那契数列](https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/)

2、

3、

4、[剑指 Offer 13. 机器人的运动范围](https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

5、

6、

7、





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









##  [剑指 Offer 13. 机器人的运动范围](https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

> 难度：简单 &emsp;&emsp; [牛客地址](https://www.nowcoder.com/practice/6fe361ede7e54db1b84adc81d09d8524?tpId=265&tqId=39207&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D13&difficulty=undefined&judgeStatus=undefined&tags=&title=) &emsp;&emsp; [LeetCode地址](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

### 题目描述

地上有一个m行n列的方格，从坐标 `[0,0]` 到坐标 `[m-1,n-1]` 。一个机器人从坐标 `[0, 0] `的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

### 样例

**示例 1：**

```
输入：m = 2, n = 3, k = 1
输出：3
```

**示例 2：**

```
输入：m = 3, n = 1, k = 0
输出：1
```

### 限制
* `1 <= n, m <= 100`
* `0 <= k <= 20`


----

### 算法

#### 法1）广度优先搜索（BFS）

* 本题可以抽象为一个经典的广度优先搜索问题
* 从每一个点可以向周围四个方向上、下、左、右去扩展（其实本题范围可以缩小为向右和下两个方向 [证明见图片演示](https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/)）


##### 时间复杂度

* 共有 `m` 行、`n` 列，且每个点最多只会被遍历（入队列）一次

* 故时间复杂度为 $O(mn)$ 。

##### 空间复杂度

* 原始空间复杂度是 $O(mn)$ 的；额外需要的空间主要是队列空间的开销，队列用于存储点，不会超过 $m * n$ 个点，故额外空间复杂度为 $O(mn)$。
* 故空间复杂度为 $O(mn)$ 。

##### C++ 代码

```cpp
class Solution {
public:
    int sumDigit(int x) {
        int sum = 0;
        while (x) sum += x % 10, x /= 10;
        return sum;
    }
    int bfs(int m, int n, int k) {
        int num = 0;
        bool st[m][n];
        memset(st, false, sizeof(st));
        queue<pair<int, int>> q;
        q.push({0, 0});
        num++;
        st[0][0] = true;
        int dx[4] = {-1, 0, 0, 1}, dy[4] = {0, -1, 1, 0};
        while (q.size()) {
            auto h = q.front();
            q.pop();
            for (int i = 0; i < 4; i++) {
                int x = h.first + dx[i];
                int y = h.second + dy[i];
                if (x < 0 || y < 0 || x >= m || y >= n || st[x][y] || sumDigit(x) + sumDigit(y) > k) continue;
                st[x][y] = true;
                num++;
                q.push({x, y});
            }
        }
        return num;
    }
    int movingCount(int m, int n, int k) {
        return bfs(m, n, k);
    }
};
```

##### Python3 代码

```python
class Solution:
    def sumDigit(self, x):
        sum = 0
        while x:
            sum += x % 10
            x //= 10
        return sum

    def bfs(self, m, n, k):
        from queue import Queue
        q = Queue()
        st = {(0, 0)}
        q.put((0, 0))
        dxy = ((-1, 0), (0, -1), (0, 1), (1, 0))
        while not q.empty():
            x, y = q.get()
            for dx, dy in dxy:
                x0, y0 = x + dx, y + dy
                if x0 < 0 or y0 < 0 or x0 >= m or y0 >= n or (x0, y0) in st or self.sumDigit(x0) + self.sumDigit(y0) > k:
                    continue
                st.add((x0, y0))
                q.put((x0, y0))
        return len(st)

    def movingCount(self, m: int, n: int, k: int) -> int:
        return self.bfs(m, n, k)
```

#### 法2）深度优先搜索（DFS）

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
#### 法3）递推 / 动态规划

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