# 第14章 金融基础、无套利、远期与复制

绿皮书对应：§6.1及§6.4，pp137–149、163–169。
 
前置章节：04、06、11

## 这一章要掌握什么

- 现金流、现值与贴现
- 复利与计息口径
- 收益率与美元损益
- 多空、杠杆与自融资
- 无套利与复制
- 远期/期货及carry
- 股息与融资
- put–call parity
- 风险中性定价的假设
- 交易成本与约束

## 代表题：题意、输入输出与思考过程

输入：无股息股票现价100，无风险连续利率5%，一年远期。
输出：在无交易成本且可按该利率融资等假设下的远期价格。

现在借100买股票，到期还100e^.05。持股组合到期提供一股，因此无套利远期价格F=100e^.05≈105.127。
若确定连续股息率为q，公式变为F=S exp[(r−q)T]。
这是复制现金流决定的价格，不能直接当作真实世界下一年股价的预测均值。
比较组合时先写每个时间点的现金流，再检查初始成本及终端风险。正期望但仍可能亏损的下注，不等于无风险套利。

## 改条件后的变式

- 有仓储成本、便利收益、融资限制：重新写carry与可执行交易
- 随机利率下远期与期货：需要区分结算机制及与利率的相关性

## 不看答案，检查自己是否理解

- 远期价高于现价一定有套利吗？不一定，要计融资、股息与carry
- 概率高的交易是否一定套利？不是
- 一份资产的收益率与持仓美元PnL怎样连接？价格变动乘持仓数量，并分别计入现金流与费用

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0355 | [Implied Probabilities and Bookmaker Overround](https://quantvault.org/problem-1855-implied-probabilities-and-bookmaker-overround.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0159 | [Minimal Market Spread Under Correlation Uncertainty](https://quantvault.org/problem-459-minimal-market-spread-under-correlation-uncertainty.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-14.md)，共25条。

## 深入讲义与新增方法

- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
