# 第08章 QR、特征分解、PCA、Cholesky与SVD

绿皮书对应：§3.6，pp50–58。
 
前置章节：07

## 这一章要掌握什么

- HouseholderQR与回代
- 最小二乘投影
- 特征值特征向量
- 谱定理
- PCA坐标与解释方差
- 数据矩阵SVD
- 秩截断
- 伪逆
- 条件数
- Cholesky与相关正态
- 协方差平方根
- 奇异PSD的处理

## 代表题：题意、输入输出与思考过程

输入：协方差Σ=[[2,1],[1,2]]。
输出：主成分方向、解释方差比例，以及相关模拟方法。

单位特征向量v1=(1,1)/√2、v2=(1,−1)/√2，对应特征值3、1。
第一主成分解释3/(3+1)=75%的总方差。新坐标y=Vᵀ(r−μ)，协方差为diag(3,1)。
模拟可取L=[[√2,0],[1/√2,√(3/2)]]，独立Z~N(0,I)，令X=μ+LZ，则Cov(X)=LLᵀ=Σ。
QR解回归应分解原始X=QR，再解Rβ=Qᵀy。先算XᵀX会把2范数条件数平方，之后再QR不能消掉这一步造成的损害。
L通常不满足L²=Σ；它是协方差因子。PCA不相关坐标也只有联合高斯时自动独立。

## 改条件后的变式

- 只保留第一特征值：得到秩1近似，不能再当成可逆协方差直接求逆
- 若D是中心化T×n数据矩阵，Σ=DᵀD/(T−1)，特征值是数据奇异值平方/(T−1)

## 不看答案，检查自己是否理解

- 特征向量可以任意缩放吗？可以，写VΛVᵀ则要使用标准正交基
- 所有小特征值都是噪声吗？不能这样断言
- Q为薄矩阵时QQᵀ是什么？列空间上的正交投影

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0283 | [Eigenvalue Interpretation in PCA](https://quantvault.org/problem-1265-eigenvalue-interpretation-in-pca.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0444 | [Eigenvalues and Eigenvectors of the Matrix [[2, 1], [1, 2]]](https://quantvault.org/problem-3651-eigenvalues-and-eigenvectors-of-the-matrix-2-1-1-2.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0214 | [Eigenvalues of a Rank-1 Matrix](https://quantvault.org/problem-713-eigenvalues-of-a-rank-1-matrix.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0339 | [Eigenvalues of the All-Ones Matrix](https://quantvault.org/problem-1733-eigenvalues-of-the-all-ones-matrix.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-08.md)，共57条。

## 深入讲义与新增方法

- [algebra_optimization_curriculum.md](../notes/algebra_optimization_curriculum.md)
- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
