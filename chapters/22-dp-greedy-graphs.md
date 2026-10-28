# 第22章 动态规划、贪心、搜索与图

绿皮书对应：§5.3，pp121–128；§7.1。
 
前置章节：05、21

## 这一章要掌握什么

- 递归与记忆化
- 状态充分性
- 无后效性与转移
- 0/1与完全背包
- 区间DP
- LIS与支配压缩
- 贪心交换论证
- 回溯剪枝
- BFS/DFS
- DAG与拓扑
- Dijkstra条件
- 连通分量
- 状态扩维
- 最优性与边界

## 代表题：题意、输入输出与思考过程

输入：硬币面额[1,3,4]，每种可无限使用，目标金额6。
输出：最少硬币数。

每次取最大面额会得到4+1+1，共3枚；真正最优是3+3，共2枚。
定义f(a)=凑出金额a所需的最少枚数。f(0)=0，凑不出的状态为∞。
若最后一枚是c，之前必须最优地凑出a−c，所以f(a)=min_{c≤a}(f(a−c)+1)。
递归函数f配合缓存，或从小金额向上填表，都是同一DP；只递归却不复用状态会重复计算。
对BurstBalloons，考虑区间内“最后戳哪个”，固定两端边界，才能把左右子问题独立。转移为dp[l,r]=max_k(dp[l,k]+a_l a_k a_r+dp[k,r])，其中(l,r)内部待戳、两端暂保留。

## 改条件后的变式

- 每枚硬币最多用一次：要增加物品维度或倒序更新，不能继续用完全背包循环
- 网格移动方向交替：状态要加入下一次允许的方向，单个坐标不够

## 不看答案，检查自己是否理解

- 贪心为什么需要证明？局部最优可能破坏未来可行解或更好组合
- DP是一定用二维数组吗？不是，维度由状态决定
- BFS何时给最短距离？无权或等边权按步数，带权需相应算法与假设

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0408 | [Uniform Sampling Game - Fair Price](https://quantvault.org/problem-2791-uniform-sampling-game-fair-price.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0287 | [Maximum Profit from Stock Trades](https://quantvault.org/problem-1287-maximum-profit-from-stock-trades.html) | 原题及站内解答已读 |
| QV-F0273 | [Number of Islands in a Grid](https://quantvault.org/problem-1180-number-of-islands-in-a-grid.html) | 原题及站内解答已读 |
| QV-F0209 | [24 Game Solver](https://quantvault.org/problem-666-24-game-solver.html) | 原题及站内解答已读 |

本章全部目录题：[题目索引](../indexes/chapter-22.md)，共168条。

## 深入讲义与新增方法

- [coding_curriculum.md](../notes/coding_curriculum.md)
- [expectation_games_curriculum.md](../notes/expectation_games_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
