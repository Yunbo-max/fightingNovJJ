# 第13章 布朗运动、鞅、首次到达与Itô

绿皮书对应：§5.4，pp129–136；§5.2。
 
前置章节：06、12

## 这一章要掌握什么

- 布朗运动定义与独立正态增量
- 自然信息流
- 鞅/局部鞅
- 二次变差
- 随机积分
- Itô与多元Itô
- GBM
- 可选停止条件
- 双边退出
- 反射原理
- 带漂移过程
- Feynman–Kac
- 测度与可积性

## 代表题：题意、输入输出与思考过程

输入：标准布朗运动W从0出发，上界a>0、下界−b<0，首次碰到任一边界时停止。
输出：先碰上界的概率和平均退出时间。

用停止后的W和W²−t。先用截断停止时间验证可积与取极限条件，再写期望恒等式。
若p为先到a概率，则0=pa−(1−p)b，得到p=b/(a+b)。
E[τ]=E[W_τ²]=pa²+(1−p)b²=ab。
若过程为σW，平均时间变为ab/σ²，而退出概率不变。
对X=μt+W，μ≠0时由停止的X−μt得到E[X_τ]=μE[τ]。所以对称边界±b的预期收益/预期时间恰好等于μ，不存在仅靠改b获得内点最优的结论。

## 改条件后的变式

- 对GBM的lnS用Itô：漂移变成μ−σ²/2
- 对无限停止时间：必须检查使用的定理条件，不能仅凭过程叫鞅就交换期望与极限

## 不看答案，检查自己是否理解

- 布朗路径能用普通导数dW/dt吗？一般不存在
- 为什么有半个二阶导项？二次变差(dW)²贡献dt量级
- 真实概率P与风险中性Q相同吗？一般不同

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0459 | [Brownian Motion With Unit Drift: Probability of Ever Reaching -1](https://quantvault.org/problem-3677-brownian-motion-with-unit-drift-probability-of-ever-reaching.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0458 | [Hitting 3 Before -5: Brownian Motion With and Without Drift](https://quantvault.org/problem-3676-hitting-3-before-5-brownian-motion-with-and-without-drift.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0386 | [MDP Formulation for Stock Trading](https://quantvault.org/problem-2151-mdp-formulation-for-stock-trading.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0399 | [Martingale Property of Brownian Motion](https://quantvault.org/problem-2251-martingale-property-of-brownian-motion.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-13.md)，共58条。

## 深入讲义与新增方法

- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
