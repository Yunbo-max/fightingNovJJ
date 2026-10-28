# 第10章 线性回归、正则化与诊断

绿皮书对应：§3.6，pp50–53；网站Regression补充。
 
前置章节：07、08、09

## 这一章要掌握什么

- OLS几何与正规方程
- 有无截距
- 条件外生性
- 异方差/自相关/内生性
- 系数标准误
- R²/调整R²
- 遗漏变量与抑制变量
- 共线性与VIF
- Ridge/Lasso
- GLS/WLS
- 分位数/Huber回归
- 大数据分布式或流式求解

## 代表题：题意、输入输出与思考过程

输入：x=[0,1,2]、y=[1,2,2]，拟合y≈a+bx。
输出：使残差平方和最小的a、b。

x均值1，y均值5/3。中心化后Σ(x−xbar)²=2，Σ(x−xbar)(y−ybar)=1。
所以b=1/2，a=5/3−1/2=7/6。
残差为[−1/6,1/3,−1/6]，与常数列和x列都正交。
正交是这次样本拟合的代数性质；若想说系数无偏，要有合适的数据生成与外生性条件，不能从残差正交倒推出因果关系。
Ridge解的奇异方向增益是s/(s²+λ)，缓和小奇异值的放大；Lasso引入不可微点，可能产生稀疏系数。

## 改条件后的变式

- 加入重复列：拟合值可唯一，但系数可能不唯一
- 预测未来收益时：滚动训练、时间对齐和成本评估要与回归一起设计

## 不看答案，检查自己是否理解

- 加入变量后训练R²会下降吗？同一OLS样本与设置下不会，但样本外可能更差
- E[误差]=0足够保证随机设计OLS无偏吗？不够，通常使用E[误差|X]=0
- 两个变量正相关为何多元系数可能负？控制其他变量后考察的是条件关系

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0309 | [R-Squared Invariance Under Transformations](https://quantvault.org/problem-1480-r-squared-invariance-under-transformations.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0041 | [Bridge and Lantern Crossing Optimization](https://quantvault.org/problem-69-bridge-and-lantern-crossing-optimization.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0319 | [Computing OLS When the Design Matrix Is Too Large for Memory](https://quantvault.org/problem-1543-computing-ols-when-the-design-matrix-is-too-large-for-memory.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0325 | [Effects of Multicollinearity on Regression](https://quantvault.org/problem-1569-effects-of-multicollinearity-on-regression.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-10.md)，共171条。

## 深入讲义与新增方法

- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)
- [algebra_optimization_curriculum.md](../notes/algebra_optimization_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
