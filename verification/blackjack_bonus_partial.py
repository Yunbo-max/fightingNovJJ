from fractions import Fraction as F
from pathlib import Path
import json
P=Path(__file__).parent
p,q=F(9,20),F(11,20)
# Full path enumeration of the explicitly proposed three-wager policy.
branches=[{'outcomes':'L','probability':q,'terminal':F(0),'turnover':F(2000)},
 {'outcomes':'WL','probability':p*q,'terminal':F(0),'turnover':F(6000)},
 {'outcomes':'WWL','probability':p*p*q,'terminal':F(4000),'turnover':F(10000)},
 {'outcomes':'WWW','probability':p**3,'terminal':F(12000),'turnover':F(10000)}]
assert sum(b['probability'] for b in branches)==1
wealth=sum(b['probability']*b['terminal'] for b in branches)
turnover=sum(b['probability']*b['turnover'] for b in branches)
assert wealth==1539 and turnover==4610 and wealth==2000-F(1,10)*turnover
strict_wealth=p*p*(F(8000)-F(1,10)*4001)
assert strict_wealth==F(6155919,4000)
result={'method':'独立枚举三笔可行策略全部终局路径；核对补偿财富恒等式',
 'result':{'fixed_10000_turnover_edge_cost':'1000','candidate_expected_cashout':'1539','candidate_expected_actual_turnover':'4610','candidate_profit_vs_1000_deposit':'539','strict_gt_integer_stake_candidate_expected_cashout':str(strict_wealth),'strict_gt_integer_stake_candidate_decimal':float(strict_wealth)},
 'scope':'仅核验第一问边际成本、一般期望恒等式及一个可行策略的值；不证明该策略全局最优。',
 'site_worked_solution_read':False,'full_optimality_proved':False,
 'assumptions':['允许下注至全部可用财富，没有未给出的桌面最大限额','主候选按累计流水至少10000完成','投注整数且需严格超过时第三笔改为4001；连续金额可用4000+epsilon逼近','实际终局现金仅在完成流水或财富归零时结算'],
 'branches':[{k:str(v) for k,v in b.items()} for b in branches]}

(P/'blackjack_bonus_partial_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate_expected_cashout':float(wealth),'expected_actual_turnover':float(turnover),'global_optimality_proved':False}))
