# 第15章 期权定价、风险中性、二叉树与BS

绿皮书对应：§6.1，pp137–149；§6.3，pp158–162。
 
前置章节：13、14

## 这一章要掌握什么

- 合约方向、call/put与payoff
- 欧式与美式
- 风险中性条件期望
- 二叉树与复制
- BS模型假设和公式
- 终端/边界条件
- 价格单调性凸性与无套利界
- 奇异/路径依赖期权
- 完整执行价曲线与终端分布

## 代表题：题意、输入输出与思考过程

输入：股票现价100，一期后只会到110或90，零利率，欧式看涨K=100。
输出：当前无套利期权价。

到期payoff分别为10、0。复制组合持Δ股并持有现金B，要求110Δ+B=10，90Δ+B=0。
相减得Δ=.5，再得B=−45。所以初始价值100×.5−45=5。
等价地，风险中性上涨概率p=(1−.9)/(1.1−.9)=.5，贴现期望=.5×10+.5×0=5。
p是复制导出的定价概率，不需要等于真实上涨概率。若要保证0<p<1，树的上涨、下跌与无风险增长必须满足相应无套利关系。
美式看跌的提前行权价值是(K−S)^+；数值网格给近似结果并需要误差控制。

## 改条件后的变式

- 增加股息：重新调整漂移和复制现金流
- 从执行价二阶导恢复的是定价测度下的分布，不能直接称为真实黑天鹅概率

## 不看答案，检查自己是否理解

- 知道E[S_T]够给任意期权定价吗？不够，需要相应分布/状态价格
- 无股息美式call为什么通常不提前行权？在标准非负利率假设下等待保留时间价值并推迟付K
- 静态无套利凸性允许等号吗？允许，是否有严格套利还依赖可执行组合与状态支持

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0347 | [Option Pricing on a Dice Product](https://quantvault.org/problem-1784-option-pricing-on-a-dice-product.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0463 | [Quick Value of an At-the-Money Call: 0.4 Sigma S Root Tau](https://quantvault.org/problem-3682-quick-value-of-an-at-the-money-call-0-4-sigma-s-root-tau.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0295 | [Binomial Tree Option Pricer](https://quantvault.org/problem-1360-binomial-tree-option-pricer.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0392 | [European Call Option With Infinite Maturity](https://quantvault.org/problem-2204-european-call-option-with-infinite-maturity.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-15.md)，共33条。

## 深入讲义与新增方法

- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
