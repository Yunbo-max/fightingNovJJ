> 当前总复习排期以 [WEEK_PLAN.md](../WEEK_PLAN.md) 为准；本讲义内的领域日程只作为补充建议。

# 扩展目录的方法补充：967条记录如何读

实时公开目录中，本模块负责Coding 786条、Combinatorics 181条，共967个不同ID。`coding_combinatorics_live_family_map.json`完整保留每个ID、题名、标签、方法候选和公开例题/主资料链接。其中83条已有实际公开原题与解答审阅，884条只是依据公开元数据做**方法路由**。后者没有读过完整原题，不声称已知其全部约束、答案或最优算法，也不把主资料链接冒充原题公开副本。

路由有主族与附加族，均可非唯一。单凭“shortest”不能认作最短路，可能是最短子数组；单凭“process”不能认作并发，可能是随机过程或任务仿真；“volume”也可能实际指成交笔数。83道已读原题的主族按正文人工校准，其余保留推断边界，拿到题目后先重做输入输出确认。

基础教材已经覆盖哈希、前缀和、滑窗、排序、贪心、基础DP、图搜索、FIFO和回撤。以下补上扩展元数据暴露出的新族。均为方法说明和原创小例，不是884道未读题的代答。

## 1. 星与杠、生成函数与无标签分拆

**输入→输出：** N个相同单位分到k个有标签盒，问多少分法。**对象：** 非负整数向量`(x1,…,xk)`，总和N。N颗星之间/两端放k-1道杠，给`C(N+k-1,k-1)`；若每盒至少1，先减1，得`C(N-1,k-1)`。这与“不同学生分组”的多项式系数不同，因为物品是否可区分已经改变对象。

有容量上限时，生成函数把每个盒子的允许贡献写成`1+x+…+x^U`，乘积的`x^N`系数就是分法数。因子选一项对应每盒一个取值，一一对应是公式的理由。统一上限U的容斥式为

\[
\sum_{j=0}^{k}(-1)^j\binom{k}{j}
\binom{N-j(U+1)+k-1}{k-1},
\]

负的剩余总量项视为0。自编：N=3、k=2、每盒≤2，全部非负解4个，删(0,3)与(3,0)，剩2个。无限次使用面值w的无序组合因子为`1/(1-x^w)`；若改为跳步**顺序**有别，不能沿用同一个乘积。

[NIST整数分拆与生成函数](https://dlmf.nist.gov/26.9)提供进一步公式查阅。选择普通或指数生成函数前，先确认物品是否有标签。

**不同球放无名非空盒**用第二类Stirling数，不等同于整数分拆。插入第n个球：进已有k盒有k种，或独占新盒，故`S(n,k)=k S(n-1,k)+S(n-1,k-1)`。自编3个不同球进2个无名盒为3种；给盒贴两个标签后变6种。有空盒或固定容量，状态还要改变。[NIST Stirling定义与递推](https://dlmf.nist.gov/26.8)

## 2. 对称除重需要轨道，不总能直接除旋转数

计二色三珠环，旋转相同视同。8个长度3二进制串不能直接除3，因为000与111旋转后仍是自己。Burnside改为数每个变换的不动串：恒等8个，两个非平凡旋转各2个，总轨道`(8+2+2)/3=4`。

保存/分类的状态是“变换有哪些循环”，每个循环中的颜色必须相同。若要求恰r个红珠，还需对循环长度进行受限颜色分配；若镜像也视同，要把反射纳入群。只有轨道大小相同时，统一除一个常数才成立。初学者本周只要能解释为什么裸除法可能错。[Stanley主资料，群作用与Burnside章节](https://math.mit.edu/~rstan/pubs/pubfiles/79.pdf)

## 3. 模、素因子与开关不变量

整除问题先拆模条件，数字乘积问题先拆素因子指数；正因数个数来自各指数可选范围的乘法。开关/行列翻转把“操作两次抵消”转成模2加法，先问哪些奇偶量不随操作改变，再问是否能构造目标。状态约束未必独立，不能把每条约束都机械当作概率减半。

不同余数条件若涉及多个模数，先查它们是否互质；非互质时需要相容性，不能套最简单的中国剩余定理版本。这里只给路标，不替未读数论题设答案。[NIST数论函数主资料](https://dlmf.nist.gov/27.2)

## 4. 背包、字符串DP与“要存两个最优值”的情况

| 输入目标 | 状态应保存什么 | 最常做的操作与优化理由 |
|---|---|---|
| 0/1物品和容量→最大价值/可行性 | 处理物品数与剩余容量 | 一维容量倒序，防同物品重复使用 |
| 无限面值→最少硬币 | 金额的最少使用数 | 转移从金额减某面值而来；不可达设无穷大 |
| 源串中出现目标子序列次数 | 两个前缀的匹配方案数 | 跳过源字符，或相等时匹配；空目标有1种 |
| 任意符号数组→最大连续乘积 | 当前末尾最大值和最小值 | 负数把最大/最小互换，不能只留最大 |
| 有时间/交易限制的收益最优 | 时间、持仓和剩余额度等 | 确认状态足以决定未来，所有右侧读旧状态 |

“硬币组合数”与“硬币序列数”会因循环顺序改变，先定义结果对象。最大乘积自编`[-2,3,-4]`最优24，丢掉末尾最小积会漏掉它。字符串计数若压成一行，目标索引倒序更新，避免同一源字符在一轮里被重复匹配。

公开练习：[最少硬币LC322](https://leetcode.com/problems/coin-change/description/?envId=dynamic-programming&envType=problem-list-v2)、[子序列计数LC115](https://leetcode.com/problems/distinct-subsequences/description/)、[最大乘积LC152](https://leetcode.com/problems/maximum-product-subarray/description/)。它们与某条QV标题同族，不保证完整题意相同。

## 5. 图算法的选择条件要比算法名字先说

输入先分有向/无向、权值/容量、是否有负边、问单源/全源或连通全部节点。单位边长用BFS；非负权可用Dijkstra；负边但需检测负环时看Bellman–Ford；DAG可按拓扑序传播。一个状态可能是“位置+剩余障碍额度”，不能只标记位置。最短路资料见[Princeton作者课程](https://algs4.cs.princeton.edu/44sp/)。

最小生成树的目标是连接所有节点、总边权最小；与每点到源最短不同。Kruskal按边权排序，用并查集避免成环；割性质解释为何可取轻边。有相等边权时最优树可不唯一。[MST主资料](https://algs4.cs.princeton.edu/43mst/index.php)

匹配与流要保存残量网络，并允许取消旧选择；只挑当前看起来最好的边可能堵住后续匹配。二分图非冲突选择可与匹配/最小覆盖联系，须先证明图确实二分。这里不从题名直接断言某个棋盘题的答案。[最大流/最小割实现资料](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/FordFulkerson.html)

## 6. 堆、LRU、树与区间数据结构

K个已排序流合并，堆只存每流当前头，弹最小后补同流下一项，总N项约O(N log K)，状态O(K)；外存数据还要考虑磁盘块与归并趟数。[优先队列与多路合并](https://algs4.cs.princeton.edu/24pq/)

LRU的最常操作是“按键定位、把某项移到最近端、淘汰最老”。哈希定位节点、双链表移动节点，相互配合才实现平均常数时间；每次更新两个索引的一致性。LFU还需频率层与并列淘汰口径，不能把LRU原样换个名字。[公开LRU契约](https://leetcode.com/problems/lru-cache/description/)

链表反转保存`prev/current/next`，先存next再断当前链接；树深度的空树边界为0，根到叶的节点数与边数要先约定。树遍历访问一次不代表递归额外空间常数，链形树栈可到n。[链表反转](https://leetcode.com/problems/reverse-linked-list/description/)、[树深度](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

| 反复操作 | 候选结构 | 先确认的条件 |
|---|---|---|
| 单点加、区间和 | Fenwick树 | 离散秩、边界是否半开、值类型溢出 |
| 单点改、区间聚合 | 线段树 | 聚合满足结合律并有单位元，不一定可交换 |
| 区间更新、区间聚合 | lazy线段树 | 更新可作用于摘要且可组合，组合方向明确 |
| 静态区间幂等查询 | 稀疏表 | 数据不更新；使用重叠区间时需幂等性质 |

区间和加δ时摘要不能只有sum，还要知道段长度；区间最小值整体加δ时直接平移min即可。仿射更新`ax+b`组合有先后，不能随意交换。参考：[Fenwick](https://atcoder.github.io/ac-library/production/document_en/fenwicktree.html)、[线段树](https://atcoder.github.io/ac-library/production/document_en/segtree.html)、[lazy映射契约](https://atcoder.github.io/ac-library/master/document_en/lazysegtree.html)。

## 7. 字符串匹配、Trie与解析

KMP保存“当前已匹配前缀长度”及失败后可复用的最长边界，避免文本游标退回；Trie把字典单词共享的前缀合成状态。查询一个长度L键的成本与L有关，但“输出此前缀下所有单词”还要计访问/输出量。滚动哈希若可能碰撞，应校验或明确误判概率；不是确定相等证明。[模式匹配](https://algs4.cs.princeton.edu/53substring/)、[Trie作者实现](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/TrieSET.html)

表达式先分词，再处理运算优先级、括号与一元负号；RPN的栈法不自动处理普通中缀优先级。日志、IP和坐标校验要分语法合法与数值范围合法，明确是抛错、跳过还是返回失败。[计算器公开题](https://leetcode.com/problems/basic-calculator/description/)

UTF-8是字节编码，字符数不等于字节数；随机抽字节、Unicode码点、用户可见字形是不同采样对象。[UTF-8规范](https://www.rfc-editor.org/info/rfc3629/)

## 8. 数值、近似摘要与计算几何

在线均值/方差优先维护稳定的增量统计，而不是大数平方和相减；删除旧观测的滚动版本需额外历史状态与误差控制。解线性方程不要先显式求逆；先确认方阵、满秩及条件数，残差小也不自动保证参数误差小。[NumPy求解接口](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)

近似流式问题先分目标：常见项频率、不同元素数、分位数，各自摘要和误差语义不同。保存空间小不等于能删除任意历史，能合并也不等于误差无条件不变。压缩参数、更新正负、输入顺序、哈希假设都要写进契约。参考：[频率摘要](https://datasketches.apache.org/docs/Frequency/FrequentItemsOverview.html)、[HLL](https://datasketches.apache.org/docs/HLL/HllSketches.html)、[t-digest作者对不变量与误差的区分](https://github.com/tdunning/t-digest)。

几何扫描先定义边界：凸包是否保留边上共线点，扇区边界是否包含，整数叉积会否溢出。立方体表面积可逐块数6面再减共享面，每共享面被两块各计一次，所以减2；不要混“被涂表面的小立方块个数”与“表面积”。[凸包边界公开练习](https://leetcode.com/problems/erect-the-fence/description/)、[堆叠立方体表面积](https://leetcode.com/problems/surface-area-of-3d-shapes/description/)

## 9. Python/pandas、C++与并发：按岗位选读

pandas连接先查键是否唯一，多对多连接可产生笛卡尔展开。`agg`给每组摘要，`transform`常把结果广播回与原组对齐的形状；业务要原行还是组表，决定操作。时间窗口明确设置`min_periods/closed/label/center`，预测特征尤其防未来信息混入。[连接](https://pandas.pydata.org/docs/user_guide/merging.html)、[分组](https://pandas.pydata.org/docs/user_guide/groupby.html)、[窗口](https://pandas.pydata.org/docs/user_guide/window.html)

C++先判断谁拥有资源、何时销毁、复制与移动分别意味着什么；裸指针存在不等于拥有，shared_ptr引用计数也不使被指对象自动线程安全。Python赋值多是绑定引用，复制容器不一定复制其内部可变对象。[C++智能指针草案](https://eel.is/c++draft/smartptr)、[Python对象模型](https://docs.python.org/3/reference/datamodel.html)

并发先描述共享状态和需要保持的不变量，再选锁/原子/队列。单个原子变量的原子性不等于多个变量组成的操作原子；relaxed原子不自动发布其他普通内存写入。无锁链表还要处理节点回收与ABA，不在一周入门课中拼出未经证明的实现。[数据竞争](https://eel.is/c++draft/intro.races)、[内存顺序](https://eel.is/c++draft/atomics.order)

线程、进程、asyncio有不同共享与调度模型；先确认解释器和构建配置，区分CPU工作与等待I/O。异步协程里直接运行阻塞操作仍会堵住事件循环。[asyncio](https://docs.python.org/3/library/asyncio.html)、[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

协议与服务设计先定消息边界、重试幂等、缓冲上限与背压，再谈吞吐。TCP可靠字节流不替应用划分一条条消息，应用仍需长度或分隔协议。[TCP规范](https://www.rfc-editor.org/rfc/rfc9293.html)

## 10. 与一周主线的关系

新增族用于看懂面试追问与找到下一道代表题。第一周只加三项：星与杠/生成函数的“系数在数什么”、0/1背包状态、SQL/pandas连接与聚合形状。目标为C++量化开发时，再给对象生命周期和并发契约一段选读时间；目标为研究岗时，将该时间给数值稳定、统计量与线性求解。其余高级族保留路标，不把967条当成本周逐题作业。

所有方法入口见`coding_combinatorics_family_references.json`，路由统计见`coding_combinatorics_live_family_stats.json`。链接状态只说明已定位公开例题/主资料；对884条原题不授予“题目读完”或“答案验证”状态。
