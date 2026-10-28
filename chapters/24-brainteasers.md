# 第24章 BrainTeasers九类方法与证明

绿皮书对应：第2章，pp3–32。
 
前置章节：01、02、05、06、07、21

## 这一章要掌握什么

- 小规模简化
- 逆向归纳
- 知识状态与逻辑排除
- 对称性与互补
- 不变量/奇偶/染色
- 求和与编码
- 抽屉原理
- 模运算
- 归纳与反证
- 信息下界与可构造策略
- 极值原则
- 费米估计与单位检查

## 代表题：题意、输入输出与思考过程

输入：1000枚硬币，恰20枚正面；蒙眼可翻面，要求分成两堆且正面数相同。
输出：对任意初始排列都成功的操作。

任取20枚。设其中原有h枚正面，剩下980枚中就有20−h枚正面。
把取出的20枚全部翻面，它原来的20−h枚反面成为正面，因此两堆都为20−h枚正面。
不需要知道h，也不需要随机性；保证来自代数恒等式。
对12球称重，要同时追踪编号与偏重/偏轻；3^3≥24只是信息必要条件，还要给合法称重树。
对随机点名的杯子计数，公平抽样可保证最终完成概率1，却不能给有限最坏时间。
对装砖染色，必须说明摆放轴向等几何约束；换一种允许操作就要重新证明不变量。

## 改条件后的变式

- 海盗分配：先写生存、金币和相同结果下的偏好，再从最后一人倒推
- 七人同时猜七色帽：分工覆盖总色码模7的七种余数，不能借用有顺序发言的信息

## 不看答案，检查自己是否理解

- 观察十次都成立算证明吗？不算
- 证明至少需要三次称重就完成了吗？还需证明三次能构造成功
- 题目问保证还是平均，会改变答案吗？经常会，先把量词说清楚

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0104 | [Age Whose Square Is the Year](https://quantvault.org/problem-228-age-whose-square-is-the-year.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0413 | [Calendar Cubes: Two Dice That Show Every Date](https://quantvault.org/problem-3613-calendar-cubes-two-dice-that-show-every-date.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0416 | [Finding the Counterfeit Bag With One Weighing](https://quantvault.org/problem-3618-finding-the-counterfeit-bag-with-one-weighing.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0006 | [Mislabeled Bins](https://quantvault.org/problem-12-mislabeled-bins.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-24.md)，共111条。

## 深入讲义与新增方法

- [brainteaser_curriculum.md](../notes/brainteaser_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)
- [combinatorics_curriculum.md](../notes/combinatorics_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
