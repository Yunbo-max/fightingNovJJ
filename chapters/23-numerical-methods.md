# 第23章 数值求根、MonteCarlo与有限差分

绿皮书对应：§3.4，pp41–46；§7.3，pp184–191。
 
前置章节：06、08、13、15、21

## 这一章要掌握什么

- 二分/Newton/secant与停止准则
- 浮点范围与消去误差
- 稳定logsumexp
- 数值微分步长
- 随机数与inverseCDF/rejection
- MC误差s/√N
- 方差缩减
- 路径/似然比Greeks
- 显式/隐式/CN差分
- 一致性稳定性收敛
- 网格与边界误差

## 代表题：题意、输入输出与思考过程

输入：在[1,2]求x²−2=0的根，要求最终区间宽度不超过10^−3。
输出：有保证的近似区间与次数。

初始宽度1，每次二分减半，k次后宽度2^−k，所以需要k≥ceil(log2(1000))=10。
如果要求的是中点的绝对误差不超过10^−3，则上界为半个区间宽度，9次已足够；两种停止口径不同。
检查端点异号宜比较符号，不要机械计算fa×fb，极小数相乘可能下溢为0。
MC平均值的标准误约为样本标准差/√N；把样本数变4倍，标准误约减半，不是变成四分之一。
热方程显式格式r=κΔt/Δx²需r≤1/2（相应标准边界设定）。减小Δx而不调Δt可能让方法失稳。

## 改条件后的变式

- 给IV用Newton：当Vega很小，要有区间保护与价格可行性检查
- 估数字期权Greek：payoff不光滑时需审查路径求导条件或用合适替代估计器

## 不看答案，检查自己是否理解

- Newton一步很小能保证离根近吗？不能无条件保证
- 两端异号就一定有根吗？还要连续性
- 隐式稳定等于任意离散都收敛吗？还需一致性、边界、可解性与相应分析

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0243 | [Limit of the Fibonacci Ratio](https://quantvault.org/problem-984-limit-of-the-fibonacci-ratio.html) | 原题及站内解答已读 |
| QV-F0277 | [Space Station Population Capacity](https://quantvault.org/problem-1220-space-station-population-capacity.html) | 原题及站内解答已读 |
| QV-F0259 | [Approximating Zeros of a Continuous Function](https://quantvault.org/problem-1085-approximating-zeros-of-a-continuous-function.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0436 | [Bisection vs Secant: Counting Steps to a Root](https://quantvault.org/problem-3642-bisection-vs-secant-counting-steps-to-a-root.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-23.md)，共105条。

## 深入讲义与新增方法

- [coding_curriculum.md](../notes/coding_curriculum.md)
- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [algebra_optimization_curriculum.md](../notes/algebra_optimization_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
