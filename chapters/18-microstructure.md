# 第18章 市场微观结构、做市与执行

绿皮书对应：网站MarketMicrostructure系统补充。
 
前置章节：02、05、11、14

## 这一章要掌握什么

- bid/ask/mid与spread
- 限价单/市价单/撮合与优先级
- 逆向选择
- GlostenMilgrom
- 条件公允价值
- 库存与风险惩罚
- 成交概率和手续费
- 队列位置
- marketimpact
- 执行分拆
- 订单簿状态
- 无交易也是信息

## 代表题：题意、输入输出与思考过程

输入：资产真值可能110或90，先验各一半。20%交易者知道真值，80%是等概率买卖的噪声交易者。
输出：风险中性、无库存成本等简化模型下，观察买单后的条件公允卖价。

P(买|V=110)=.2+.8×.5=.6；P(买|V=90)=.8×.5=.4。
先验对称，因此观察买单后高值概率为.6。
ask=E[V|买]=.6×110+.4×90=102。类似得到bid=98，spread=4。
买单本身携带信息，不能仍按无条件均值100卖出。加入库存、订单大小、成本或成交概率后，优化目标要相应修改。

## 改条件后的变式

- 观察到没有成交：如果不同状态下无成交概率不同，仍可Bayes更新
- 目标只写“最佳报价”：需补充收益、风险、持仓期限和成交模型才能得到唯一最优解

## 不看答案，检查自己是否理解

- spread全部是利润吗？不是，还补偿逆向选择、库存等成本
- 更靠前的队列位置一定值得付出任意价格吗？需要比较成交改善与成本
- P&L撮合队列与交易所订单队列相同吗？是不同任务的数据结构

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0377 | [Order Book Dynamics and Price Formation](https://quantvault.org/problem-2035-order-book-dynamics-and-price-formation.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0151 | [Glosten-Milgrom Zero-Profit Bid-Ask Quotes](https://quantvault.org/problem-425-glosten-milgrom-zero-profit-bid-ask-quotes.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0286 | [Market Making the Population Guessing Game](https://quantvault.org/problem-1285-market-making-the-population-guessing-game.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0387 | [Optimal Bid-Ask Quotes Against an Informed Trader](https://quantvault.org/problem-2163-optimal-bid-ask-quotes-against-an-informed-trader.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-18.md)，共106条。

## 深入讲义与新增方法

- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)
- [coding_curriculum.md](../notes/coding_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
