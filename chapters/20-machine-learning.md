# 第20章 机器学习、校准与样本外验证

绿皮书对应：网站MachineLearning系统补充。
 
前置章节：09、10、19

## 这一章要掌握什么

- 监督目标与标签
- biasvariance
- 损失与业务效用
- 逻辑回归
- 树/随机森林/Boosting
- KMeans
- 特征缩放/缺失值
- 正则化
- 超参选择与nestedvalidation
- 分布外泛化
- 概率校准
- 模型选择与泄漏
- SGD/momentum/batchnorm基础

## 代表题：题意、输入输出与思考过程

输入：训练特征为[2,4,缺失]，测试时观测到100。
输出：训练阶段缺失值应怎样填补，并保持真实的样本外流程。

只在训练集拟合填补器：训练均值为3，缺失填3。测试值100不能参与这个参数的估计。
同样，标准化、特征筛选、PCA、超参数与阈值都应在相应训练层内拟合。
若目标是成功概率p，logloss与Brier等是评价概率的工具；若目标是交易，还要把概率/预测值转成动作并计成本和风险。
模型在样本外是否准确、概率是否校准、决策是否有用，是不同检查，不能只用训练准确率回答。

## 改条件后的变式

- 多次看同一个测试集选模型：测试集已成为调参信息
- 特征在训练有意义而部署时定义改变：属于分布或测量机制变化，需要专门验证

## 不看答案，检查自己是否理解

- 随机森林与Boosting如何减少误差？前者聚合去相关树，后者迭代拟合当前损失的剩余结构
- 更高R²必然更高PnL吗？不必然
- 校准好意味着预测很有区分力吗？不一定，常数基率也可能校准

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0340 | [Gradient Boosting vs. Random Forests, Batch Normalization, and SGD Momentum](https://quantvault.org/problem-1743-gradient-boosting-vs-random-forests-batch-normalization-and-.html) | 原题及站内解答已读 |
| QV-F0341 | [Hyperparameter Selection in Machine Learning](https://quantvault.org/problem-1746-hyperparameter-selection-in-machine-learning.html) | 原题及站内解答已读 |
| QV-F0306 | [Out-of-Distribution Prediction: Dog Weight Regression](https://quantvault.org/problem-1465-out-of-distribution-prediction-dog-weight-regression.html) | 原题及站内解答已读 |
| QV-F0385 | [Comparing Forecasting Models for Daily Asset Returns](https://quantvault.org/problem-2126-comparing-forecasting-models-for-daily-asset-returns.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-20.md)，共92条。

## 深入讲义与新增方法

- [statistics_ml_curriculum.md](../notes/statistics_ml_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
