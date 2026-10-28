# 第06章 微积分、泰勒展开与微分方程

绿皮书对应：§3.1–3.5，pp33–50。
 
前置章节：03、04

## 这一章要掌握什么

- 极限与定义域
- 乘商链式/对数求导
- 极值与边界
- LHopital条件
- 定积分与条件归一化
- 换元与分部积分
- 多元链式与梯度Hessian
- Jacobian
- Taylor余项
- 凸性
- Euler复指数
- 分离变量ODE
- 一阶线性积分因子
- 二阶齐次与非齐次ODE

## 代表题：题意、输入输出与思考过程

输入：y=(ln x)^(ln x)，求导。
输出：y′及实数定义域下的表达式。

按正底实幂取x>1。先取对数：ln y=(ln x)ln(ln x)。
两边求导：y′/y=[ln(ln x)+1]/x。
所以 y′=(ln x)^(ln x)[ln(ln x)+1]/x。
这是底数和指数都变化时的对数求导。若错误地只用幂函数公式，会漏掉指数变化的贡献。
金融中的小变化近似使用多元Taylor：ΔV≈V_SΔS+V_tΔt+V_σΔσ+(1/2)V_SS(ΔS)^2，保留项的阶数与误差要说明。

## 改条件后的变式

- 求不定积分lnx：分部积分，结果xlnx−x+C，x>0
- 解y′+6xy=0且y(0)=1：分离变量得y=exp(−3x²)

## 不看答案，检查自己是否理解

- f′=0能保证最小值吗？不能，还要检查形状与边界
- Hessian半正定足以说明单点严格极小吗？仅单点半正定一般不足
- 换元后为什么有Jacobian？坐标变化改变了面积或体积的局部缩放

## 已读公开题的练习入口

| 来源ID | 代表题 | 访问/核对范围 |
|---|---|---|
| QV-F0427 | [Differentiating (ln x) to the Power ln x](https://quantvault.org/problem-3630-differentiating-ln-x-to-the-power-ln-x.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0437 | [Distance From the Origin to the Plane 2x + 3y + 4z = 12](https://quantvault.org/problem-3643-distance-from-the-origin-to-the-plane-2x-3y-4z-12.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0440 | [First-Order Linear ODE: y' + y/x = 1/x^2 with y(1) = 1](https://quantvault.org/problem-3646-first-order-linear-ode-y-y-x-1-x-2-with-y-1-1.html) | 原题及站内解答已读；核心结论另有独立检查 |
| QV-F0441 | [General Solution of y'' + y' + y = 0](https://quantvault.org/problem-3647-general-solution-of-y-y-y-0.html) | 原题及站内解答已读；核心结论另有独立检查 |

本章全部目录题：[题目索引](../indexes/chapter-06.md)，共25条。

## 深入讲义与新增方法

- [algebra_optimization_curriculum.md](../notes/algebra_optimization_curriculum.md)
- [greenbook_curriculum.md](../notes/greenbook_curriculum.md)

这张卡片是复习入口；深入讲义保留完整推导、更多代表题及勘误。题目路由只负责定位方法，原题未见时需先检查具体约束。
