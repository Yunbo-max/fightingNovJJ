# 第04章 期望、方差、相关与顺序统计

绿皮书对应：§4.5–4.6，pp92–103；§3.2，p40。
 
前置章节：01、02、03

## 这一章要掌握什么

- 期望线性性与指示变量
- 尾和/尾积分
- 方差与协方差
- 相关与独立
- 全期望和全方差
- 条件期望作为投影
- 顺序统计与最大最小值
- CouponCollector
- 随机和与Wald条件
- 矩不等式与尾界
- 极值与记录过程

## 代表题：题意、输入输出与思考过程

输入：Z为标准正态，问只在Z>0时取平均，得到多少。
输出：条件均值 E[Z|Z>0]。

先算未归一化的一半积分：E[Z·1{Z>0}]=∫_0^∞ zφ(z)dz=φ(0)=1/√(2π)。
条件化还需要除以P(Z>0)=1/2，所以 E[Z|Z>0]=√(2/π)。
这正是绿皮书p40需要修正的归一化遗漏。
另一个常用例子：n个独立U(0,1)的最大值M满足P(M≤x)=x^n，密度为nx^(n−1)，均值n/(n+1)。

## 改条件后的变式

- 若问最大值的方差：继续积分求二阶矩，不能只知道均值
- 抽样相关时：最大值CDF不能直接写边缘CDF的乘积

## 不看答案，检查自己是否理解

- 总方差怎么拆？E[Var(X|Y)]+Var(E[X|Y])
- E[X/Y]能否写成E[X]/E[Y]？一般不能
- 有限阈值的精确答案等于更新过程极限吗？通常只有渐近接近，必须检查阈值与假设

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0003 | [Breaking a Stick into a Triangle](https://quantvault.org/problem-7-breaking-a-stick-into-a-triangle.html) | 原题及站内解答已读 |
| QV-F0091 | [Maximum of Multiple Dice Rolls](https://quantvault.org/problem-193-maximum-of-multiple-dice-rolls.html) | 原题及站内解答已读 |
| QV-F0083 | [Dice Sum vs. Coin Flip Count](https://quantvault.org/problem-170-dice-sum-vs-coin-flip-count.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0135 | [Expected Adjacent Couples at a Round Table](https://quantvault.org/problem-368-expected-adjacent-couples-at-a-round-table.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-04.md)，共288条。

## 深入讲义与新增方法

- [probability_curriculum.md](../notes/probability_curriculum.md)
- [expectation_games_curriculum.md](../notes/expectation_games_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
