# 24章合并学习目录

目标：把绿皮书的基础框架、QuantVault公开题、以及其余题目的公开方法资料合成一条复习路线。
每章顺序：题目问什么 → 输入输出与约束 → 选择方法 → 推导代表题 → 改条件做变式 → 自测。
完整题目索引保留所有动态目录ID；只按标题匹配的方法链接，和已阅读原题的记录严格区分。

| 章 | 章节 | 必须会的主线 | 绿皮书对应 | 目录题数 |
|---|---|---|---|---:|
| 01 | [组合计数与概率事件](chapters/01-counting-probability.md) | 样本空间与等可能性、事件的交并补、加法与乘法原理、排列、组合、多重排列 | §4.1–4.2，pp59–72 | 271 |
| 02 | [条件概率与贝叶斯](chapters/02-conditional-bayes.md) | 条件样本空间、条件概率、全概率、Bayes公式 | §4.3，pp72–86 | 330 |
| 03 | [随机变量、分布与变量变换](chapters/03-random-variables.md) | PMF/PDF/CDF及取值域、Bernoulli/Binomial/Geometric/Poisson、Uniform/Normal/Exponential/Gamma/Beta、联合、边缘与条件分布 | §4.4，pp86–92 | 137 |
| 04 | [期望、方差、相关与顺序统计](chapters/04-expectation-moments.md) | 期望线性性与指示变量、尾和/尾积分、方差与协方差、相关与独立 | §4.5–4.6，pp92–103；§3.2，p40 | 288 |
| 05 | [递推期望、最优停止与博弈](chapters/05-recurrences-games.md) | 状态与充分信息、第一次转移分析、递推期望、自循环 | §5.2–5.3，pp115–128；§2.1 | 129 |
| 06 | [微积分、泰勒展开与微分方程](chapters/06-calculus-ode.md) | 极限与定义域、乘商链式/对数求导、极值与边界、LHopital条件 | §3.1–3.5，pp33–50 | 25 |
| 07 | [向量、矩阵、秩与正定性](chapters/07-matrix-foundations.md) | 维度与矩阵乘法、内积与范数、线性组合与独立、列空间/零空间/秩 | §3.6，pp50–58 | 3 |
| 08 | [QR、特征分解、PCA、Cholesky与SVD](chapters/08-decompositions.md) | HouseholderQR与回代、最小二乘投影、特征值特征向量、谱定理 | §3.6，pp50–58 | 57 |
| 09 | [参数估计、区间、检验与多重选择](chapters/09-statistics-inference.md) | 样本与参数、似然、MLE、MAP、偏差、方差、一致性、Fisher信息与条件 | 绿皮书§4.4–4.5为基础；网站系统补充 | 144 |
| 10 | [线性回归、正则化与诊断](chapters/10-regression.md) | OLS几何与正规方程、有无截距、条件外生性、异方差/自相关/内生性 | §3.6，pp50–53；网站Regression补充 | 171 |
| 11 | [约束优化、投资组合与Kelly](chapters/11-optimization-portfolios.md) | 目标、变量、约束与单位、凸集凸函数、梯度Hessian、Lagrange与KKT | §3.4，pp41–46；§6.4，pp163–169 | 172 |
| 12 | [马尔可夫链、随机游走与泊松过程](chapters/12-markov-random-walk.md) | 状态、转移概率与充分性、平稳分布与收敛条件、吸收概率/时间、birth–death链 | §5.1–5.2，pp105–121；§4.3 | 146 |
| 13 | [布朗运动、鞅、首次到达与Itô](chapters/13-brownian-ito.md) | 布朗运动定义与独立正态增量、自然信息流、鞅/局部鞅、二次变差 | §5.4，pp129–136；§5.2 | 58 |
| 14 | [金融基础、无套利、远期与复制](chapters/14-finance-foundations.md) | 现金流、现值与贴现、复利与计息口径、收益率与美元损益、多空、杠杆与自融资 | §6.1及§6.4，pp137–149、163–169 | 25 |
| 15 | [期权定价、风险中性、二叉树与BS](chapters/15-option-pricing.md) | 合约方向、call/put与payoff、欧式与美式、风险中性条件期望、二叉树与复制 | §6.1，pp137–149；§6.3，pp158–162 | 33 |
| 16 | [Greeks、对冲、隐含波动率与PnL](chapters/16-greeks-iv.md) | Delta/Gamma/Theta/Vega/Rho、高阶与交叉Greeks、单位与报价尺度、Taylor盈亏归因 | §6.2，pp149–158 | 59 |
| 17 | [固定收益、久期凸性与利率模型](chapters/17-fixed-income.md) | 债券现金流与价格、yield与零息曲线、修正久期与DV01、凸性 | §6.4，pp163–169 | 44 |
| 18 | [市场微观结构、做市与执行](chapters/18-microstructure.md) | bid/ask/mid与spread、限价单/市价单/撮合与优先级、逆向选择、GlostenMilgrom | 网站MarketMicrostructure系统补充 | 106 |
| 19 | [时间序列、研究设计与回测](chapters/19-time-series-backtesting.md) | 价格/收益与平稳性、AR/MA/ARMA、ACF/PACF、条件异方差 | 网站TimeSeries与Finance补充 | 117 |
| 20 | [机器学习、校准与样本外验证](chapters/20-machine-learning.md) | 监督目标与标签、biasvariance、损失与业务效用、逻辑回归 | 网站MachineLearning系统补充 | 92 |
| 21 | [算法、数据结构与流式状态](chapters/21-coding-data-structures.md) | 输入输出与状态、复杂度计数、数组字符串、dict/set | §7.1–7.2，pp171–183 | 594 |
| 22 | [动态规划、贪心、搜索与图](chapters/22-dp-greedy-graphs.md) | 递归与记忆化、状态充分性、无后效性与转移、0/1与完全背包 | §5.3，pp121–128；§7.1 | 168 |
| 23 | [数值求根、MonteCarlo与有限差分](chapters/23-numerical-methods.md) | 二分/Newton/secant与停止准则、浮点范围与消去误差、稳定logsumexp、数值微分步长 | §3.4，pp41–46；§7.3，pp184–191 | 105 |
| 24 | [BrainTeasers九类方法与证明](chapters/24-brainteasers.md) | 小规模简化、逆向归纳、知识状态与逻辑排除、对称性与互补 | 第2章，pp3–32 | 111 |

## 章节之外的完整补充

- [绿皮书完整知识地图与150题组索引](notes/greenbook_curriculum.md)
- [全部方法族](data/method_families.json)
- [公开一手来源与例题](data/public_references.json)
- [逐题原文审阅与勘误](data/question_reviews.json)
- [本周五天计划](WEEK_PLAN.md)
- [实际来源覆盖范围](SCOPE.md)
- [持续学习记忆](MEMORY.md)
