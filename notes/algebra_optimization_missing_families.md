> 当前总复习排期以 [WEEK_PLAN.md](../WEEK_PLAN.md) 为准；本讲义内的领域日程只作为补充建议。

# 全量线代/优化目录：新增方法补充

已逐条检查`site-live-catalog.json`中**75条Linear Algebra和144条Optimization，共219个live ID**，全部映射到36个学习方法族。`algebra_optimization_live_family_map.json`包含每个ID的题名、知识点、公开练习或一手/官方资料链接及来源层级；`algebra_optimization_live_family_summary.json`包含方法族和计数。

其中**39条原站公开完整解答已读并复核，180条仅做元数据到方法族的路由**。后者不等于已知原题的参数、约束或官方答案。下面例子是明确声明条件的原创复习例，帮助补充原39条笔记的盲区；不冒充那些私有题的解答。

## 1. 结构谱与等相关矩阵

对n≥2，等相关矩阵R=(1−ρ)I+ρ11ᵀ，公共方向1的特征值是1+(n−1)ρ，正交补方向是1−ρ。因此PSD要求−1/(n−1)≤ρ≤1；可逆时可在这两个子空间分别取倒数。不要逐项展开n阶行列式。

另一常见模板是实对称三对角Toeplitz：对角a、相邻b。尝试正弦向量v_j=sin(jθ)，边界v_0=v_(n+1)=0给θ=kπ/(n+1)，从而得到特征值a+2b cosθ。这是“猜不变方向并代回”的例子。

公开方法：[MIT SVD习题与解答](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/positive-definite-matrices-and-applications/singular-value-decomposition/)、[SymPy矩阵官方参考](https://docs.sympy.org/latest/modules/matrices/matrices.html)。

## 2. 协方差矩阵的乘积

A、B均PSD不代表AB对称，也不代表xᵀABx总非负。例A=diag(1,0)、B=[[1,2],[2,5]]给AB=[[1,2],[0,0]]；取x=(1,−1)，二次型为−1。若A正定，AB与A^(1/2)BA^(1/2)相似，因此其谱非负。**谱、对称性、二次型是三件不同的事。**

公开方法：[SciPy Schur分解](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.schur.html)、[Higham的相关矩阵说明](https://nhigham.com/correlation-matrices/)。

## 3. Jordan、幂零与矩阵多项式

幂零指数由最大Jordan块决定；A^k=0表示每个块大小至多k，秩等于n减Jordan块数。由此可讨论给定指数上界时的最大秩，但“指数恰为k”和“至多k”须区分。

两种0/1问题尤其不能混淆：一般实数域幂零0/1矩阵对应DAG，可有n(n−1)/2条边；**实际已读F0372要求A²=0**，不允许任何长度2路径，最大只有floor(n²/4)个1。其公开原页为[平方零矩阵题](https://quantvault.org/problem-2010-maximum-ones-in-a-nilpotent-binary-matrix.html)。

对矩阵多项式，先说明数域与结构。例如**如果A实对称**且A⁵+A³+A=3I，实特征值必须解z⁵+z³+z=3；该标量函数严格递增，唯一实根1，所以A=I。删除实对称条件后，复根和实非对称伴随矩阵给出其他可能，不能沿用结论。

公开方法：[SymPy Jordan、幂零与对角化](https://docs.sympy.org/latest/modules/matrices/matrices.html)。

## 4. 交换子、矩阵函数与随机矩阵

与所有方阵交换的方阵只能是cI：先与各E_ii交换迫使其为对角矩阵，再与E_ij交换迫使对角元素相同。只与某个简单谱矩阵交换时，可在其特征基逐方向分析；有重根时块内自由度不同。

矩阵指数满足tr(expA)=Σexp(λ_i)，即使A不可对角化也可由三角/Schur形式理解；通常不等于exp(trA)。行列和均1给左右特征向量1，但要有**非负性**才可直接调用随机矩阵谱界。[[2,−1],[−1,2]]的行列和均1，却有特征值3。

公开方法：[SciPy Sylvester方程](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_sylvester.html)、[Schur分解](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.schur.html)、[SymPy矩阵函数](https://docs.sympy.org/latest/modules/matrices/matrices.html)。

## 5. 大规模PCA、稀疏特征对和协方差修复

稀疏矩阵不应先转稠密再完整对角化；幂迭代依赖谱间隙与初始分量，多个特征方向常用Lanczos和重正交化。流式PCA还要维护中心化信息；截断合并会引入近似误差。

估计协方差时，收缩可改善条件数；修复“几乎相关矩阵”还需保持单位对角。单次把负特征值裁0一般不保证对角仍1，更不自动是所选距离下的最近相关矩阵。

公开资料：[eigsh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigsh.html)、[IncrementalPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html)、[Ledoit–Wolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html)、[Higham原始研究](https://eprints.maths.manchester.ac.uk/232/)。

## 6. 秩亏最小范数、超平面拟合与插值

OLS残差最小可能有多个系数解；最小范数版本用SVD伪逆。拟合超平面时，垂直坐标误差的OLS与所有方向正交距离的total least squares不同；后者对中心化点云取最小奇异值方向作法向量。多项式插值需检查横坐标重复和Vandermonde秩；相同x却不同y不能由单值函数同时通过。

公开方法：[MIT SVD公开习题](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/positive-definite-matrices-and-applications/singular-value-decomposition/)。

## 7. 数值稳定不只是更小的步长

设I_n=∫₀¹xⁿeˣdx，分部积分给I_n=e−nI_(n−1)。前向误差被乘以n且发生大数相减；反向递推I_(n−1)=(e−I_n)/n可压缩尾部误差，但必须给尾项初值或误差界。这是一个已声明积分区间的复习例，不能默认等于只见标题的原题区间。

中心一阶差分的误差常为O(h²)+O(ε/h)，量级平衡h∝ε^(1/3)；中心二阶导则为O(h²)+O(ε/h²)，量级h∝ε^(1/4)。比例常数依赖导数和尺度。

二次目标f=.5xᵀHx−bᵀx、H正定时，沿负梯度g的精确线搜索步长为(gᵀg)/(gᵀHg)。固定步长需0<α<2/λ_max(H)才有通常线性收敛结论。求根、最小化、差分、递推各有不同误差来源。

公开方法：[Boyd–Vandenberghe](https://stanford.edu/~boyd/cvxbook/)、[SciPy优化教程](https://docs.scipy.org/doc/scipy/tutorial/optimize.html)。

## 8. LAD、几何中位数、KKT与熵

LAD可用u≥Ax−b、u≥−(Ax−b)将绝对值和转成LP。过原点直线的LAD在x_i≠0部分等价于对斜率y_i/x_i求权重|x_i|的加权中位数；x_i=0只贡献与斜率无关的常数。

几何中位数最小化Σw_i||x−a_i||；Weiszfeld按距离倒数加权更新，迭代撞到数据点须检查次梯度或使用修正版，不能直接除0。对一般凸约束，先查可行性、边界和最优值是否达到，再用满足资格条件的KKT。

若f≥0、∫₀¹f=1，则Jensen给∫₀¹f log f≥0，等号为f=1几乎处处；未给归一化约束的题不能直接套这个答案。

公开方法：[Vardi–Zhang原始论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC26449/)、[SciPy LP](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)、[Boyd凸优化](https://stanford.edu/~boyd/cvxbook/)。

## 9. 图优化不等于排序

线性一对一分配为min_πΣc_(i,π(i))；可用专门分配算法。汇率图用−ln汇率作边权，乘积超过1的套利环转成负环，还需计入费用、报价方向与可成交量。疏散题必须明确边/点容量、同步移动和时间，可能需要时间展开流。Top-K加相关或多样性约束往往是组合优化；简单排序或贪心只是候选，除非有可证明结构。

公开方法：[线性分配](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html)、[Bellman–Ford](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.bellman_ford_predecessor_and_distance.html)、[最小费用流](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.min_cost_flow.html)。

## 10. Bloom与二选一

标准插入型Bloom过滤器的近似误报率为(1−e^(−kn/m))^k；连续最优哈希数k≈(m/n)ln2，最终应比较相邻整数。公式依赖哈希近似和插入规则，删除不能随意清位。

在n球顺序投入n桶、每球独立随机取d≥2个候选并放最空桶的经典模型中，最大负载高概率为lnlnn/lnd+O(1)，与平均负载不同；Poisson到达队列的稳态是另一模型，不能直接照搬常数。

公开原始资料：[Broder–Mitzenmacher Bloom调查](https://www.eecs.harvard.edu/~michaelm/NEWWORK/postscripts/BloomFilterSurvey.pdf)、[二选一作者调查](https://www.eecs.harvard.edu/~michaelm/postscripts/handbook2001.pdf)。

## 11. 执行、库存、中性化与容量

一个明确的玩具清仓模型可取q_t=x_(t−1)−x_t、x_0=X、x_T=0，最小化Σηq_t²+λσ²Σx_t²。它连接库存守恒、冲击与持仓风险，并能化为三对角线性系统。随机做市HJB、成交条件逆向选择、maker/taker费用和库存惩罚则各自增加状态与条件，不能仅从标题判为同一模型。

同样，未知协方差时没有只由五个信号均值决定的通用最优权重。持有期重叠会改变协方差和有效样本量；容量还取决于冲击、成交量和费用。此类研究题的第一步是明确目标和外样本协议。

公开原始方法：[Almgren–Chriss](https://doi.org/10.21314/JOR.2001.041)、[Boyd凸优化](https://stanford.edu/~boyd/cvxbook/)、[协方差收缩](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html)。

## 使用这些路由的方法

先按JSON中的family学习一个已读公开例或官方教程，再对未读题写出“已知/未知/待确认条件”。只有实际拿到完整题干并核对推导后，才能把`metadata_family_route`升级为完整题复核。对`Burger Flipper`、`Candle Length Ratio`等无法仅由标题确定规则的条目尤其如此。
