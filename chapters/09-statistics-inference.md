# 第09章 参数估计、区间、检验与多重选择

绿皮书对应：绿皮书§4.4–4.5为基础；网站系统补充。
 
前置章节：02、03、04、06、07

## 这一章要掌握什么

- 样本与参数
- 似然、MLE、MAP
- 偏差、方差、一致性
- Fisher信息与条件
- LLN/CLT适用条件
- 标准误与置信区间
- 检验、p值、功效
- bootstrap与时间依赖
- 多重检验/FDR
- Bayesian后验与预测
- 等相关样本有效信息

## 代表题：题意、输入输出与思考过程

输入：独立Bernoulli观测[1,1,0]，估计成功概率θ。
输出：MLE以及在Beta(1,1)先验下的后验均值。

似然L(θ)=θ²(1−θ)。对数似然求导2/θ−1/(1−θ)=0，得到MLE=2/3。
Beta–Bernoulli共轭更新：后验Beta(3,2)，后验均值3/5。
这两个答案针对不同估计规则，都不等于“真θ已经被知道”。
若给样本均值做区间，IID时标准误是s/√n；序列相关时要使用长期方差/HAC或适当的区块重采样，不能把相关样本当成独立样本直接套。

## 改条件后的变式

- 全0数据且参数只允许(0,1)：只有边界上确界，没有区间内MLE
- 同时筛选很多alpha：单个p<0.05不能直接解释为发现稳定信号

## 不看答案，检查自己是否理解

- 95%置信区间的频率解释是什么？重复构造的区间有95%覆盖固定真值
- p值是原假设为真的概率吗？不是
- BH在任意依赖下都控制FDR吗？需要独立/合适正依赖等条件，任意依赖可考虑BY等方法

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0223 | [MLE for a Bernoulli Parameter](https://quantvault.org/problem-795-mle-for-a-bernoulli-parameter.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0260 | [Correct Interpretation of a Frequentist Confidence Interval](https://quantvault.org/problem-1102-correct-interpretation-of-a-frequentist-confidence-interval.html) | 原题及站内解答已读 |
| QV-F0317 | [Bayesian Update from a No-Trade Event](https://quantvault.org/problem-1529-bayesian-update-from-a-no-trade-event.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0300 | [False Discovery in Alpha Mining](https://quantvault.org/problem-1400-false-discovery-in-alpha-mining.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-09.md)，共144条。

## 深入讲义与新增方法

- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)
- [probability_curriculum.md](../notes/probability_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
