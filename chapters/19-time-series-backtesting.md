# 第19章 时间序列、研究设计与回测

绿皮书对应：网站TimeSeries与Finance补充。
 
前置章节：09、10、12、14

## 这一章要掌握什么

- 价格/收益与平稳性
- AR/MA/ARMA
- ACF/PACF
- 条件异方差
- 单位根和协整的假设
- 时间戳与可得性
- 滚动/扩展训练
- 标签重叠与purging
- 交易成本/滑点/换手
- Sharpe与回撤
- 多重选择
- 区块bootstrap与HAC

## 代表题：题意、输入输出与思考过程

输入：X_t=.8X_{t−1}+ε_t，ε独立均值0方差1；取因果平稳解。
输出：长期均值、方差与自相关。

均值0；方差v=.64v+1，所以v=1/.36≈2.7778；lag-k自相关为.8^k。
若把这些依赖样本当IID，均值区间和检验的标准误会出错。
回测还要把每个特征记录为“在哪一刻真正可得”。预测t至t+H收益时，训练标签不能使用验证期内才发生的价格；重叠标签要按区间相交情况purge。
Sharpe是均值/波动率，比较两个策略应同时处理分子分母与配对依赖；事前目标波动率相同不保证真实波动率相同。

## 改条件后的变式

- ARMA中AR和MA公因子抵消：表面有参数也可能退化白噪声
- 历史指数成分股如果用今天名单回测过去：引入存活/未来信息偏差

## 不看答案，检查自己是否理解

- 随机打散训练测试为什么可能不合适？破坏时间可得性并让重叠标签泄漏
- 累计已实现PnL的回撤等于账户净值回撤吗？通常不等
- 样本外好一次能排除模型选择偏差吗？不能

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0365 | [Detecting the Direction of Time in a Price Series](https://quantvault.org/problem-1945-detecting-the-direction-of-time-in-a-price-series.html) | 原题及站内解答已读 |
| QV-F0059 | [Monte Carlo Backtest of Kelly and Fractional Kelly Strategies](https://quantvault.org/problem-112-monte-carlo-backtest-of-kelly-and-fractional-kelly-strategie.html) | 原题及站内解答已读 |
| QV-F0361 | [ACF and PACF of an ARMA(1,1) Process](https://quantvault.org/problem-1893-acf-and-pacf-of-an-arma-1-1-process.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0271 | [Maximum Drawdown in a Sliding Window](https://quantvault.org/problem-1163-maximum-drawdown-in-a-sliding-window.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-19.md)，共117条。

## 深入讲义与新增方法

- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)
- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [coding_curriculum.md](../notes/coding_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
