# 第03章 随机变量、分布与变量变换

绿皮书对应：§4.4，pp86–92。
 
前置章节：01、02

## 这一章要掌握什么

- PMF/PDF/CDF及取值域
- Bernoulli/Binomial/Geometric/Poisson
- Uniform/Normal/Exponential/Gamma/Beta
- 联合、边缘与条件分布
- 变量变换Jacobian
- 卷积
- MGF/特征函数
- 离散原子与连续密度
- 截断与裁剪
- 正态联合性与独立

## 代表题：题意、输入输出与思考过程

输入：两个独立 U(0,1) 随机变量 U、V，令 S=U+V。
输出：S 的密度与 P(S>1)。

固定 S=s，允许的U区间为 max(0,s−1) 到 min(1,s)，其长度就是卷积密度。
于是 f_S(s)=s（0<s<1），f_S(s)=2−s（1≤s<2），其他位置为0。
密度图是面积为1的三角形；对称性给 P(S>1)=1/2。
这里“每个U,V均匀”不代表“和S均匀”。密度高度也不是单点概率。

## 改条件后的变式

- 改成乘积或比值：先用CDF确定可行区域，再求导或作Jacobian
- 把正态裁剪到区间：端点出现概率质量，不能只保留中间的PDF

## 不看答案，检查自己是否理解

- 连续变量P(X=x)是多少？有密度的连续分布为0
- 不相关能否推出独立？一般不能，联合正态时可以
- 截断与裁剪区别？截断重新条件化，裁剪把尾部概率堆到边界

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0213 | [Correlation Under Linear Transformations](https://quantvault.org/problem-701-correlation-under-linear-transformations.html) | 原题及站内解答已读 |
| QV-F0321 | [Correlation of Sum and Difference](https://quantvault.org/problem-1549-correlation-of-sum-and-difference.html) | 原题及站内解答已读 |
| QV-F0058 | [Matching Colors from Two Jars](https://quantvault.org/problem-109-matching-colors-from-two-jars.html) | 原题及站内解答已读 |
| QV-F0203 | [Probability of More Heads Than Tails With Odd Flips](https://quantvault.org/problem-632-probability-of-more-heads-than-tails-with-odd-flips.html) | 原题及站内解答已读 |

本章全部目录题：[题目索引](../indexes/chapter-03.md)，共137条。

## 深入讲义与新增方法

- [probability_curriculum.md](../notes/probability_curriculum.md)
- [expectation_games_curriculum.md](../notes/expectation_games_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
