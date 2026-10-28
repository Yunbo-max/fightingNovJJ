> 当前总复习排期以 [WEEK_PLAN.md](../WEEK_PLAN.md) 为准；本讲义内的领域日程只作为补充建议。

# 线性代数与优化：39条公开目录的复习讲义

本批逐项核对`public_catalog.json`中的线性代数11条、优化28条。**39条均已打开原站公开完整题干和Worked Solution，再独立推导并检查。** 分别记录在`algebra_optimization_reviews.json`的`access`与`status`。不能将“列在免费目录”“有同类绿皮书题”当成已读原站完整解答。

全部39条完成独立图搜索、精确有理数、矩阵或数值恒等式检查；`algebra_optimization_verification.json`保留结果，`verify_algebra_optimization.py`可复跑。数值抽样检查补充数学论证，不能证明未见到的原题条件。

## 先建立的三条主线

**第一条：投影→最小二乘→QR。** 内积衡量沿某方向的分量；把残差要求为正交，得到投影系数。对多个方向逐个减投影得到正交基，把系数放进R就是QR。OLS是把y投影到X的列空间。计算时直接对X作QR或SVD通常比先形成XᵀX更稳；正规方程是数学最优条件，不是默认实现要求。流式数据可以累计充分统计量，但病态时要考虑TSQR等合并分解。

**第二条：协方差→PSD→谱→PCA与模拟。** 任意组合权重w的方差wᵀΣw都不能为负，所以Σ必须PSD。对称矩阵的正交特征基把二次型变成各坐标平方的加权和；每个协方差特征值就是对应主方向的方差。相同的分解既能求最大Rayleigh商，也能把独立正态缩放旋转成相关正态。PCA解释的是方差，不能自动推出预测能力或“剩下的全是噪声”。

**第三条：建模→可行域→一阶条件→充分性→边界。** 一阶导为零只是候选；凸/凹性、单峰性、可行域和端点决定是否为全局解。整数问题要比较可行整数，不机械四舍五入。动态决策则把一次优化扩成Bellman递推，并给终端条件；Kelly与信息价值都先写清到底最大化什么。

## 核心知识与容易失分的条件

| 知识块 | 必须会解释 | 常见失误 |
|---|---|---|
| 秩一与结构矩阵 | A=uvᵀ只把向量送到u方向；vᵀu决定可能的非零特征值；J/n是投影 | 非对称秩一矩阵可非零而全谱为0；不能把秩当成非零特征值总数 |
| PSD/PD | 对称PSD等价于所有特征值非负、所有主子式非负；PD可用正首序主子式 | 非负首序主子式不够判PSD；diag(0,−1)是最小反例 |
| 相关约束 | 三变量可行区间由残差相关或Gram矩阵给出；四变量可用Schur补 | 单独把未知相关限定[−1,1]不够；只看行列式并非一般PSD判别 |
| QR与OLS | 满列秩时R回代；秩亏需识别或SVD；TSQR适于高行数 | “没有任何两列完全相关”不能排除线性依赖；形成XᵀX会平方条件数 |
| 高斯生成 | 任意AAᵀ=Σ都给X=μ+AZ；奇异Σ仍可用谱分解 | 边际正态不保证联合正态；有实质负特征值不能默默裁剪 |
| 数值求根 | 二分保持夹逼；割线用最近两点；Newton是局部二次 | 小步差不是绝对误差证书；有导数下界m时残差/m才给可用上界 |
| 变量幂、积分、ODE | 变量同时在底和指数时先取对数；原函数求导检查；ODE代回与初值检查 | 定义域、积分常数、零解、奇点、复根衰减因子漏掉 |
| 凹收益与约束 | Kelly的部署资金收益是±.01f；报价收益=成交概率×每笔利润 | ±f和±.01f混淆；%与bp差100倍；隐含的一阶解未检查边界 |
| 稀疏优化 | L0是计数；一般支持选择难；L1为常用凸替代 | “没有梯度所以所有坐标法不能用”错误；凸包络需要说明有界定义域 |
| DP与信息价值 | 状态含所需信息；终端清算；观察后再做最优选择再平均 | 忘终端持仓价值；把一次采样的即时收益与信息价值混算；一步收益不是一般最优停止证明 |

## 严格检查后补充或纠正的结论

1. **四变量相关页**重复了“非负首序主子式足够PSD”的错误；正确答案仍为[−1/3,1]。r=1仅让a与d标准化后相同，其余相关仍1/2，不会使四个变量全相同。
2. **Kelly页**算出的0.0007500对数增长=0.07500%=7.5000bp，文中0.75bp差10倍。
3. **流式OLS页**的累计公式代数正确，不能据此保证病态正规方程准确；补充直接QR/TSQR和秩条件。
4. **L0页**的“没有算法能避免指数爆炸”“坐标下降不能使用”过强；一般问题困难，但有特殊可解情形、混合整数法与硬阈值启发式。L1凸包络说法需指定有界域。
5. **tick改善页**应比较floor与ceil的可行候选及0；一tick严格改善的精确条件是e^λ(s−τ)>s，等号保留并列。
6. **Poisson需求页**先检查λ0≥−lnv；否则无可行非负价格。只有一套公寓时收入容量上限会改变模型，pQ和p·1{Q≥1}不能混用。
7. **tender报价页**问显式解却只给隐式方程；本笔记补充主分支Lambert W公式。价值与接受事件独立时，不能再把模型解读成真实成交条件逆向选择。
8. **Newton停止页**步长阈值只是局部代理，不是无条件误差保证；补充已知根区间上的导数下界残差证书。
9. **平方零矩阵页**需用A²=0的路径约束；仅秩界不足。它与一般幂零矩阵是不同问题，答案分别为floor(n²/4)与n(n−1)/2。
10. **清零掷骰页**n=15时停下与再掷一次后停同值；“从15开始每次严格负收益”不准。阈值15仍是一条最优策略。

## 与付费标题的公开同类题映射

以下付费/未标免费标题只从公开专题目录读取元数据，**没有读取其私有题干或解答**。右侧是已读公开原题或书中对应方法；构成可练习的公开替代，不保证参数与原题逐字等同。

| 公开目录中的题族/标题 | 可用的公开练习与方法 |
|---|---|
| Shifting Eigenvalues；All-Ones Matrix Plus Identity；Eigenvalues of an Equicorrelated Matrix | QV-F0214、F0339、F0444；拆为aI+b11ᵀ，沿1与其正交补分解 |
| Testing Positive Definiteness；Correlation Matrices Are PSD；Equal Pairwise Correlation | F0301、F0320；二次型、Gram表示、所有主子式、Schur补 |
| QR via Householder；Factor Neutralization；Industry-Neutralized Signal | F0313、F0319；投影残差、稳定QR、秩识别 |
| PCA Variance with Additional Feature；PCA Risk Model；Yield Curve PCA | F0283、F0371；Rayleigh商、解释方差与损失，额外模型要分别核查 |
| Fixing a Nearly-PSD Covariance；High-Dimensional Covariance Inversion | F0349、F0319；谱截断的模型改变量与正规方程条件数；不能把修正后矩阵当原矩阵 |
| Minimum Variance Portfolio；Optimal Hedge Ratio；Mean-Variance via Linear Algebra | 书pp94、163–164及F0371/F0437；协方差二次型、仿射约束、Lagrange |
| KKT Conditions for Quadratic Programs；Relaxing Infeasible Constraints | F0437作为等式约束基础；进一步区分不等式、互补松弛和可行性 |
| Kelly with Risk-Free Rate；Drawdown Constraints；Transaction Costs | F0061作为基本凹对数增长练习；新约束应重新建模，不能简单裁剪所有变体 |
| Optimal Spread with Adverse Selection；Inventory-Averse Quoting | F0345、F0346提供成交率×利润骨架；条件价值、库存动态与成本是新增变量 |
| Bayesian One-Step Lookahead Bandit；Posterior Kelly | F0356；Beta更新→后验行动→采样前期望，后验信息与实际交易收益分别建模 |
| Egg Drop Problem；Minimum Cost Path；Step Function Fitting with DP | F0124、F0386、F0457；阶段、状态、动作、边界与Bellman，而非只记答案 |

公开专题索引：[线性代数](https://quantvault.org/linear-algebra-interview-questions.html)、[优化](https://quantvault.org/optimization-interview-questions.html)。已读书中对照的公开导航：[Green Book guide](https://quantvault.org/green-book-solutions.html)。其中“176”按网页拆分的小问口径，不能与绿皮书127个独立命名题组直接比较。

## 39条逐项覆盖

表中“原站完整”表示实际读到该链接的完整题干和Worked Solution。全部独立推导、答案、检查、条件与书页映射见JSON。

| ID | 原目录题名 | 来源层级 | 方法 |
|---|---|---|---|
| QV-F0041 | [Bridge and Lantern Crossing Optimization](https://quantvault.org/problem-69-bridge-and-lantern-crossing-optimization.html) | 原站完整 | 桥灯调度与贪心 |
| QV-F0061 | [Optimal Kelly Bet Sizing for a Mean-Reversion Signal](https://quantvault.org/problem-117-optimal-kelly-bet-sizing-for-a-mean-reversion-signal.html) | 原站完整 | 受约束Kelly增长 |
| QV-F0124 | [Two Eggs, d Drops: Maximum Floors](https://quantvault.org/problem-317-two-eggs-d-drops-maximum-floors.html) | 原站完整 | 两球最坏探测 |
| QV-F0214 | [Eigenvalues of a Rank-1 Matrix](https://quantvault.org/problem-713-eigenvalues-of-a-rank-1-matrix.html) | 原站完整 | 秩一谱结构 |
| QV-F0283 | [Eigenvalue Interpretation in PCA](https://quantvault.org/problem-1265-eigenvalue-interpretation-in-pca.html) | 原站完整 | PCA方差解释 |
| QV-F0289 | [Newton's Method for Square Roots](https://quantvault.org/problem-1293-newton-s-method-for-square-roots.html) | 原站完整 | 平方根Newton迭代 |
| QV-F0301 | [Feasible Range of Third Pairwise Correlation](https://quantvault.org/problem-1401-feasible-range-of-third-pairwise-correlation.html) | 原站完整 | 三变量相关可行区间 |
| QV-F0303 | [Mean as the Minimizer of Squared Loss](https://quantvault.org/problem-1437-mean-as-the-minimizer-of-squared-loss.html) | 原站完整 | 损失函数决定位置统计量 |
| QV-F0313 | [Vector Projection and Gram-Schmidt Orthogonalization](https://quantvault.org/problem-1510-vector-projection-and-gram-schmidt-orthogonalization.html) | 原站完整 | 投影、正交化与QR |
| QV-F0319 | [Computing OLS When the Design Matrix Is Too Large for Memory](https://quantvault.org/problem-1543-computing-ols-when-the-design-matrix-is-too-large-for-memory.html) | 原站完整 | 流式OLS与数值稳定 |
| QV-F0320 | [Correlation Range with Four Variables](https://quantvault.org/problem-1548-correlation-range-with-four-variables.html) | 原站完整 | 四变量相关与Schur补 |
| QV-F0339 | [Eigenvalues of the All-Ones Matrix](https://quantvault.org/problem-1733-eigenvalues-of-the-all-ones-matrix.html) | 原站完整 | 全1矩阵的谱 |
| QV-F0345 | [Optimal Tender Price for a Block Trade](https://quantvault.org/problem-1779-optimal-tender-price-for-a-block-trade.html) | 原站完整 | 成交率乘收益的报价优化 |
| QV-F0346 | [Optimal Tick Improvement for a Market Maker](https://quantvault.org/problem-1780-optimal-tick-improvement-for-a-market-maker.html) | 原站完整 | 离散报价最优化 |
| QV-F0349 | [Sampling Multivariate Normals via Spectral Decomposition](https://quantvault.org/problem-1804-sampling-multivariate-normals-via-spectral-decomposition.html) | 原站完整 | 谱分解高斯模拟 |
| QV-F0356 | [Knowledge Gradient for Two Bernoulli Arms](https://quantvault.org/problem-1858-knowledge-gradient-for-two-bernoulli-arms.html) | 原站完整 | 单步Bayes信息价值 |
| QV-F0371 | [Maximizing a Quadratic Form](https://quantvault.org/problem-2007-maximizing-a-quadratic-form.html) | 原站完整 | Rayleigh商与二次型 |
| QV-F0372 | [Maximum Ones in a Nilpotent Binary Matrix](https://quantvault.org/problem-2010-maximum-ones-in-a-nilpotent-binary-matrix.html) | 原站完整 | 平方零0/1矩阵的极值 |
| QV-F0373 | [Minimum of x^x on (0, 1]](https://quantvault.org/problem-2016-minimum-of-x-x-on-0-1.html) | 原站完整 | 变量底数和指数的极值 |
| QV-F0376 | [Numerical Function Minimization via Gradient Descent](https://quantvault.org/problem-2029-numerical-function-minimization-via-gradient-descent.html) | 原站完整 | 数值梯度下降 |
| QV-F0378 | [Problems With L0 Regularization](https://quantvault.org/problem-2050-problems-with-l0-regularization.html) | 原站完整 | 稀疏选择与非凸优化 |
| QV-F0386 | [MDP Formulation for Stock Trading](https://quantvault.org/problem-2151-mdp-formulation-for-stock-trading.html) | 原站完整 | 交易决策MDP |
| QV-F0388 | [Revenue Optimization with Poisson Demand](https://quantvault.org/problem-2172-revenue-optimization-with-poisson-demand.html) | 原站完整 | 价格需求与可行性 |
| QV-F0393 | [Newton's Method: Quadratic Convergence Proof and Stopping Rule](https://quantvault.org/problem-2206-newton-s-method-quadratic-convergence-proof-and-stopping-rul.html) | 原站完整 | Newton局部二次与误差认证 |
| QV-F0427 | [Differentiating (ln x) to the Power ln x](https://quantvault.org/problem-3630-differentiating-ln-x-to-the-power-ln-x.html) | 原站完整 | 对数求导 |
| QV-F0428 | [Two Limits by L'Hospital: e^x / x^2 and x^2 ln x](https://quantvault.org/problem-3632-two-limits-by-l-hospital-e-x-x-2-and-x-2-ln-x.html) | 原站完整 | 洛必达与增长阶 |
| QV-F0429 | [The Antiderivative of ln x](https://quantvault.org/problem-3633-the-antiderivative-of-ln-x.html) | 原站完整 | 分部积分 |
| QV-F0430 | [Integrating sec x from 0 to pi/6](https://quantvault.org/problem-3634-integrating-sec-x-from-0-to-pi-6.html) | 原站完整 | 三角函数对数导数 |
| QV-F0435 | [Bernoulli's Inequality via Taylor's Theorem](https://quantvault.org/problem-3640-bernoulli-s-inequality-via-taylor-s-theorem.html) | 原站完整 | 凸性与Bernoulli不等式 |
| QV-F0436 | [Bisection vs Secant: Counting Steps to a Root](https://quantvault.org/problem-3642-bisection-vs-secant-counting-steps-to-a-root.html) | 原站完整 | 无导数求根比较 |
| QV-F0437 | [Distance From the Origin to the Plane 2x + 3y + 4z = 12](https://quantvault.org/problem-3643-distance-from-the-origin-to-the-plane-2x-3y-4z-12.html) | 原站完整 | 仿射约束最小范数 |
| QV-F0438 | [Separable ODE: y' + 6xy = 0 with y(0) = 1](https://quantvault.org/problem-3644-separable-ode-y-6xy-0-with-y-0-1.html) | 原站完整 | 可分离ODE |
| QV-F0439 | [Solving y' = (x - y)/(x + y) by Substitution](https://quantvault.org/problem-3645-solving-y-x-y-x-y-by-substitution.html) | 原站完整 | 变换为可分离ODE |
| QV-F0440 | [First-Order Linear ODE: y' + y/x = 1/x^2 with y(1) = 1](https://quantvault.org/problem-3646-first-order-linear-ode-y-y-x-1-x-2-with-y-1-1.html) | 原站完整 | 积分因子ODE |
| QV-F0441 | [General Solution of y'' + y' + y = 0](https://quantvault.org/problem-3647-general-solution-of-y-y-y-0.html) | 原站完整 | 常系数齐次ODE |
| QV-F0442 | [Nonhomogeneous ODEs: y'' + y' + y = 1 and y'' + y' + y = x](https://quantvault.org/problem-3648-nonhomogeneous-odes-y-y-y-1-and-y-y-y-x.html) | 原站完整 | 非齐次ODE |
| QV-F0444 | [Eigenvalues and Eigenvectors of the Matrix [[2, 1], [1, 2]]](https://quantvault.org/problem-3651-eigenvalues-and-eigenvectors-of-the-matrix-2-1-1-2.html) | 原站完整 | 二阶对称谱分解 |
| QV-F0445 | [Generating Correlated Normals From Independent Ones](https://quantvault.org/problem-3653-generating-correlated-normals-from-independent-ones.html) | 原站完整 | Cholesky相关高斯 |
| QV-F0457 | [Roll Until You Stop or Hit a 6: Optimal Strategy and Fair Price](https://quantvault.org/problem-3673-roll-until-you-stop-or-hit-a-6-optimal-strategy-and-fair-pri.html) | 原站完整 | 累积收益最优停止 |

F0372完整原题的条件是**A²=0**，最大1的数量为floor(n²/4)，由无长度2路径及平衡二分块构造证明；不能与一般幂零矩阵的n(n−1)/2极值混淆。来源主证明正确，但末尾“仅由秩即可最大化1数量”的直觉不充分，已在复核说明中标出。
