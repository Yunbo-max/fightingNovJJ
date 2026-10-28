# 第12章 马尔可夫链、随机游走与泊松过程

绿皮书对应：§5.1–5.2，pp105–121；§4.3。
 
前置章节：02、03、04、05

## 这一章要掌握什么

- 状态、转移概率与充分性
- 平稳分布与收敛条件
- 吸收概率/时间
- birth–death链
- 随机游走
- 模式等待与重叠
- Poisson过程独立增量
- 指数无记忆
- 更新与更新报酬
- 周期与可约性
- 精确递推与极限

## 代表题：题意、输入输出与思考过程

输入：公平随机游走在0与N之间，从i出发，每步±1；到边界结束。
输出：先到N的概率p_i与平均步数t_i。

p_i=(p_{i−1}+p_{i+1})/2，边界p_0=0,p_N=1，因此p_i=i/N。
t_i=1+(t_{i−1}+t_{i+1})/2，边界t_0=t_N=0，解为i(N−i)。
例如N=5、i=2，成功概率2/5，平均6步。
若加入原地停留概率，每次走动的方向比例可能不变，但实际时间会变长；不能据此说平均吸收时间不变。
对模式HH、HTH等，状态保存“当前后缀与目标前缀的最长匹配”，避免把重叠出现当成独立试验。

## 改条件后的变式

- 有偏游走：概率递推的系数改为p与1−p
- 泊松计数：只有平均到达率恒定不足以推出Poisson，还需要相应增量与稀疏性假设

## 不看答案，检查自己是否理解

- 平稳分布存在等于任意初值都收敛吗？不等于，要检查不可约、周期等条件
- 平均等待时间为1/单次概率总成立吗？重叠模式一般不成立
- 能把有限阈值精确答案直接写成极限常数吗？须区分精确与渐近

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0454 | [Cars on the Highway: From a 20-Minute Window to a 5-Minute Window](https://quantvault.org/problem-3664-cars-on-the-highway-from-a-20-minute-window-to-a-5-minute-wi.html) | 原题及站内解答已读 |
| QV-F0033 | [Gambler's Ruin on a Fair Coin](https://quantvault.org/problem-56-gambler-s-ruin-on-a-fair-coin.html) | 原题及站内解答已读 |
| QV-F0176 | [Stationary Distribution of a Candy Conveyor Belt Markov Chain](https://quantvault.org/problem-515-stationary-distribution-of-a-candy-conveyor-belt-markov-chai.html) | 原题及站内解答已读 |
| QV-F0452 | [Amoeba Extinction: Die, Stay, Split in Two, or Split in Three](https://quantvault.org/problem-3661-amoeba-extinction-die-stay-split-in-two-or-split-in-three.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-12.md)，共146条。

## 深入讲义与新增方法

- [finance_stochastic_curriculum.md](../notes/finance_stochastic_curriculum.md)
- [expectation_games_curriculum.md](../notes/expectation_games_curriculum.md)
- [probability_curriculum.md](../notes/probability_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
