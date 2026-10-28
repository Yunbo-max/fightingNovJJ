# 第11章 约束优化、投资组合与Kelly

绿皮书对应：§3.4，pp41–46；§6.4，pp163–169。
 
前置章节：06、07、08、09

## 这一章要掌握什么

- 目标、变量、约束与单位
- 凸集凸函数
- 梯度Hessian
- Lagrange与KKT
- 约束资格与Slater
- 二次规划
- 最小方差与对冲
- 多信号组合
- 协方差收缩
- 交易成本/换手约束
- Kelly与分数Kelly
- 可行性及边界

## 代表题：题意、输入输出与思考过程

输入：两个不相关、方差都为1的资产，权重为w和1−w。
输出：全投资组合的最小方差权重。

组合方差v(w)=w²+(1−w)²。求导4w−2=0，得到w=1/2，方差为1/2。
一般PD协方差Σ、允许做空且只有1ᵀw=1约束时，最小方差权重为Σ^−1 1/(1ᵀΣ^−1 1)；实现中解线性方程即可，不必显式求逆。
另一个目标是最大化长期对数财富。胜率p、赢时净赔率b、每次下注比例f，目标g(f)=p ln(1+bf)+(1−p)ln(1−f)。
内点解f*=[bp−(1−p)]/b；还要检查下注范围和财富正值条件。p=.6、b=1时f*=.2。

## 改条件后的变式

- 禁止做空或增加换手上限：原闭式权重一般不再成立
- 加入估计误差与回撤约束：全Kelly不自动成为合适策略，需重新定义风险目标

## 不看答案，检查自己是否理解

- KKT点一定全局最优吗？凸问题在相应条件下是，非凸问题一般不是
- 最大收益与最小风险是同一目标吗？不是
- 只知道每个信号方差够确定最优组合吗？还需要相关/协方差结构及目标

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0352 | [Basket Return and Dollar P&L Calculation](https://quantvault.org/problem-1827-basket-return-and-dollar-p-l-calculation.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0303 | [Mean as the Minimizer of Squared Loss](https://quantvault.org/problem-1437-mean-as-the-minimizer-of-squared-loss.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0360 | [Systematic vs. Idiosyncratic Risk](https://quantvault.org/problem-1885-systematic-vs-idiosyncratic-risk.html) | 原题及站内解答已读 |
| QV-F0297 | [Blackjack Bonus Wagering Strategy](https://quantvault.org/problems.html?id=1362) | 原题已读；站内解答未读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-11.md)，共172条。

## 深入讲义与新增方法

- [algebra_optimization_curriculum.md](../notes/algebra_optimization_curriculum.md)
- [expectation_games_curriculum.md](../notes/expectation_games_curriculum.md)
- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
