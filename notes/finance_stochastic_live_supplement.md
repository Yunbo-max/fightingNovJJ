> 当前总复习排期以 [WEEK_PLAN.md](../WEEK_PLAN.md) 为准；本讲义内的领域日程只作为补充建议。

# 实时题库新增家族：从标题到公开方法

本补充针对实时目录中的385个金融/随机过程相关ID。51个有实际公开题面和解答复核；其余334个仅按标题和标签路由至方法家族。`metadata_family_route`表示公开同族教材、原始论文或官方材料可以帮助学习，不表示已找到同一道付费题的副本，也不表示已读原题条件。完整逐ID映射、39个来源的访问范围和45个家族见配套JSON。

一周内先掌握主讲义中的状态、鞅、复制、Greeks、现金流和条件报价。以下按缺失机制补齐：每个高级模型应至少能说出状态、目标或支付、关键假设、可验证结论，以及相邻方法为何不能直接替代它。

## A. 随机过程新增家族

### A1. Poisson、复合Poisson与方向订单流

若 \(N_T\sim\mathrm{Poisson}(\lambda T)\)，每笔独立标记Y与N独立，累计量 \(V=\sum_{i=1}^{N_T}Y_i\)，则

\[
EV=\lambda T E[Y],\quad
\operatorname{Var}V=\lambda T E[Y^2],\quad
\varphi_V(u)=\exp\{\lambda T(\varphi_Y(u)-1)\}.
\]

方差使用二阶矩，而不是只用 \(\lambda T\operatorname{Var}Y\)。独立买卖计数率 \(\lambda_+,\lambda_-\) 的差服从Skellam：均值 \((\lambda_+-\lambda_-)T\)，方差 \((\lambda_++\lambda_-)T\)。独立按成交概率p稀释后强度为pλ；若p依赖基本面或队列，不能继续宣称无条件独立稀释。

公交等待的inspection paradox属于更新过程的抽样偏置。一般间隔X下，平稳随机时点的剩余等待均值为 \(E[X^2]/(2EX)\)，前提为相应矩存在；Poisson指数间隔只是特殊的无记忆情形。

### A2. Hawkes：不能把聚集到达当恒定Poisson

指数核模型

\[
\lambda_t=\mu+\sum_{t_i<t}\alpha e^{-\beta(t-t_i)}
\]

中，过去到达提升未来短期强度。线性单变量模型的分支率为 \(\eta=\alpha/\beta\)；\(\eta<1\)时平稳平均率为 \(\mu/(1-\eta)\)。例如μ=.5、α=.8、β=2，平均率为5/6，不能直接把基准率.5当长期到达率。

点过程MLE的核心是

\[
\ell=\sum_i\log\lambda_{t_i}-\int_0^T\lambda_sds.
\]

只最大化第一项会偏向无限抬高强度。需检查初始历史、边界项、平稳性以及时间重标定后的残差，而不只报告似然值。

原作者公开方法：[Laub–Taimre–Pollett，Hawkes Processes](https://arxiv.org/abs/1507.02822)。

### A3. OU、线性SDE与阈值交易

\[
dX_t=\kappa(m-X_t)dt+\eta dW_t
\]

的积分因子给

\[
X_t=m+(X_0-m)e^{-\kappa t}
+\eta\int_0^te^{-\kappa(t-s)}dW_s.
\]

所以均值按指数回归m，条件方差为 \(\eta^2(1-e^{-2\kappa t})/(2\kappa)\)。κ>0才有均值回复的平稳分布；固定初值的过程从一开始通常不平稳。

“最优OU交易阈值”仍需交易成本、收益定义、持仓方向、重启方式与截止时间。命中时间解生成元方程 \(\mathcal L u=-1\)，命中概率解 \(\mathcal L h=0\)；最优停止还需价值匹配及适当光滑粘贴条件。不能仅凭均值回复就给一个普遍最优z-score。

### A4. Kalman、HMM与RTS平滑

线性Gaussian状态模型先预测 \(x^-_t=Ax_{t-1}\)、\(P^-_t=AP_{t-1}A^T+Q\)，再通过创新协方差 \(S_t=HP^-_tH^T+R\) 和增益 \(K_t=P^-_tH^TS_t^{-1}\)更新。HMM先用转移矩阵预测状态概率，再乘本期观测似然并归一化。

滤波使用当时及过去信息；RTS平滑利用未来观测，适合事后估计，直接作为当时交易特征会泄漏。稳健滤波的门控、Student-t或Huber修改需要同时说明均值和协方差如何更新。Huber损失无界，但其影响函数有界；异常观测与真实状态跳变也不能混为一类。

公开原作者方法：[Student-t Kalman smoothers](https://optimization-online.org/2011/12/3270/)。

### A5. 实现波动与bipower分解

高频收益的实现方差 \(RV=\sum r_i^2\)估计二次变差；含有限活动跳跃时，极限包括连续积分方差及跳跃平方和。Bipower量常取

\[
BV=\mu_1^{-2}\sum_i|r_i||r_{i-1}|,
\quad\mu_1=E|Z|=\sqrt{2/\pi}.
\]

在相应模型和采样渐近条件下，BV对稀疏跳跃较稳健，可用RV−BV估计跳跃贡献。市场微观噪声会让无限加密采样失效；应先说明观测模型和采样尺度。

原作者机构材料：[Barndorff-Nielsen–Shephard，Power and Bipower Variation](https://ora.ox.ac.uk/objects/uuid%3A2eac6b4f-bda9-4195-b119-2e7098ab4aeb)。

## B. 定价与衍生品新增家族

### B1. Black、Bachelier与利率numeraire

远期F、确定支付年金/贴现因子A下，Black型call为

\[
V=A[F\Phi(d_1)-K\Phi(d_2)].
\]

这里的Q应是对应numeraire的测度，不能一律使用货币账户Q并假定远期仍无漂移。Caplet的支付日、计息因子和浮动重置日要先列清；swaption常用swap年金作numeraire。

Bachelier则使用正态远期：\(V=A[(F-K)\Phi(z)+\sigma_N\sqrt T\phi(z)]\)。ATM小波动近似给 \(\sigma_N\approx F\sigma_B\)，但这不是跨执行价、负F环境都精确成立的通用换算。FX的Garman–Kohlhagen把国外利率当carry，且需说明报价币种、premium-adjusted与否、spot/forward delta约定。

### B2. Heston、SABR、局部波动与跳跃

| 模型 | 状态和机制 | 面试应说明的边界 |
|---|---|---|
| 局部波动 | \(dS/S=(r-q)dt+\sigma(t,S)dW\) | 拟合边际分布不表示正确复制未来微笑动态 |
| Heston | \(dS/S=(r-q)dt+\sqrt v dW_1\)，\(dv=\kappa(\theta-v)dt+\xi\sqrt v dW_2\) | 指定相关ρ，处理方差边界和离散化负值 |
| SABR | \(dF=\alpha F^\beta dW_1\)，\(d\alpha=\nu\alpha dW_2\) | 指定相关与测度，负利率可能需shift或其他模型；近似式不自动全域无套利 |
| Merton jump diffusion | diffusion加独立复合Poisson跳跃 | Q漂移必须补偿平均跳跃；股票与现金通常不能完全对冲跳跃风险 |

对跳跃乘数J，风险中性漂移包含 \(-\lambda(E[J]-1)\)，不能仍用r−q后又额外加跳跃而不补偿。Heston模拟应把驱动相关构造成 \(Z_2=\rho Z_1+\sqrt{1-\rho^2}Z_\perp\)，同时报告所用方差保持方案和时间偏差。

公开原始出处：[Heston](https://academic.oup.com/rfs/article-abstract/6/2/327/1574747)、[SABR原出版方文章](https://www.wilmott.com/managing--smile--risk/)、[Merton在MIT的工作论文](https://dspace.mit.edu/entities/publication/e63635d9-d2bf-40ce-a79b-67786dd9f105)。这些是方法家族入口，不代表已对题库中的每个校准问题读取具体输入。

### B3. 特征函数、Carr–Madan与数值积分

已知 \(\varphi(u)=E[e^{iu\log S_T}]\) 后可通过变换恢复价格。Carr–Madan给call加入执行价指数阻尼，使变换可积，再用FFT在一组执行价上快速计算。阻尼α要求相应高阶矩 \(E[S_T^{\alpha+1}]\)存在；不满足时不能只调FFT网格来补救。

验收检查应分开：特征函数归一化 \(\varphi(0)=1\)、Q下的一阶矩、积分截断、频率间距/aliasing、执行价插值，以及是否满足单调凸性。单个执行价接近BS真值不验证整个FFT实现。

原作者公开论文：[Carr–Madan，Option valuation using FFT](https://engineering.nyu.edu/sites/default/files/2018-08/CarrMadan2_0.pdf)。

### B4. 障碍、Asian、autocall与方差合约

离散监控障碍MC会漏掉网格之间的触碰。对数价格桥在两端x,y均低于上障碍h时，常波动条件下跨越概率为

\[
\exp\left[-\frac{2(h-x)(h-y)}{\sigma^2\Delta t}\right].
\]

它依赖连续扩散桥假设，跳跃模型不能直接套用。敲入与敲出在同支付、相同监控、无额外返还时相加等于香草；敲入本身不比对应香草更贵。Arithmetic Asian通常无闭式，可用同路径geometric Asian作控制。Autocall需要事件日、观察先后、coupon与赎回状态，不能仅用 \(S_T\) 的边际分布估值。

连续扩散下的方差swap可用对数支付及跨执行价期权静态复制；发生跳跃、有限执行价覆盖和离散采样时要修正。VIX类指数是特定公开方法计算的隐含量，不是保证未来实现波动。市场实现细节应回到[Cboe官方说明](https://www.cboe.com/tradable_products/vix/faqs)。

### B5. 信用结构、CVA与分层现金流

Merton结构模型把到期企业权益视为资产A上的call，支付 \((A_T-D)^+\)；债务为资产减权益。该基本模型只在T判断违约，不能无修改地代表任意时刻破产。

单边CVA可先写成

\[
(1-R_c)E_Q[D_\tau\,E^+_\tau\,1_{\tau\le T}],
\]

再在独立条件下分解暴露与违约。Wrong-way risk正是这种独立性失效的情形。净额结算、抵押、closeout、违约时暴露和付款时点必须由合约决定。

分层损失的基础是attachment A、detachment D，对组合损失L的tranche损失为 \(\min((L-A)^+,D-A)\)。先明确损失单位和本金归一化，再谈相关、Monte Carlo和waterfall；不能把tranche当简单平均信用价差。

## C. 微观结构新增家族

### C1. Kyle：策略需求与价格更新必须相互一致

单期Gaussian模型中，基本面V、独立噪声U，知情客户下单X，做市商看见 \(Y=X+U\)。猜线性均衡

\[
X=\beta(V-EV),\qquad P=EV+\lambda Y.
\]

客户给定λ最大化 \(x(V-EV-\lambda x)\)，得 \(\beta=1/(2\lambda)\)。做市商要求 \(P=E[V\mid Y]\)，得

\[
\lambda=\frac{\beta\sigma_V^2}{\beta^2\sigma_V^2+\sigma_U^2}.
\]

联立得到 \(\beta=\sigma_U/\sigma_V\)、\(\lambda=\sigma_V/(2\sigma_U)\)。这是Gaussian独立噪声、风险中性、单期线性均衡的结论；多期、不同噪声方差和信息释放规则需要重新倒推。

原始论文：[Kyle，Continuous Auctions and Insider Trading](https://people.stern.nyu.edu/lpederse/courses/LAP/papers/Information%2CFundamental/Kyle85.pdf)。

### C2. Hasbrouck信息份额和跨市场lead–lag

同一资产多市场价格常用VECM分离平稳价差与共同随机趋势。若共同趋势对创新的长期暴露为ψ、创新协方差为Ω，且 \(\Omega=LL^T\)，Cholesky信息份额形式为

\[
IS_j=\frac{(\psi L)_j^2}{\psi\Omega\psi^T}.
\]

创新有同期相关时，Cholesky排序会影响份额；应给排序区间或说明识别约束。不能仅凭两个价格序列的一阶交叉相关峰值就认定因果价格发现。时区、撮合时间戳、异步采样、陈旧报价和数据传输延迟都可能制造假lead–lag。

原作者论文记录：[One Security, Many Markets](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1995.tb04054.x)。

### C3. 执行、暂态冲击与数据延迟

执行目标先写成预期成本加风险惩罚，例如 \(E[C]+\lambda\operatorname{Var}C\)。Almgren–Chriss的永久与暂态冲击、持仓价格风险提供一个清楚的权衡，而不是“拆单一定便宜”的口号。瞬态冲击模型还需跟踪旧订单影响如何衰减；忽略恢复状态会让优化状态不完整。

TWAP以时间均匀为目标，VWAP依赖成交量预测；participation算法还需实时量的定义、滞后和可用性。500ms固定延迟题应按接收时刻对齐信号及可执行行情，而不是把事后知道的exchange timestamp直接当可交易价格。Closing auction需独立处理撮合价格、取消规则和不平衡信息，不等同普通连续盘口。

公开原始方法：[Almgren–Chriss](https://doi.org/10.21314/JOR.2001.041)。

### C4. ETF、杠杆重置与跨时区公允价

ETF价格与NAV之间存在交易、申赎、篮子可得性、市场关闭和融资成本。闭市成分的上次价格不自动代表当前公允值；跨时区ETF还需汇率和可交易替代品。创建/赎回机制并不保证所有观察到的价差都可以无成本执行。

每日L倍重置产品的财富为 \(\prod_t(1+Lr_t)\)，不是 \(1+L(\prod_t(1+r_t)-1)\)。例如标的先+10%、再−9.0909%回到起点，3倍产品为 \(1.3\times.7272727=.9454545\)，亏5.4545%（未计费）。持续趋势下也可能超出简单倍数收益，所以“杠杆ETF必然衰减”不是普遍方向结论。

公开官方对照：[SEC关于杠杆及反向ETF的投资者说明](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/sec)。这类材料用于解释结构，不构成产品建议。

### C5. 常乘积AMM和CeFi比较

Uniswap v2的简化储备约束为xy=k。输入 \(\Delta x\)、交易费比例f时，有效输入 \((1-f)\Delta x\)，输出

\[
\Delta y=y-\frac{k}{x+(1-f)\Delta x}.
\]

边际价格y/x、平均成交价 \(\Delta y/\Delta x\)及链下可执行价格不是同一个量。Gas、交易顺序、被夹、结算延迟和库存风险都会影响套利；不能只比较两个屏幕中间价。此公式属于指定v2机制，不代表所有AMM或当前所有Uniswap版本。

协议原始公开论文：[Uniswap v2 Core](https://docs.uniswap.org/whitepaper.pdf)。

## D. 金融研究与常识新增家族

### D1. Kelly、Bayes与资本约束

单次二元赌注，赢概率p、每单位净赢b、亏损1，投入财富比例f，则

\[
\max_f\;p\log(1+bf)+(1-p)\log(1-f)
\quad\Rightarrow\quad f^*=p-(1-p)/b.
\]

还需套用允许卖空、借贷和破产的可行域。连续收益的小收益近似 \(f\approx\mu/\sigma^2\)依赖矩与近似尺度；有交易成本、估计误差或非正财富风险时不能直接套用。Bayes收缩改变的是参数分布和决策目标，不是随意把仓位统一乘一个常数。

### D2. 风险平价、切点组合与不同持有期信号

风险贡献常写为 \(RC_i=w_i(\Sigma w)_i/\sigma_p\)，加总为组合波动。等风险贡献与等资金权重、最小方差、最大Sharpe是不同优化目标。两资产波动率及组合方差均为正时，做多风险平价可得到权重比 \(w_1/w_2=\sigma_2/\sigma_1\)，但该简式不应无条件推广到多资产。

切点组合在传统无约束模型中沿 \(\Sigma^{-1}(\mu-r_f\mathbf1)\)；预期收益估计误差会放大仓位不稳定性。把5日与20日信号合并时，先统一预测目标、实际持有重叠和换手，再估计它们的共同风险；不能只平均两个历史Sharpe。

### D3. 商品carry、公司事件与时点事实

商品远期的融资、仓储和便利收益须分别进入复制成本。便利收益不一定是可直接交易现金流，因此等式需要具体资产和可借贷/储存假设。航空公司买油call是为经营成本上行提供保护，还存在油种、数量、期限和基差差异，不能把它简化为纯粹看涨投机。

并购题先区分EPS机械增厚与经济价值增值；交换比例、增发、债务融资、协同和协同兑现概率都可能改变答案。由事件前后价格反推“批准概率”需要明确状态价值、风险溢价和贴现，不能自动解释为物理成功概率。

“当前恒指/沪深300点位”“主要市场旗舰指数”“期货合约lot size”需要按标的和时点查询官方资料。本补充只给[恒生官方入口](https://www.hsi.com.hk/en-hk/indexes/all-indexes/index-details/?seriesCode=hsi)、[CSI官方说明书](https://oss-ch.csindex.com.cn/static/html/csindex/public/uploads/indices/detail/files/en/000300factsheeten.pdf)、[CME合约单位说明](https://www.cmegroup.com/education/courses/introduction-to-futures/about-contract-notional-value)，没有填入容易过期的行情数值。

职业动机题应由个人经历和岗位理解作答；方法路由只提供金融工作的内容背景，不能代写成不存在的个人经历。

## E. 最小验收与访问边界

高级题的最低合格答案应包含：模型状态/支付；信息与测度；目标和约束；一个公式或可执行递推；至少一个极限、单位或反例检查。知识标签只作为路由，不是题面证据。公开来源若只有摘要、机构目录或扫描PDF，访问范围已在来源JSON中单独标明；没有把它们计为“原题已读”。

新增家族的来源以原作者论文、作者机构教材、交易所、监管机构或协议原始说明为主。标题相似不保证条件相同，应在读到具体题面后重新核对参数、支付、交易限制和目标。
