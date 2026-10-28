# 第05章 递推期望、最优停止与博弈

绿皮书对应：§5.2–5.3，pp115–128；§2.1。
 
前置章节：02、03、04

## 这一章要掌握什么

- 状态与充分信息
- 第一次转移分析
- 递推期望
- 自循环
- 吸收边界
- Bellman方程
- 停止/继续比较
- 有限期倒推
- 无限期存在性
- 海盗与逆向归纳
- Nim败态
- 混合策略
- Kelly与信息成本
- 拍卖与机制条件

## 代表题：题意、输入输出与思考过程

输入：最多掷公平六面骰3次，每次可以接受当前点数并结束，也可以放弃继续，最后一次必须接受。
输出：最优接受规则和开始时的期望收入。

只有一次机会时V_1=3.5。
剩两次时，接受当前x与继续价值3.5比较，所以4、5、6接受。V_2=(3×3.5+4+5+6)/6=4.25。
剩三次时，继续价值为4.25，因此第一次只在5、6接受。
V_3=(4×4.25+5+6)/6=14/3≈4.6667。
状态必须包含剩余次数；若重掷收费，继续价值改为V_{k−1}−费用。

## 改条件后的变式

- 公平随机游走允许无限等到赢：先检查停止时间与可选停止条件
- 海盗人数超过金币能买的选票数：生存价值可改变买票成本，不能一直外推小规模公式

## 不看答案，检查自己是否理解

- 为什么不能一直贪当前最高收益？动作改变剩余机会与未来状态
- 递归与DP是什么关系？递归是实现方式，DP复用相同状态的子问题
- 停止边界是什么？立即收益不低于条件继续价值的状态集合

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0298 | [Card Game: Redraw vs. Switch Option](https://quantvault.org/problem-1366-card-game-redraw-vs-switch-option.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0288 | [Minimax Card Number Assignment](https://quantvault.org/problem-1289-minimax-card-number-assignment.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0245 | [Nim-Style Counting Game: Optimal Strategy and Losing Positions](https://quantvault.org/problem-1002-nim-style-counting-game-optimal-strategy-and-losing-position.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0063 | [Optimal Stopping in a Blue-Red Ball Draw](https://quantvault.org/problem-122-optimal-stopping-in-a-blue-red-ball-draw.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-05.md)，共129条。

## 深入讲义与新增方法

- [expectation_games_curriculum.md](../notes/expectation_games_curriculum.md)
- [coding_curriculum.md](../notes/coding_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
