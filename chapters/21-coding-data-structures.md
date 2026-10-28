# 第21章 算法、数据结构与流式状态

绿皮书对应：§7.1–7.2，pp171–183。
 
前置章节：01

## 这一章要掌握什么

- 输入输出与状态
- 复杂度计数
- 数组字符串
- dict/set
- 栈、队列、deque
- heap
- 排序与二分
- 双指针与滑窗的单调性
- 前缀和
- 单调队列
- 交易FIFO
- 最大回撤
- 流式统计
- SQL与时间连接
- 位运算
- 数值精度

## 代表题：题意、输入输出与思考过程

输入：数组[1,−1,1]，目标和1。
输出：和为1的连续子数组数量。

令前缀和P_j为前j项之和。区间和为1等价于P_j−P_i=1，即寻找此前出现多少次P_j−1。
从频次表{0:1}开始。依次读1、−1、1，当前前缀为1、0、1；查询此前0、−1、0的次数，分别1、0、2，合计3。
然后才把当前前缀计入频次，避免把空区间算进去。输入含负数，普通只增不减的正数滑窗条件不成立。
每项一次查询和更新，期望时间O(n)、额外空间O(n)。这里dict保存的是前缀值的频次，不是元素下标。

## 改条件后的变式

- 求最长区间：保存每个前缀和第一次出现的位置
- 求FIFO已实现PnL：保存未平仓的最老批次及剩余数量，允许部分消耗与反向开仓

## 不看答案，检查自己是否理解

- list.pop(0)是O(1)吗？不是，deque两端操作才适合此类队列
- heap能直接O(1)删任意元素吗？不能
- 整数运算转float后再截断总安全吗？大整数可能丢精度

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0406 | [Evaluate a Reverse-Polish-Notation Expression](https://quantvault.org/problem-2759-evaluate-a-reverse-polish-notation-expression.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0402 | [Maximum Value After Repeated Doubling](https://quantvault.org/problem-2426-maximum-value-after-repeated-doubling.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0469 | [Swap Two Integers Without a Temporary Variable](https://quantvault.org/problem-3689-swap-two-integers-without-a-temporary-variable.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0186 | [Add Two Numbers (Linked List)](https://quantvault.org/problem-546-add-two-numbers-linked-list.html) | 原题及站内解答已读 |

本章全部目录题：[题目索引](../indexes/chapter-21.md)，共594条。

## 深入讲义与新增方法

- [coding_curriculum.md](../notes/coding_curriculum.md)
- [combinatorics_curriculum.md](../notes/combinatorics_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
