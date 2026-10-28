# 第02章 条件概率与贝叶斯

绿皮书对应：§4.3，pp72–86。
 
前置章节：01

## 这一章要掌握什么

- 条件样本空间
- 条件概率
- 全概率
- Bayes公式
- 先验、似然、后验
- 后验赔率与似然比
- 抽样/报告机制
- MontyHall
- 见证人可靠性
- Beta–Bernoulli更新
- 信息价值

## 代表题：题意、输入输出与思考过程

输入：袋中等概率选到公平硬币或双正面硬币，观察连续3次正面。
输出：选到双正面硬币的后验概率。

两种假设的先验都为1/2；观察概率分别是1和(1/2)^3=1/8。
后验= (1×1/2)/(1×1/2+(1/8)×1/2)=8/9。
后验赔率=先验赔率1 × 似然比8。
下一次正面的预测概率=8/9×1+1/9×1/2=17/18。
“随机看见一个正面”与“主动翻三次得到正面”可能有不同抽样机制，必须先把观测过程写清楚。

## 改条件后的变式

- 把公平硬币先验改成90%：重新乘先验，不能保留8/9
- 加入观测费用：后验更新之外，还需要比较信息的期望收益与成本

## 不看答案，检查自己是否理解

- 后验概率和下一次正面概率相同吗？不同，此例是8/9与17/18
- 为什么低基率会改变可靠检测的解释？后验分母包含大量非目标人群产生的假阳性
- 只知道“至少一个孩子是男孩”够吗？还要明确家庭如何被抽样、信息如何被报告

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0148 | [Fixed Point Probability in a Random Permutation](https://quantvault.org/problem-419-fixed-point-probability-in-a-random-permutation.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0177 | [The Birthday Problem: Shared Birthdays in a Room](https://quantvault.org/problem-518-the-birthday-problem-shared-birthdays-in-a-room.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0106 | [Bayesian Coin Identification](https://quantvault.org/problem-235-bayesian-coin-identification.html) | 原题及站内解答已读 |
| QV-F0037 | [Bayesian Die Identification](https://quantvault.org/problem-64-bayesian-die-identification.html) | 原题及站内解答已读 |

本章全部目录题：[题目索引](../indexes/chapter-02.md)，共330条。

## 深入讲义与新增方法

- [probability_curriculum.md](../notes/probability_curriculum.md)
- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
