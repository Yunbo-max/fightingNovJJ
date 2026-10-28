# 第16章 Greeks、对冲、隐含波动率与PnL

绿皮书对应：§6.2，pp149–158。
 
前置章节：06、15

## 这一章要掌握什么

- Delta/Gamma/Theta/Vega/Rho
- 高阶与交叉Greeks
- 单位与报价尺度
- Taylor盈亏归因
- 动态对冲与融资
- 实现/隐含波动率
- IV求根及Vega退化
- 数字期权
- Breeden–Litzenberger
- 局部近似与大变动残差

## 代表题：题意、输入输出与思考过程

输入：无股息欧式call，S=K=100,r=.04,σ=.20,τ=.25年。给定明天场景ΔS=1、Δσ=.01、Δt=1/365。
输出：场景下的期权近似PnL，而非预测这些场景一定发生。

当前约有Delta=.559618,Gamma=.039448,Theta=−9.948648/年,Vega=19.723967/波动率绝对单位。
Taylor项分别为.559618、.5×.039448=.019724、−9.948648/365=−.027257、19.723967×.01=.197240。
合计约.749325/份。若持100份且每份对1股，则乘100；股票对冲腿与现金融资腿另外计入。
Vega按波动率变化1个百分点报价时应再除100。Theta按一年还是一天、期权乘数是多少，都必须先说明。
IV把当前市场价格作为输入、σ作为未知量；Newton迭代C误差除以Vega，但Vega很小时应配合有界求根与无套利价格检查。

## 改条件后的变式

- 股价大幅波动：高阶项与交叉项会变得重要
- LongGamma不保证赚钱，还要计Theta、波动率、对冲误差、费用和融资

## 不看答案，检查自己是否理解

- 算Delta时需要输入未来涨幅吗？不需要，涨幅用于场景PnL
- Theta一定负、Volga一定正吗？一般不能如此断言
- Delta中性是否等于所有风险为零？不是，还有Gamma、Vega、跳跃、基差等

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0461 | [Delta of an At-the-Money Call: Above or Below One Half?](https://quantvault.org/problem-3680-delta-of-an-at-the-money-call-above-or-below-one-half.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0462 | [Delta-Hedging a Long Call After a Sudden Jump](https://quantvault.org/problem-3681-delta-hedging-a-long-call-after-a-sudden-jump.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0460 | [Which Way Do Option Prices Move? Six Inputs, Four Options](https://quantvault.org/problem-3678-which-way-do-option-prices-move-six-inputs-four-options.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0296 | [Black-Scholes Assumptions and the American Call Delta](https://quantvault.org/problem-1361-black-scholes-assumptions-and-the-american-call-delta.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-16.md)，共59条。

## 深入讲义与新增方法

- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
