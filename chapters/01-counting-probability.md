# 第01章 组合计数与概率事件

绿皮书对应：§4.1–4.2，pp59–72。
 
前置章节：可直接开始。

## 这一章要掌握什么

- 样本空间与等可能性
- 事件的交并补
- 加法与乘法原理
- 排列、组合、多重排列
- 有放回与无放回
- 隔板法
- 容斥
- 错排
- Catalan计数
- 圆排列、旋转与反射
- 抽屉原理
- 生成函数与双重计数

## 代表题：题意、输入输出与思考过程

输入：随机排列 n 人，问平均有多少人站在自己原来的位置。
输出：期望个数，而非“至少一人站对”的概率。

对第 i 人定义 I_i=1（站对）或0（没站对）。每个人站对的概率是1/n。
总数 X=ΣI_i，所以 E[X]=ΣE[I_i]=n×(1/n)=1。
这个推导不需要这些指示变量相互独立。若问“无人站对”，需要容斥，答案为 Σ_{k=0}^n(-1)^k/k!。
先判断对象是否可区分、顺序是否重要，再确定分母的等可能样本，最后检查是否重复计数。

## 改条件后的变式

- 改问至少一人站对：不能把期望1直接当概率
- 改成圆桌：说明固定谁或除以几种对称，是否区分镜像

## 不看答案，检查自己是否理解

- 三个可区分球放入两个可区分盒子有几种？答案8
- 两个事件独立与互斥有什么区别？正概率互斥事件不能独立
- 为什么期望可加不要求独立？因为积分或求和本身是线性的

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0258 | [Alternating Sum of Squares](https://quantvault.org/problem-1082-alternating-sum-of-squares.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0235 | [Count Even-Product Triplets](https://quantvault.org/problem-912-count-even-product-triplets.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0263 | [Digits of 2^1000 and 5^1000 Written Side by Side](https://quantvault.org/problem-1120-digits-of-2-1000-and-5-1000-written-side-by-side.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0447 | [Hopping Rabbit: Counting Ways Up an n-Step Staircase](https://quantvault.org/problem-3655-hopping-rabbit-counting-ways-up-an-n-step-staircase.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-01.md)，共271条。

## 深入讲义与新增方法

- [combinatorics_curriculum.md](../notes/combinatorics_curriculum.md)
- [probability_curriculum.md](../notes/probability_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
