> 当前总复习排期以 [WEEK_PLAN.md](../WEEK_PLAN.md) 为准；本讲义内的领域日程只作为补充建议。

# 绿皮书完整知识点与七日复习路线

依据 Xinfeng Zhou, *A Practical Guide to Quantitative Finance Interviews*（2008）所提供扫描本。正文七章印刷页1–191；PDF页码=印刷页码+16。正文OCR逐页读完，目录五页均已看原图核对；p104、p170为空白。以下是原创压缩讲义与题型索引，不复刻整段题干或解答。

目录有**127个独立命名的题目组**：第2章37、第4章42、第5章15、第6章18、第7章15。第3章另整理**23组未单列题名的题目摘要**，不是书中额外命名的23道题。一个题目组可能有A–E多个小问；重复的“Dice game”“Card game”等按章节分开计数。23条理论记录覆盖非题目叙述。完整190条原目录项、173条内容记录及页码见同目录的`greenbook_inventory.json`。

## 从零开始，先建立的语言

1. **代数**：分数、指数、对数、绝对值、阶乘、求和符号、等比数列、一元二次方程；会把文字约束写成等式或不等式。
2. **集合与逻辑**：且/或/非、必要与充分、互斥与完备、证明与举例的区别；样本空间必须说明“随机”如何产生。
3. **函数与图形**：输入输出、单调、凸性、斜率、面积；能画分段收益函数与二维概率区域。
4. **向量与矩阵**：维度、转置、内积、矩阵乘法；矩阵相乘次序不能交换。
5. **随机变量**：事件与数值映射不同；概率是权重，期望是加权平均，方差是平方偏差平均；条件概率必须重新归一化。
6. **编程**：数组、循环、分支、函数、递归、整数与浮点、索引边界；算法正确性与复杂度分别回答。
7. **金融**：买卖方向、单位与现金流时点、现值、贴现、收益与利润；风险中性概率用于无套利定价，并不等于现实上涨概率。

每个题型统一练习六步：①复述条件与观察机制；②列出状态、随机变量和目标；③先做小例；④选方法并说明为什么；⑤处理边界与单位；⑥给出一项独立检查。口头输出要让面试官看见这些关键决定。

## 七日安排与依赖

这是七日覆盖与查漏路线；首次接触高等数学时，先做到识别条件、写出模型和解释直觉，再逐步补完整推导。每天都保留一次不看笔记的回忆和一次口述。

| 日 | 主线与原书页码 | 当日需要形成的可检查产出 |
|---|---|---|
| 1 | 数学语言；第1章；3.1–3.5 pp33–50；2.1–2.4 pp3–17 | 能求导、换元/分部积分、写Taylor近似、分类简单ODE；能解释递归、守恒、对称与信息编码各一题 |
| 2 | 4.1–4.4 pp59–92；2.5–2.9 pp17–32 | 先选样本空间再计数；能做Bayes、几何概率、到达过程；列出常用分布支持集、参数、均值方差 |
| 3 | 3.6 pp50–58；4.5–4.6 pp92–103；6.4组合优化 pp163–164 | 从协方差推出PSD约束、回归/对冲/最小方差；能用指示变量、条件期望和极值CDF解题 |
| 4 | 第5章 pp105–136 | 画模式识别状态图；写吸收概率/时间方程；说明可选停止条件；写Bellman递推；会用Ito辨认漂移 |
| 5 | 6.1–6.3 pp137–162 | 按现金流证明parity与边界；连接复制、风险中性与PDE；解释Greeks及静态/动态对冲的局限 |
| 6 | 7.1–7.2 pp171–183；6.4其余 pp164–169 | 写清晰算法、说复杂度并测边界；解释VaR尾部问题、DV01、期货远期与四种短率模型 |
| 7 | 7.3 pp184–191；整本混合复盘 | 实现/手推MC与FD骨架，报告误差与稳定性；按错题回到对应页；完成跨主题口述而非按章节提示作答 |

依赖顺序：代数与函数→导数/积分→Taylor与多元导数→线性代数与协方差；集合/计数→条件概率→分布与期望→Markov/鞅/DP；Brownian+Ito+贴现→风险中性与BSM→Greeks/奇异期权；算法与线性代数+概率→Monte Carlo；Taylor+PDE+边界→有限差分。逆向归纳、递推、守恒、对称在整条链路反复出现。

## 第1章 General Principles（pp1–2）

五条不是背诵口号，而是操作习惯：基础知识面、事先练习、主动倾听、口述思路、声明合理假设。常错是直接套熟题答案、默算、跳过随机机制、把面试官提供的约束当成无关文字。每次练习最后补一句：“这个结论依赖哪些条件？”

## 第2章 Brain Teasers（pp3–32）：九种方法

| 方法与页码 | 最低先修与核心知识 | 易错点 |
|---|---|---|
| 2.1 Problem Simplification pp3–5 | 有限状态、递推；从1、2、3个参与者反推一般情况 | 忽略生存/收益/平局偏好或投票阈值；把观察到的模式当成证明 |
| 2.2 Logic Reasoning pp5–10 | 约束满足、公共知识、守恒、决策树、素因子、偏序、固定点 | 不区分“一直不知道”和“现在知道”；称重只有左右两结果的误解；指数塔候选未检验收敛 |
| 2.3 Thinking Out of the Box pp10–15 | 染色、编码、协议、奇偶、额外物理观测量、掩码求和 | 体积够就认为可装；擅自禁用旋转/多锁；用概率替代保证 |
| 2.4 Application of Symmetry pp15–17 | 相同角色采取相同策略，必要时指定一个例外角色 | 只看表面相同而不证明可交换；随机反复访问不能重复计一次性信号 |
| 2.5 Series Summation pp17–20 | 等差和、平方和、未知数恢复、加权编码、最坏情况预算 | 忽略圆周邻接；两球问题误用二分查找；平均次数与最坏次数混淆 |
| 2.6 The Pigeon Hole Principle pp20–23 | 数量大于可区分类别时必有碰撞；几何分割与三进制编码 | 抽屉数量选错；只证明不够而未给可行构造；度数范围不可能同时含0和n−1 |
| 2.7 Modular Arithmetic pp23–27 | 同余、模k校验、模3不变量 | 混淆颜色标签与余数；只跟踪绝对数量而忽略差的余数 |
| 2.8 Math Induction pp27–31 | 明确命题、基例、归纳假设、归纳步；强归纳；前缀最低点 | 用待证明命题本身作理由；未说明如何把n+1情形缩成n情形 |
| 2.9 Proof by Contradiction pp31–32 | 假设否命题，推出与已知约束矛盾；最简分数；余数覆盖 | “没找到解”不是反证；同时猜帽与能听见前人回答的协议不同 |

跨题迁移：pirates→DP；gas track→前缀和算法；coin weights→信息编码；hats→校验码；pigeonhole→比较下界。37个题组详见末尾完整目录。

## 第3章 Calculus and Linear Algebra（pp33–58）

**3.1 Limits and Derivatives（pp33–36）**：导数定义；乘积、商、链式、幂、指数对数和三角函数；对数求导；导数符号与局部极值；二阶检验；洛必达法则。先修是函数与极限直觉。易错：导数为零不保证极值、边界极值漏查、未先确认0/0或∞/∞就用洛必达。

**3.2 Integration（pp36–40）**：微积分基本定理；换元、分部；用截面积算体积、速度算距离、密度算期望。先画区域或写量纲，再决定被积函数。标准正态的正半轴条件均值在书p40有实质错误，正确值为√(2/π)，见勘误。易错：积分上下限未随换元改变；忘积分常数；条件密度未归一化。

**3.3 Partial Derivatives and Multiple Integrals（pp40–41）**：偏导、混合二阶导、多元链式；极坐标Jacobian为r；把高斯积分的平方写成二维积分。易错是漏Jacobian或把积分区域错误地当成矩形。

**3.4 Important Calculus Methods（pp41–46）**：Taylor有限展开与余项界；Euler公式和复对数分支；Bernoulli不等式；Newton、二分、割线；Lagrange乘子。Newton的二次收敛是局部且需简单根等条件。二分要有连续与异号区间；驻点候选还须核对可行性和最优性。i^i需区分主值和多值；不等式在x=0必须保留等号。

**3.5 ODE（pp46–50）**：可分离；变量替换；一阶线性积分因子；二阶常系数特征根三种情形；非齐次解=齐次通解+一个特解。先识别方程类型再求解，最后代回方程和初值。特解试探与齐次解重合时需乘x等修正，不能机械照抄次数。

**3.6 Linear Algebra（pp50–58）**：向量、内积、范数、角与正交；QR；最小二乘与正规方程、矩阵求导、回归条件；行列式与迹；特征值/向量、对角化、矩阵幂；对称矩阵、PSD/PD；LU、Cholesky；SVD、相关正态模拟。关键迁移是把协方差看成二次型、把随机变量的相关看成中心化标准化后的L2内积。易错：只排除两两共线不能保证满秩；回归不宜显式求逆；QR宜直接作用于设计矩阵X；PSD要检查所有主子式而非仅首序主子式；Cholesky的L或R方向要与生成公式一致。

## 第4章 Probability Theory（pp59–103）

**4.1 Basic Definitions and Set Operations（pp59–64）**：事件、随机变量、并交补、互斥与可加性、指示变量。coin/card/passenger题的共同技巧是找到可交换标签并单独处理平局或两个特殊状态。圆周题将“存在某半圆”拆成由某点开始的弧事件，边界重合在连续模型下概率为零。易错：互斥不等于独立；可能结果未必等概率。

**4.2 Combinatorial Analysis（pp64–72）**：乘法计数；排列、重复排列、组合；二项式定理；容斥；Fibonacci递推；门限访问结构；淘汰树；错排；生日碰撞；代数共轭与模100计数。先说清对象是否带标签、顺序是否计入、是否放回。易错：两对牌型重复计数；容斥符号错误；生日题忽略补集；对锁钥匙方案只给上界未说明下界。

**4.3 Conditional Probability and Bayes（pp72–86）**：条件归一化、乘法法则、全概率、独立、Bayes；观察机制；无偏比特提取；交换性与排名；离散最大值；主持人信息；分枝灭绝固定点；随机排列最后出现；模式递归；无放回；吸收财富；强化过程；到达概率。易错：Boys and girls忽略看到孩子的选择机制；Monty忽略主持人协议；灭绝取了错误固定点；Cars只凭恒定率就假设区间独立。

**4.4 Distributions（pp86–92）**：CDF/PMF/PDF、支持集、期望方差；离散均匀、二项、Poisson、几何、负二项；连续均匀、正态、指数、Gamma、Beta；几何概率；指数无记忆；Poisson计数与到达；长度偏差/inspection paradox；MGF与正态矩。要特别说明几何/负二项是计“试验次数”还是“失败次数”，Gamma采用rate还是scale。Poisson随机时刻的前后等待各平均10不与到达间隔均值10矛盾，因为抽到的间隔是长度加权的。

**4.5 Expectation, Variance, Covariance（pp92–99）**：期望线性不需独立；独立时乘积期望分解；协方差双线性、方差展开；不相关≠独立；条件期望与全期望；指示变量；更新递推；几何等待分阶段；均匀和的单纯形；Bernoulli联合界。最优对冲要区别回报权重、美元敞口和股数。Joint default中相关系数可行区间由边际概率限制，不能先设±1。

**4.6 Order Statistics（pp99–103）**：最大值CDF为F(x)^n；最小值生存函数为[1−F(x)]^n；求导得到密度，再积分求矩；两样本min/max的联合区域与相关；碰撞交换标签的蚂蚁耦合。易错：求最小值时忘补集；混淆极值和平均值；替换标签只消除相互作用，不表示单只被指定标签的轨迹不变。

## 第5章 Stochastic Process and Stochastic Calculus（pp105–136）

**5.1 Markov Chain（pp105–115）**：齐次性、转移矩阵/图、路径概率、可达互通、暂态常返与吸收；吸收概率a=Pa加边界，吸收时间m=1+Pm加边界。真正难处是状态要保留决定未来所需的最短后缀。coin triplets含等待、竞赛、自由选序列三个层次；较短平均等待不自动意味着对所有对手更高胜率。Color balls的转移概率是以最终某色胜出为条件，不能用未条件化的原转移代替。

**5.2 Martingale and Random walk（pp115–121）**：IID增量、对称游走、信息流与条件均值；S_n、S_n²−n；停止时刻“不能看未来”；Wald；双边退出；反射原理与Catalan；一般模式的前后缀重叠。鞅不是Markov的同义词；均值恒定也不够。用E[M_T]=E[M_0]前检查可选停止条件，单侧首次命中虽几乎必然也可能平均无限。

**5.3 DP（pp121–128）**：阶段、状态、行动、扰动、加法收益、终端边界、最优性原则、Bellman倒推。有限掷骰是剩余机会的阈值；World series是给定终端收益的复制；dynamic dice是累积金额与归零风险；dynamic card是红黑剩余数与停止价值。把“继续一期后立刻停”的收益和完整继续价值分清，阈值必须以Bellman方程验证。策略和初始价值均需给出。

**5.4 Brownian/Ito（pp129–136）**：连续路径、W0=0、独立平稳正态增量；Var(Wt)=t、Cov(Ws,Wt)=min(s,t)；二次与指数鞅；不相关但依赖；双边和单边首达、反射、命中概率与漂移；Ito二阶项；时间依赖变换和多项式鞅判断。易错：dW²=dt的二阶项漏掉；零无条件均值当成鞅；“无漂移”在一般情形只先得到局部鞅；极限边界和无限期停止直接代入而未检验。

## 第6章 Finance（pp137–169）

**6.1 Option Pricing（pp137–149）**：现值、股息、欧式/美式；收益与比较静态；parity、上下界、合成远期；提前行权与凸性；delta复制、自融资、BSM PDE；风险中性、lognormal终值、d1/d2；热方程转换；首达支付和逆股票合约。先画现金流再列公式；d2的正态CDF是定价测度下到期实值概率，delta不是同一概率。无股息美式看涨的通常结论需非负利率等条件；换测度不是把现实世界漂移随意替换。

**6.2 Greeks（pp149–158）**：delta、gamma、theta、vega、rho；ATM短期近似；临近到期的delta阶跃与gamma集中；融资腿、动态再平衡；gamma与theta的局部平衡；隐含波动率与smile/skew；volga与σ方向凸性；Breeden–Litzenberger式执行价二阶导。易错：求delta把d1/d2当常数；t和τ的theta符号混淆；volatility上涨获利说成无条件套利；“价格对σ总是凸”错误；从σ的随机抽样价格比较泛化为任意随机波动率过程。

**6.3 Portfolios and Exotics（pp158–162）**：背景策略covered call、protective put、bull/bear spread、butterfly；完整展开bull spread、straddle、digital、exchange。策略先用到期分段收益检查；straddle持仓的delta会变，不能将其当成纯波动率互换。digital不连续收益造成近到期对冲敏感；窄价差复制需要密集执行价和较大头寸。exchange换numeraire必须伴随换测度，有效波动率σ_eff²=σ1²+σ2²−2ρσ1σ2。

**6.4 Other Finance（pp163–169）**：wᵀμ、wᵀΣw、权重/目标收益约束；VaR分位数、尾部严重性、非次可加与压力测试；债券modified duration、convexity、美元久期、DV01；逆浮息债现金流复制；期货逐日盯市与随机利率相关；短率模型与HJM；Vasicek/CIR/Ho-Lee/Hull-White。久期不是债券到期年数；净值为零的swap宜用美元敏感度；CIR非负不代表无条件严格正；2008年教材中“负利率不理想”的市场评价不当作普遍事实。

## 第7章 Algorithms and Numerical Methods（pp171–191）

**7.1 Algorithms（pp171–182）**：O/Ω/Θ、最坏/平均、Master theorem；交换、有序去重、Horner、滑动平均；插入/归并/快排；Fisher–Yates、随机键排序、reservoir；成对min/max、指数扩张+二分、阶梯矩阵搜索；Fibonacci迭代与矩阵快速幂；前缀最小值/最大连续子数组。先说明输入、返回值、空输入、全负数、重复值、索引与整型溢出。源书C++不能未经测试直接搬入现代代码；最优值与区间索引需各自维护。快速幂O(log n)按固定成本矩阵运算计，大整数位复杂度另算。

**7.2 The Power of Two（pp182–183）**：二进制、位与/XOR/移位、2幂判断、乘7、用公平比特生成任意Bernoulli(p)、一轮并行二进制群测。x&(x−1)=0要加x>0；浮点p只是目标概率近似；移位可能溢出；同时编码与自适应二分不可混为一谈。

**7.3 Numerical Methods（pp184–191）**：MC基于大数定律；风险中性GBM精确离散；终值收益可直接模拟终点，路径依赖需路径；随机数逆变换/拒绝；反变量、矩匹配、控制变量、重要性抽样、低差异序列；共用随机数的bump Greeks；面积估π；FD网格、终端/空间边界、显式/隐式/CN、稳定性。MC标准误差为σ/√M，不能把它写成方差；正态拒绝生成器必须能输出负数；重要性采样必须覆盖目标支持且检查加权方差。标准BSM是线性PDE；热方程u_t=κu_xx显式法需κΔt/Δx²≤1/2；时间步更细与空间步更细的稳定性作用不同。稳定不等于足够准确；提前行权问题还需最优停止处理。

## 已核查的勘误与教学条件

- **p40，原图确认**：书把半轴一阶矩1/√(2π)当成条件均值。条件均值还需除以P(X>0)=1/2，因此为√(2/π)。
- **p56，原图确认**：PSD的判别不能只看非负首序主子式。反例diag(0,−1)的首序行列式均为0，仍不是PSD；需所有主子式非负。PD使用首序主子式严格正。
- **p186，原图确认**：指数提议只支持正数；按书中半正态比例拒绝后还须独立随机符号，才得到标准正态。印刷密度与比例前因子也不一致。
- **p186，原图确认**：独立同分布抽样平均的方差是σ²/M，标准误差是σ/√M；不能混写。
- **p53，数值与秩条件**：不存在两两完美相关不足以保证设计矩阵满列秩；QR宜作用于X，SVD可识别秩亏；不要把求逆当默认回归实现。
- **pp85–86，假设补全**：汽车到达的四段无车概率相乘需要独立区间等额外条件；恒定边际率本身不够。
- **p94，单位补全**：用回报波动率时，给定一股A，B的股数对冲须乘S_A/S_B；简单ρσ_A/σ_B是相对回报权重。
- **pp116等，停止条件**：停下的过程与终端均值恒等式分开核查；Wald、可选停止、无穷边界都需相应条件。
- **p143，贴现补全**：定价测度下是贴现价值过程具有鞅性质。
- **p169，边界条件**：CIR通常保证非负；正初值时严格正需要Feller条件2ab≥σ²。
- **p117，算术核查**：书印1441步；按该页公式17×83应为1411步。
- **p182，输入边界**：2幂判断需x>0。
- **pp189–191，术语与系数**：标准BSM PDE是线性的；显式法稳定系数包含扩散常数κ。

这些是对来源的独立核查与教学补全，不意味着已对全书所有印刷公式逐字校勘。完整机器可读的16条错误/条件说明已附在JSON的`corrections_and_cautions`。

## 完整题组索引与全部原目录

下面自动从已核查目录与内容记录生成。命名题组标题保留为短检索标签；“原创摘要”是无独立题名的第3章题型。所有页码均为印刷页。

### 第1章题组

本章是面试方法原则，没有独立题组。

### 第2章题组

| 章节 | 题名或原创摘要 | 印刷页 | 迁移方法与知识点 |
|---|---|---|---|
| 2.1 | Screwy pirates | 3–4 | 从小规模反推；生存、收益、偏好的字典序；投票阈值与最低补偿 |
| 2.1 | Tiger and sheep | 4–5 | 从1、2、3只建立递推；理性行为与奇偶不变量 |
| 2.2 | River crossing | 5 | 慢者共同过桥；手电往返资源；总时间与最坏耗时 |
| 2.2 | Birthday problem | 5–6 | 把不知道转成候选集合约束；逐轮更新信息集 |
| 2.2 | Card game | 6–7 | 红黑总量守恒；配对删除保持数量差 |
| 2.2 | Burning ropes | 7 | 燃烧速度不均匀；双端点火将剩余燃烧时间减半 |
| 2.2 | Defective ball | 7–9 | 三值称重结果；同时区分球编号与轻重；用正常球作基准 |
| 2.2 | Trailing zeros | 9 | 阶乘中的5的幂次；计入25、125等重复因子 |
| 2.2 | Horse race | 9–10 | 分组排名；跨组比较；排除不可能的前三名 |
| 2.2 | Infinite sequence | 10 | 指数塔的固定点；代数候选与收敛条件区别 |
| 2.3 | Box packing | 10–11 | 二维棋盘拓展到三维；体积条件不是充分条件；颜色资源上界 |
| 2.3 | Calendar cubes | 11–12 | 重复数字约束；0、1、2的必要重复；6/9旋转共用 |
| 2.3 | Door to offer | 12–13 | 真假守卫的复合问句；逐情景检验回答策略 |
| 2.3 | Message delivery | 13 | 双锁三次传递；钥匙与文档分离；通信约束下的状态演化 |
| 2.3 | Last ball | 13–14 | 红球数模2保持；总球数严格下降 |
| 2.3 | Light switches | 14 | 亮灭与余热组合编码；区分操作次数和进屋次数 |
| 2.3 | Quant salary | 15 | 随机掩码与抵消；聚合量与个体信息区分 |
| 2.4 | Coin piles | 15–16 | 选定与正面数相同数量的硬币；整体翻转把未知量抵消 |
| 2.4 | Mislabeled bags | 16 | 全部标签错误是关键约束；从混合标签取样 |
| 2.4 | Wise men | 17 | 指定计数者打破对称；一次性信号与重复访问；随机访问的公平性 |
| 2.5 | Clock pieces | 18 | 等差求和；圆周邻接；核查分块形状限制 |
| 2.5 | Missing integers | 18–19 | 总和与平方和恢复两个未知整数；线性扫描复杂度 |
| 2.5 | Counterfeit coins I | 19 | 每袋取不同数量；测重偏差编码袋号与轻重 |
| 2.5 | Glass balls | 19–20 | 两球探测；递减楼层间距；N(N+1)/2覆盖范围 |
| 2.6 | Matching socks | 21 | 颜色作抽屉；保证条件与概率条件区分 |
| 2.6 | Handshakes | 21 | 人数与可能度数；握手次数的可行范围 |
| 2.6 | Have we met before? | 21–22 | 六人二色完全图；先固定一人再用三人子集 |
| 2.6 | Ants on a square | 22 | 分成25格；格子对角线与圆直径比较 |
| 2.6 | Counterfeit coins II | 22–23 | 每袋三种重量；1、3、9等权重；唯一解码与抽屉下界 |
| 2.7 | Prisoner problem | 24–25 | 二色奇偶校验；多色模k求和；一个人传递全局余数 |
| 2.7 | Division by 9 | 25 | 10模9等于1；数位和判别；模11交错和扩展 |
| 2.7 | Chameleon colors | 26–27 | 两颜色数量差模3保持；不可能状态证明 |
| 2.8 | Coin split problem | 27–28 | 拆分递推；无序对计数；与拆分路径无关 |
| 2.8 | Chocolate bar problem | 28–29 | 每次仅增加一块；初末块数决定操作次数 |
| 2.8 | Race track | 29–31 | 合并可达相邻补给站；从累计净油量最低点起步 |
| 2.9 | Irrational number | 31 | 最简分数；平方的奇偶性；共同因子矛盾 |
| 2.9 | Rainbow hats | 31–32 | 各人负责一个总余数；同时猜测与顺序通信区分 |

### 第3章题组

| 章节 | 题名或原创摘要 | 印刷页 | 迁移方法与知识点 |
|---|---|---|---|
| 3.1 | 嵌套对数幂函数求导（原创摘要） | 34 | 变量同时出现在底与指数时取对数；链式法则；定义域 |
| 3.1 | 比较e的π次幂与π的e次幂（原创摘要） | 35 | 取对数；研究ln(x)/x的最大值；Taylor替代证明 |
| 3.1 | 指数与幂、幂与对数的极限（原创摘要） | 36 | 识别无穷比无穷与零乘无穷；改写后应用洛必达 |
| 3.2 | 对数函数的不定积分（原创摘要） | 37 | 选择u与dv；积分常数；对结果求导检验 |
| 3.2 | 正割函数的定积分（原创摘要） | 37–38 | sec与tan的导数关系；对数原函数；积分上下限 |
| 3.2 | 垂直相交圆柱的公共体积（原创摘要） | 38–39 | 横截面为正方形；对称性；三维几何建模 |
| 3.2 | 恒定清雪体积的雪铲问题（原创摘要） | 39–40 | 积雪厚度随时间线性增长；速度反比于厚度；距离为速度积分 |
| 3.2 | 标准正态的正半轴条件均值（原创摘要） | 40 | 截断分布需除以事件概率；区分E[X1(X>0)]与E[X；X>0] |
| 3.3 | 高斯积分的极坐标证明（原创摘要） | 41 | 积分平方变二维；极坐标Jacobian为r；对称与非负积分 |
| 3.4 | 计算复数i的i次幂（原创摘要） | 42–43 | Euler公式；复对数分支；主值与多值区别 |
| 3.4 | Bernoulli不等式（原创摘要） | 43–44 | Taylor余项符号；归纳证明；x=0时应取等号 |
| 3.4 | 估算平方根37（原创摘要） | 44–45 | Newton迭代；一阶Taylor近似；误差与舍入 |
| 3.4 | 比较Newton、二分与割线法（原创摘要） | 45 | 初值与夹逼；导数需求；局部收敛速度；收敛保证的前提 |
| 3.4 | 原点至平面的最短距离（原创摘要） | 46 | 最小化距离平方；Lagrange乘数；梯度垂直 |
| 3.5 | 可分离ODE及变量替换（原创摘要） | 47 | 分离变量；引入x+y化简；初值决定常数 |
| 3.5 | 一阶线性ODE初值问题（原创摘要） | 48 | 积分因子exp(∫P)；乘积法则逆用；初始条件 |
| 3.5 | 常系数二阶齐次ODE（原创摘要） | 49 | 特征多项式；不同实根、重根、复根；通解线性组合 |
| 3.5 | 常数和一次多项式强迫项的ODE（原创摘要） | 50 | 齐次解加特解；待定系数；共振时修正试探形式 |
| 3.6 | 给定两相关系数约束第三个相关系数（原创摘要） | 51 | 中心化标准化随机变量作L2向量；夹角和余弦；相关范围 |
| 3.6 | 实现最小二乘回归（原创摘要） | 52–53 | 设计矩阵；正规方程；QR与三角求解；误差条件、秩与数值稳定 |
| 3.6 | 二阶对称矩阵的特征分解（原创摘要） | 55 | 定义法、特征方程、迹与行列式；特征向量标准化 |
| 3.6 | 相关矩阵的半正定约束（原创摘要） | 56–57 | 二次型非负；特征值；所有主子式与首序主子式区别 |
| 3.6 | 生成相关标准正态与多元正态（原创摘要） | 57–58 | 线性组合的协方差；Cholesky；特征分解或SVD；退化协方差 |

### 第4章题组

| 章节 | 题名或原创摘要 | 印刷页 | 迁移方法与知识点 |
|---|---|---|---|
| 4.1 | Coin toss game | 61 | 相差一枚硬币；胜、平、负完备划分；处理平局 |
| 4.1 | Card game | 61–62 | 相同牌值概率；胜负对称；并非独立抽样 |
| 4.1 | Drunk passenger | 62–63 | 追踪首末两个特殊座位；中间冲突可压缩 |
| 4.1 | N points on a circle | 63–64 | 以某点为弧起点；几乎处处互斥事件；半圆及更短弧推广 |
| 4.2 | Poker hands | 65–66 | 四条、葫芦、两对；顺序与重复计数；总手牌空间 |
| 4.2 | Hopping rabbit | 66–67 | 末步分类；初值；计数递推与组合和 |
| 4.2 | Screwy pirates 2 | 67 | 多数联盟；按无法开锁的少数子集配置锁；组合数与每人钥匙数 |
| 4.2 | Chess tournament | 68–69 | 淘汰树分区；强者必胜假设；逐轮条件概率乘积 |
| 4.2 | Application letters | 69–71 | 补集；至少一封正确；交集概率与阶乘展开 |
| 4.2 | Birthday problem | 71 | 补集乘积；独立均匀生日假设；阈值23人 |
| 4.2 | 100th digit | 71–72 | 共轭幂的整数性；微小正余项决定小数尾部 |
| 4.2 | Cubic of integer | 72 | 末两位决定立方末两位；模100逆求；均匀整数范围 |
| 4.3 | Boys and girls | 73–74 | 至少一男与随机看见一男；观察机制改变条件事件 |
| 4.3 | All-girl world? | 74 | 生育停止规则；个体比例与家庭平均比例不同；大样本性别比 |
| 4.3 | Unfair coin | 74–75 | 稀有先验；重复观测的似然；后验赔率 |
| 4.3 | Fair probability from an unfair coin | 75 | HT与TH等概率；独立同偏硬币；拒绝HH与TT；退化偏置不产生输出 |
| 4.3 | Dart game | 75–76 | 独立同分布连续距离；条件排名；记录值概率 |
| 4.3 | Birthday line | 76–77 | 首次碰撞分解；相邻概率比；离散最大值 |
| 4.3 | Dice order | 78 | 先排除相同点数；不同数的排列等概率 |
| 4.3 | Monty Hall problem | 78 | 知道奖品位置且总打开羊门；换门收益事件；明确开门策略 |
| 4.3 | Amoeba population | 79 | 首次繁殖分类；独立子群；灭绝概率为最小非负固定点 |
| 4.3 | Candies in a jar | 79–80 | 比较三种颜色的最后位置；按全局末色分类 |
| 4.3 | Coin toss game | 80–81 | HT终止；当前尾部状态；先手次序影响 |
| 4.3 | Russian roulette series | 81–82 | 固定排列与重复随机化；两随机位置与相邻位置；生存信息更新 |
| 4.3 | Aces | 82–83 | 四堆各一A；依次占不同堆；计数比与乘法法则 |
| 4.3 | Gambler's ruin problem | 83–84 | 相邻财富状态；边界概率；公平与有偏两种解 |
| 4.3 | Basketball scores | 84–85 | 当前命中比例作下次概率；全概率递推；均匀计数分布 |
| 4.3 | Cars on road | 85–86 | 无车事件相乘；需补充不相交区间独立假设；恒定边际概率不足 |
| 4.4 | Meeting probability | 88–89 | 二维均匀样本空间；距离带状区域；补集面积 |
| 4.4 | Probability of triangle | 89–90 | 两独立切点；最长段小于半长；排序或对称区域 |
| 4.4 | Property of Poisson process | 90–91 | 指数等待与无记忆；Poisson计数；随机时刻的长度偏差；一般剩余寿命 |
| 4.4 | Moments of normal distribution | 91–92 | 奇矩为零；正态矩母函数；求导得到一至四阶矩 |
| 4.5 | Connecting noodles | 93–94 | 闭环事件；剩余自由端结构；线性期望与调和奇数和 |
| 4.5 | Optimal hedge ratio | 94 | 协方差展开；一阶和二阶条件；回报权重与股数单位区别 |
| 4.5 | Dice game | 94–95 | 首次掷骰分类；继续项保留总期望；终止条件 |
| 4.5 | Card game | 95 | 第一张A位置；普通牌落在特殊牌间隔；无放回顺序统计 |
| 4.5 | Sum of random variables | 95–97 | 独立U(0,1)之和；缩放体积；条件积分与归纳 |
| 4.5 | Coupon collection | 97–98 | 集齐全部种类的分阶段等待；已抽n张时不同种类数；指示变量 |
| 4.5 | Joint default probability | 98–99 | 交并事件上下界；不等边际限制相关范围；不能任取相关±1 |
| 4.6 | Expected value of max and min | 99–100 | 极值CDF与PDF；独立性用于乘积；均匀极值期望 |
| 4.6 | Correlation of max and min | 100–102 | 条件区域；联合CDF求密度；min×max=X1×X2；协方差 |
| 4.6 | Random ants | 102–103 | 碰撞交换标签；方向对称；独立均匀退出时间的最大值 |

### 第5章题组

| 章节 | 题名或原创摘要 | 印刷页 | 迁移方法与知识点 |
|---|---|---|---|
| 5.1 | Gambler's ruin problem | 107–108 | 财富状态压缩；边界概率；有限线性方程组 |
| 5.1 | Dice question | 108–109 | 12与连续两次7；保留最近一个7的状态；吸收概率 |
| 5.1 | Coin triplets | 109–112 | HHH和THH等待时间；先出现概率；状态为最长相关后缀；Penney游戏与后手优势 |
| 5.1 | Color balls | 113–115 | 最终颜色对称；按某颜色个数压缩；以最终吸收事件条件化；条件转移与吸收时间 |
| 5.2 | Drunk man | 116–117 | 位移与平方减时间的鞅；双边吸收概率；退出时间 |
| 5.2 | Dice game | 117 | 停止规则无偷看；几何掷骰次数；随机和期望与适用条件 |
| 5.2 | Ticket line | 117–119 | 付款序列变±1游走；坏路径与反射路径一一对应；非负桥路径比例 |
| 5.2 | Coin sequence | 119–121 | 连续n次正面；新赌徒逐次进入；前后缀重叠决定等待；HHTTHH扩展 |
| 5.3 | Dice game | 123 | 倒推末次掷骰期望；状态与剩余机会数；比较停下收益和继续价值 |
| 5.3 | World series | 123–125 | 终端目标收益；逐状态倒推资金与下注额；等赔率复制与金融二叉树 |
| 5.3 | Dynamic dice game | 126 | 累积收益与归零风险；停止阈值；Bellman递推；风险中性价格 |
| 5.3 | Dynamic card game | 127–128 | 红黑剩余数量作状态；终端边界；立即停止与继续抽牌价值；美式行权类比 |
| 5.4 | Brownian motion | 129–131 | 连续路径、独立平稳正态增量；方差t与协方差min(s,t)；Markov与鞅；平方减t及指数鞅；与平方不相关不代表独立；B1>0、B2<0 |
| 5.4 | Stopping time/ first passage time | 131–135 | 双边退出时间；反射原理与首达密度；几乎必达但均值可无穷；有漂移边界命中概率；ODE和指数鞅两法 |
| 5.4 | Ito's lemma | 135–136 | 二阶修正项；时间依赖变换√t Bt；W^3的漂移；零均值与鞅区别；局部鞅与真鞅的可积性 |

### 第6章题组

| 章节 | 题名或原创摘要 | 印刷页 | 迁移方法与知识点 |
|---|---|---|---|
| 6.1 | Price direction of options | 137–138 | 现价、执行价、波动率、利率、股息与期限方向；欧式期限效应例外；固定其他参数的含义 |
| 6.1 | Put-call parity | 138–139 | 同标的同执行价同到期；股息调整；合成远期；欧式等式、美式界 |
| 6.1 | American v.s. European options | 139–142 | 无股息且非负利率时美式看涨不提前行权；时间价值与融资；Jensen不等式；看跌可能提前行权；执行价方向的凸性套利 |
| 6.1 | Black-Scholes-Merton differential equation | 142–143 | Ito展开；delta消去扩散项；自融资与无风险收益率；真实漂移消失；Feynman-Kac联系 |
| 6.1 | Black-Scholes formula | 143–149 | 股息、外汇和期货版本；市场与过程假设；log(S)正态分布；N(d2)为风险中性到期实值概率；热方程变换；永续首达支付；倒数股票的定价 |
| 6.2 | Delta | 149–152 | 求导时d1和d2也依赖S；ATM短期期限极限；delta中性后再平衡；现金融资腿；ATM价格约0.4σS√τ |
| 6.2 | Gamma | 152–154 | call与put同gamma；正凸性；临近到期ATM曲率集中；delta跳跃极限 |
| 6.2 | Theta | 154–156 | 日历时间t与剩余期限τ符号相反；深实值欧式put或高股息call可正theta；delta中性长gamma与时间耗损；局部PDE风险平衡 |
| 6.2 | Vega | 156–158 | 隐含波动率、smile、skew；恒波动lognormal模型限制；volga符号与Jensen适用条件；call对执行价二阶导恢复风险中性密度 |
| 6.3 | Bull spread | 159 | 低执行价call减高执行价call；收益分段；贴现执行价差与标的比例上界 |
| 6.3 | Straddle | 159–160 | 同执行价call+put；绝对值收益；delta随价格变化；隐含与实现波动率；方差与波动率互换 |
| 6.3 | Binary options | 160–161 | cash-or-nothing的风险中性事件概率；贴现；近到期ATM delta不稳定；窄call spread近似和执行价离散性 |
| 6.3 | Exchange options | 161–162 | 标的价格比；换numeraire需同步换测度；有效波动率含相关项；Margrabe型公式 |
| 6.4 | Portfolio optimization | 163–164 | 权重和为1；组合收益和wᵀΣw；有效前沿；两资产最小方差；借贷、卖空等约束影响 |
| 6.4 | Value at risk | 164–165 | 损益符号与置信度；尾部损失严重性；VaR不总次可加；独立违约反例；条件尾部均值与压力测试 |
| 6.4 | Duration and convexity | 165–167 | modified duration与凸性；一、二阶价格近似；美元久期、DV01；组合加总；逆浮动债以固定债和浮息债复制 |
| 6.4 | Forward and futures | 167–168 | 远期和期货的现金流时点；确定利率时持有成本；随机利率与价格相关造成convexity adjustment |
| 6.4 | Interest rate models | 168–169 | 短率模型与HJM远期曲线模型；均衡模型与拟合初始曲线；Vasicek、CIR、Ho-Lee、Hull-White；均值回复；CIR边界与Feller条件 |

### 第7章题组

| 章节 | 题名或原创摘要 | 印刷页 | 迁移方法与知识点 |
|---|---|---|---|
| 7.1 | Number swap | 172–173 | 加减交换与XOR交换；溢出、别名与语言求值规则；实际编码应优先清晰 |
| 7.1 | Unique elements | 173–174 | 只在相邻值变化时输出；空数组处理；空间与时间复杂度 |
| 7.1 | Horner's algorithm | 174 | 嵌套乘加；线性次数；数值误差与fused multiply-add |
| 7.1 | Moving average | 174 | 旧窗口和减移出加移入；边界索引；O(m)总时间 |
| 7.1 | Sorting algorithm | 174–176 | insertion、merge、quick；平均与最坏差异；分治；quicksort成对比较概率 |
| 7.1 | Random permutation | 176–177 | 随机键排序；Knuth/Fisher-Yates等概率交换；未知长度流的reservoir sampling |
| 7.1 | Search algorithm | 177–179 | 成对求min/max；未知规模的指数扩张加二分；行列单调矩阵的阶梯搜索 |
| 7.1 | Fibonacci numbers | 179–180 | 重复子问题导致指数时间；迭代DP；二阶矩阵快速幂；单位成本与大整数成本区别 |
| 7.1 | Maximum contiguous subarray | 180–182 | 最大区间和；前缀最小值；全负数与空区间约定；最优区间索引需单独跟踪 |
| 7.2 | Power of 2? | 182 | 正整数才可用x&(x−1)==0；0与负数边界 |
| 7.2 | Multiplication by 7 | 182 | 8x−x；整数位宽、符号与溢出 |
| 7.2 | Probability simulation | 182–183 | 逐位产生U(0,1)；比较概率p的二进制展开；几乎必然终止与精度 |
| 7.2 | Poisonous wine | 183 | 一轮二进制群测；2^k可区分状态；标签与检测模式对应 |
| 7.3 | Monte Carlo simulation | 184–189 | 大数定律；风险中性GBM精确离散；终值与路径依赖；逆CDF、拒绝采样及随机符号；标准误差1/√M；反变量、矩匹配、控制变量、重要性抽样、低差异序列；共用随机数估计Greeks；面积法估π |
| 7.3 | Finite difference method | 189–191 | 终端和边界条件；显式、隐式、Crank-Nicolson；一阶时间和二阶空间近似；热方程显式稳定性κΔt/Δx²≤1/2；稳定、收敛、精度和计算成本区别 |

### 原书目录：190条完整转录

下列层级、标题和起始页以原目录PDF7–11核对。句末标点与点引导线不转录；正文涵盖结束页另在JSON。

| 层级 | 章节 | 原标题 | 印刷起始页 |
|---|---|---|---|
| 1 | 1 | General Principles | 1 |
| 2 | 1 | Build a broad knowledge base | 1 |
| 2 | 1 | Practice your interview skills | 1 |
| 2 | 1 | Listen carefully | 2 |
| 2 | 1 | Speak your mind | 2 |
| 2 | 1 | Make reasonable assumptions | 2 |
| 1 | 2 | Brain Teasers | 3 |
| 2 | 2.1 | Problem Simplification | 3 |
| 3 | 2.1 | Screwy pirates | 3 |
| 3 | 2.1 | Tiger and sheep | 4 |
| 2 | 2.2 | Logic Reasoning | 5 |
| 3 | 2.2 | River crossing | 5 |
| 3 | 2.2 | Birthday problem | 5 |
| 3 | 2.2 | Card game | 6 |
| 3 | 2.2 | Burning ropes | 7 |
| 3 | 2.2 | Defective ball | 7 |
| 3 | 2.2 | Trailing zeros | 9 |
| 3 | 2.2 | Horse race | 9 |
| 3 | 2.2 | Infinite sequence | 10 |
| 2 | 2.3 | Thinking Out of the Box | 10 |
| 3 | 2.3 | Box packing | 10 |
| 3 | 2.3 | Calendar cubes | 11 |
| 3 | 2.3 | Door to offer | 12 |
| 3 | 2.3 | Message delivery | 13 |
| 3 | 2.3 | Last ball | 13 |
| 3 | 2.3 | Light switches | 14 |
| 3 | 2.3 | Quant salary | 15 |
| 2 | 2.4 | Application of Symmetry | 15 |
| 3 | 2.4 | Coin piles | 15 |
| 3 | 2.4 | Mislabeled bags | 16 |
| 3 | 2.4 | Wise men | 17 |
| 2 | 2.5 | Series Summation | 17 |
| 3 | 2.5 | Clock pieces | 18 |
| 3 | 2.5 | Missing integers | 18 |
| 3 | 2.5 | Counterfeit coins I | 19 |
| 3 | 2.5 | Glass balls | 19 |
| 2 | 2.6 | The Pigeon Hole Principle | 20 |
| 3 | 2.6 | Matching socks | 21 |
| 3 | 2.6 | Handshakes | 21 |
| 3 | 2.6 | Have we met before? | 21 |
| 3 | 2.6 | Ants on a square | 22 |
| 3 | 2.6 | Counterfeit coins II | 22 |
| 2 | 2.7 | Modular Arithmetic | 23 |
| 3 | 2.7 | Prisoner problem | 24 |
| 3 | 2.7 | Division by 9 | 25 |
| 3 | 2.7 | Chameleon colors | 26 |
| 2 | 2.8 | Math Induction | 27 |
| 3 | 2.8 | Coin split problem | 27 |
| 3 | 2.8 | Chocolate bar problem | 28 |
| 3 | 2.8 | Race track | 29 |
| 2 | 2.9 | Proof by Contradiction | 31 |
| 3 | 2.9 | Irrational number | 31 |
| 3 | 2.9 | Rainbow hats | 31 |
| 1 | 3 | Calculus and Linear Algebra | 33 |
| 2 | 3.1 | Limits and Derivatives | 33 |
| 3 | 3.1 | Basics of derivatives | 33 |
| 3 | 3.1 | Maximum and minimum | 34 |
| 3 | 3.1 | L'Hospital's rule | 35 |
| 2 | 3.2 | Integration | 36 |
| 3 | 3.2 | Basics of integration | 36 |
| 3 | 3.2 | Applications of integration | 38 |
| 3 | 3.2 | Expected value using integration | 40 |
| 2 | 3.3 | Partial Derivatives and Multiple Integrals | 40 |
| 2 | 3.4 | Important Calculus Methods | 41 |
| 3 | 3.4 | Taylor's series | 41 |
| 3 | 3.4 | Newton's method | 44 |
| 3 | 3.4 | Lagrange multipliers | 45 |
| 2 | 3.5 | Ordinary Differential Equations | 46 |
| 3 | 3.5 | Separable differential equations | 47 |
| 3 | 3.5 | First-order linear differential equations | 47 |
| 3 | 3.5 | Homogeneous linear equations | 48 |
| 3 | 3.5 | Nonhomogeneous linear equations | 49 |
| 2 | 3.6 | Linear Algebra | 50 |
| 3 | 3.6 | Vectors | 50 |
| 3 | 3.6 | QR decomposition | 52 |
| 3 | 3.6 | Determinant, eigenvalue and eigenvector | 53 |
| 3 | 3.6 | Positive semidefinite/definite matrix | 56 |
| 3 | 3.6 | LU decomposition and Cholesky decomposition | 57 |
| 1 | 4 | Probability Theory | 59 |
| 2 | 4.1 | Basic Probability Definitions and Set Operations | 59 |
| 3 | 4.1 | Coin toss game | 61 |
| 3 | 4.1 | Card game | 61 |
| 3 | 4.1 | Drunk passenger | 62 |
| 3 | 4.1 | N points on a circle | 63 |
| 2 | 4.2 | Combinatorial Analysis | 64 |
| 3 | 4.2 | Poker hands | 65 |
| 3 | 4.2 | Hopping rabbit | 66 |
| 3 | 4.2 | Screwy pirates 2 | 67 |
| 3 | 4.2 | Chess tournament | 68 |
| 3 | 4.2 | Application letters | 69 |
| 3 | 4.2 | Birthday problem | 71 |
| 3 | 4.2 | 100th digit | 71 |
| 3 | 4.2 | Cubic of integer | 72 |
| 2 | 4.3 | Conditional Probability and Bayes' formula | 72 |
| 3 | 4.3 | Boys and girls | 73 |
| 3 | 4.3 | All-girl world? | 74 |
| 3 | 4.3 | Unfair coin | 74 |
| 3 | 4.3 | Fair probability from an unfair coin | 75 |
| 3 | 4.3 | Dart game | 75 |
| 3 | 4.3 | Birthday line | 76 |
| 3 | 4.3 | Dice order | 78 |
| 3 | 4.3 | Monty Hall problem | 78 |
| 3 | 4.3 | Amoeba population | 79 |
| 3 | 4.3 | Candies in a jar | 79 |
| 3 | 4.3 | Coin toss game | 80 |
| 3 | 4.3 | Russian roulette series | 81 |
| 3 | 4.3 | Aces | 82 |
| 3 | 4.3 | Gambler's ruin problem | 83 |
| 3 | 4.3 | Basketball scores | 84 |
| 3 | 4.3 | Cars on road | 85 |
| 2 | 4.4 | Discrete and Continuous Distributions | 86 |
| 3 | 4.4 | Meeting probability | 88 |
| 3 | 4.4 | Probability of triangle | 89 |
| 3 | 4.4 | Property of Poisson process | 90 |
| 3 | 4.4 | Moments of normal distribution | 91 |
| 2 | 4.5 | Expected Value, Variance & Covariance | 92 |
| 3 | 4.5 | Connecting noodles | 93 |
| 3 | 4.5 | Optimal hedge ratio | 94 |
| 3 | 4.5 | Dice game | 94 |
| 3 | 4.5 | Card game | 95 |
| 3 | 4.5 | Sum of random variables | 95 |
| 3 | 4.5 | Coupon collection | 97 |
| 3 | 4.5 | Joint default probability | 98 |
| 2 | 4.6 | Order Statistics | 99 |
| 3 | 4.6 | Expected value of max and min | 99 |
| 3 | 4.6 | Correlation of max and min | 100 |
| 3 | 4.6 | Random ants | 102 |
| 1 | 5 | Stochastic Process and Stochastic Calculus | 105 |
| 2 | 5.1 | Markov Chain | 105 |
| 3 | 5.1 | Gambler's ruin problem | 107 |
| 3 | 5.1 | Dice question | 108 |
| 3 | 5.1 | Coin triplets | 109 |
| 3 | 5.1 | Color balls | 113 |
| 2 | 5.2 | Martingale and Random walk | 115 |
| 3 | 5.2 | Drunk man | 116 |
| 3 | 5.2 | Dice game | 117 |
| 3 | 5.2 | Ticket line | 117 |
| 3 | 5.2 | Coin sequence | 119 |
| 2 | 5.3 | Dynamic Programming | 121 |
| 3 | 5.3 | Dynamic programming (DP) algorithm | 122 |
| 3 | 5.3 | Dice game | 123 |
| 3 | 5.3 | World series | 123 |
| 3 | 5.3 | Dynamic dice game | 126 |
| 3 | 5.3 | Dynamic card game | 127 |
| 2 | 5.4 | Brownian Motion and Stochastic Calculus | 129 |
| 3 | 5.4 | Brownian motion | 129 |
| 3 | 5.4 | Stopping time/ first passage time | 131 |
| 3 | 5.4 | Ito's lemma | 135 |
| 1 | 6 | Finance | 137 |
| 2 | 6.1 | Option Pricing | 137 |
| 3 | 6.1 | Price direction of options | 137 |
| 3 | 6.1 | Put-call parity | 138 |
| 3 | 6.1 | American v.s. European options | 139 |
| 3 | 6.1 | Black-Scholes-Merton differential equation | 142 |
| 3 | 6.1 | Black-Scholes formula | 143 |
| 2 | 6.2 | The Greeks | 149 |
| 3 | 6.2 | Delta | 149 |
| 3 | 6.2 | Gamma | 152 |
| 3 | 6.2 | Theta | 154 |
| 3 | 6.2 | Vega | 156 |
| 2 | 6.3 | Option Portfolios and Exotic Options | 158 |
| 3 | 6.3 | Bull spread | 159 |
| 3 | 6.3 | Straddle | 159 |
| 3 | 6.3 | Binary options | 160 |
| 3 | 6.3 | Exchange options | 161 |
| 2 | 6.4 | Other Finance Questions | 163 |
| 3 | 6.4 | Portfolio optimization | 163 |
| 3 | 6.4 | Value at risk | 164 |
| 3 | 6.4 | Duration and convexity | 165 |
| 3 | 6.4 | Forward and futures | 167 |
| 3 | 6.4 | Interest rate models | 168 |
| 1 | 7 | Algorithms and Numerical Methods | 171 |
| 2 | 7.1 | Algorithms | 171 |
| 3 | 7.1 | Number swap | 172 |
| 3 | 7.1 | Unique elements | 173 |
| 3 | 7.1 | Horner's algorithm | 174 |
| 3 | 7.1 | Moving average | 174 |
| 3 | 7.1 | Sorting algorithm | 174 |
| 3 | 7.1 | Random permutation | 176 |
| 3 | 7.1 | Search algorithm | 177 |
| 3 | 7.1 | Fibonacci numbers | 179 |
| 3 | 7.1 | Maximum contiguous subarray | 180 |
| 2 | 7.2 | The Power of Two | 182 |
| 3 | 7.2 | Power of 2? | 182 |
| 3 | 7.2 | Multiplication by 7 | 182 |
| 3 | 7.2 | Probability simulation | 182 |
| 3 | 7.2 | Poisonous wine | 183 |
| 2 | 7.3 | Numerical Methods | 184 |
| 3 | 7.3 | Monte Carlo simulation | 184 |
| 3 | 7.3 | Finite difference method | 189 |
