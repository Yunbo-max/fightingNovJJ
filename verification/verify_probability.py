"""Independent finite enumeration, exact recurrences and numerical integration.

This checks selected claims; it does not promote unchecked pages to verified.
Run with Python + numpy + scipy. No network calls or private content.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations, combinations
from math import factorial, comb, sqrt, log2, asin, pi, exp
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm, binom, skellam

HERE = Path(__file__).resolve().parent
checks = []

def record(cid, method, observed, expected, ok=True, detail=None):
    assert ok, (cid, observed, expected)
    checks.append(dict(catalog_id=cid, method=method, observed=str(observed),
                       expected=str(expected), passed=bool(ok), detail=detail))

def solve_fraction(a, b):
    a = [[F(x) for x in row] + [F(y)] for row, y in zip(a, b)]
    n = len(b)
    for c in range(n):
        pivot = next(r for r in range(c, n) if a[r][c])
        a[c], a[pivot] = a[pivot], a[c]
        z = a[c][c]
        a[c] = [x / z for x in a[c]]
        for r in range(n):
            if r != c and a[r][c]:
                z = a[r][c]
                a[r] = [x - z*y for x, y in zip(a[r], a[c])]
    return [a[r][-1] for r in range(n)]

def pattern_probability(win, lose):
    states = sorted({""} | {p[:k] for p in (win, lose) for k in range(1, len(p))})
    ix = {s:i for i,s in enumerate(states)}
    a = [[F(i == j) for j in range(len(states))] for i in range(len(states))]
    b = [F(0) for _ in states]
    for s in states:
        for ch in "HT":
            t = s + ch
            if t.endswith(win): b[ix[s]] += F(1,2)
            elif not t.endswith(lose):
                target = max((v for v in states if t.endswith(v)), key=len)
                a[ix[s]][ix[target]] -= F(1,2)
    return solve_fraction(a,b)[ix[""]]

for cid, p1, p2, answer in [
    ("QV-F0005","HHT","THH",F(1,4)),
    ("QV-F0065","HTH","HHT",F(1,3)),
    ("QV-F0173","HTH","HTT",F(1,2)),
]:
    result = pattern_probability(p1,p2)
    record(cid,"Exact suffix-automaton linear equations",result,answer,result == answer)

p = .99
h = -p*log2(p) - (1-p)*log2(1-p)
record("QV-F0018","Check all-heads counterevent and paired extraction cost",
       dict(all_heads=p**100,mean_von_neumann=1/(p*(1-p)),entropy=h,
            asymptotic_entropy_lower_bound=1/h),
       "All-heads has positive probability; cannot guarantee six fair bits",
       p**100 > .36,
       "99-head type has 100 strings: accepting 64 gives six fair bits only with acceptance probability .64 conditional on that type.")

counts = Counter(sum(f[i] == i for i in range(3)) for f in product(range(3),repeat=3))
target = {k: comb(3,k)*2**(3-k) for k in range(4)}
perms = list(permutations(range(5)))
joint = F(sum(p[0] == 0 and p[1] == 1 for p in perms),len(perms))
cov = joint - F(1,25)
record("QV-F0057","Enumerate all 27 functions and 120 permutations",
       dict(function_counts=dict(counts),permutation_indicator_covariance=str(cov)),
       dict(function_counts=target,permutation_indicator_covariance=str(F(1,100))),
       dict(counts)==target and cov==F(1,100))

deranged = sum(all(p[i] != i for i in range(5)) for p in perms)
record("QV-F0067","Enumerate 5! permutations",F(deranged,120),F(11,30),deranged==44)
fp = F(sum(p[0]==0 and p[1]!=1 for p in perms),120)
record("QV-F0148","Enumerate 5! permutations to check general formula",fp,F(3,20),fp==F(3,20))

for rates in [(2,1),(12,11)]:
    a,b = rates
    assert (skellam.sf(0,a,b) > skellam.cdf(-1,a,b)) == (a>b)
record("QV-F0071","Skellam numerical check plus rate-order proof in notes",
       [(a,b,float(skellam.sf(0,a,b)),float(skellam.cdf(-1,a,b))) for a,b in [(2,1),(12,11)]],
       "A more likely to win every pair when its rate is larger; sums preserve rate order")

ex = F(8,9)*F(1,2)+F(1,9)*5
ex2 = F(8,9)*F(1,4)+F(1,9)*25
record("QV-F0073","Extremal distribution moments and tail mass",
       [str(ex),str(ex2),str(F(1,9))],["1","3","1/9"],ex==1 and ex2==3)

def qhead(d):
    odds = 2.0**d
    return (2*odds+1)/(3*(odds+1))

@lru_cache(None)
def betting_value(a,b,d):
    if a+b==0:return 0.0
    q = qhead(d)
    values = [0.0]
    if a:
        values.append(4*q-2 + q*betting_value(a-1,b,d+1)+(1-q)*betting_value(a-1,b,d-1))
    if b:
        values.append(3-5*q + q*betting_value(a,b-1,d+1)+(1-q)*betting_value(a,b-1,d-1))
    return max(values)

q = F(4,9)
static = F(1400,27)
# Improvement over committing to 100 A bets: after four future tails, stop
# A permanently and use the otherwise-unused positive-EV B bet instead.
event = F(8,9)*F(1,3)**4+F(1,9)*F(2,3)**4
gain = event*(-96*(4*q-2)+(3-5*q))
optimal = betting_value(100,1,3)
record("QV-F0081","Counterhistory, explicit dominating policy, and finite-resource Bellman recursion",
       dict(q_after_four_tails=str(q),A_EV=str(4*q-2),B_EV=str(3-5*q),
            static_100_A=float(static),dominating_policy=float(static+gain),
            optional_stop_DP_value=optimal),
       "Adaptive value strictly exceeds static 100-A policy",
       optimal > float(static+gain) > float(static),
       "Protocol: no free observations; each A/B action consumes one flip and its own remaining count; stop is allowed; risk-neutral expected profit.")

paths = list(product((-1,1),repeat=10))
valid=0
for path in paths:
    s=5;survive=True
    for step in path:
        s+=step
        if s in (0,10):survive=False;break
    valid += bool(survive and s==5)
record("QV-F0082","Enumerate all 1024 ten-step paths",F(valid,1024),F(125,512),valid==250)

pd = np.array([1.])
for _ in range(100):pd=np.convolve(pd,np.r_[0.,np.full(6,1/6)])
threshold = np.arange(len(pd))-1
exact_p = float(np.dot(pd,binom.cdf(threshold,600,.5)))
record("QV-F0083","Finite convolution plus exact binomial CDF (floating precision)",
       dict(finite_probability=exact_p,CLT_uncorrected=float(norm.cdf(50/sqrt(1325/3))),
            CLT_continuity_corrected=float(norm.cdf(49.5/sqrt(1325/3)))),
       "Finite probability around .9908; Gaussian result is approximate",
       0.990 < exact_p < .992)

distinct = sum(len(set(x))==4 for x in product(range(6),repeat=6))
record("QV-F0085","Enumerate all 6^6 dice sequences",F(distinct,6**6),F(325,648),F(distinct,6**6)==F(325,648))
multisets=Counter(tuple(sorted(x)) for x in product(range(6),repeat=3))
collision=F(sum(c*c for c in multisets.values()),6**6)
record("QV-F0089","Group 216 ordered rolls by multiset and sum squared masses",collision,F(83,3888),collision==F(83,3888))

best=max((F(r,r+b)+F(50-r,100-r-b))/2 for r in range(51) for b in range(51) if 0<r+b<100)
record("QV-F0090","Exhaust all feasible integer allocations",best,F(74,99),best==F(74,99))

for n in range(4,12):
    triples=list(combinations(range(n),3))
    count=sum(any((a-b)%n in (1,n-1) for a,b in combinations(t,2)) for t in triples)
    assert F(count,len(triples))==F(6*(n-3),(n-1)*(n-2))
record("QV-F0102","Enumerate vertex triples for n=4,...,11","All 8 cases agree","6(n-3)/[(n-1)(n-2)]")

a = sqrt((sqrt(5)-1)/2)
y0=a*a
yslice = (2*quad(lambda y:sqrt(y),0,y0)[0]+2*quad(lambda y:sqrt(1-y*y),y0,1)[0])/pi
xslice = (asin(a)+a**3/3)/pi
record("QV-F0122","Independent vertical and horizontal slice integrals",
       dict(xslice=xslice,yslice=yslice,sqrt_identity=sqrt(1-a*a)),
       "Both ≈.339481626833; sqrt(1-a²)=a²",abs(xslice-yslice)<1e-12 and abs(sqrt(1-a*a)-a*a)<1e-12)

tp=np.zeros((9,9))
for i in range(9):
    r,c=divmod(i,3)
    dest=[3*rr+cc for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)] if 0<=rr<3 and 0<=cc<3]
    for j in dest:tp[i,j]=1/len(dest)
end=np.full(9,1/9)@tp@tp
even_prob=float(end[[1,3,5,7]].sum())
record("QV-F0123","Full telephone-grid transition matrix squared",even_prob,4/9,abs(even_prob-4/9)<1e-14)

import random
rng=random.Random(1)
draws=[]
for _ in range(20000):
    while True:
        num=5*(rng.randint(1,5)-1)+(rng.randint(1,5)-1)
        if num<21:
            draws.append(num%7+1);break
mean=sum(draws)/len(draws)
preimages=Counter(x%7+1 for x in range(21))
record("QV-F0150","Count accepted preimages; execute stated seeded algorithm",
       dict(mean_20000_seed1=mean,accepted_preimages=dict(preimages)),
       "Three preimages per output; seeded mean independently measured",set(preimages.values())=={3})

u=[F(1)]
for n in range(1,101):u.append(sum(u[max(0,n-6):n])/6)
cross=(u[99]+u[100])/6
record("QV-F0170","Exact rational renewal recurrence through level 100",
       dict(probability=float(cross),difference_from_2_over_21=float(cross-F(2,21)),
            exact_numerator=str(cross.numerator),exact_denominator=str(cross.denominator)),
       "Extremely close to, but strictly different from 2/21",cross!=F(2,21))

states=list(product(range(3),range(3),range(2)))
ix={s:i for i,s in enumerate(states)}
mat=[[F(i==j) for j in range(18)] for i in range(18)];rhs=[F(0) for _ in states]
for (a,b,t),i in ix.items():
    if t==0:
        mat[i][ix[(0,b,1)]]-=F(1,2)
        if a==2:rhs[i]+=F(1,2)
        else:mat[i][ix[(a+1,b,1)]]-=F(1,2)
    else:
        mat[i][ix[(a,0,0)]]-=F(1,2)
        if b<2:mat[i][ix[(a,b+1,0)]]-=F(1,2)
ans=solve_fraction(mat,rhs)[ix[(1,0,1)]]
record("QV-F0171","Solve full 18-state chain with exact rational elimination",ans,F(521,913),ans==F(521,913))

bday23=1-F(364,365)**22
record("QV-F0177","Exact fixed-birthday complementary probability",float(bday23),".058571325264..., not .061",.0585<float(bday23)<.0587)
record("QV-F0188","Exact Gaussian tail versus Chebyshev",2*norm.sf(sqrt(2)),"≈.157299 < .5",2*norm.sf(sqrt(2))<.5)

faces=list(product(range(1,7),repeat=3));win=lose=tie=0
for d in range(1,21):
    for f in faces:
        s=sum(f)
        win+=d>s;lose+=d<s;tie+=d==s
record("QV-F0220","Enumerate all 20·6^3 one-round outcomes",[win,lose,tie],"Equal strict-win and strict-loss counts",win==lose and F(win,win+lose)==F(1,2))

rho=.85
bvn,quad_error=quad(lambda z:norm.cdf((rho*z-1)/sqrt(1-rho*rho))*norm.pdf(z),-12,0,epsabs=1e-14)
record("QV-F0285","One-dimensional conditional-normal numerical integration",bvn,"≈.00263684426370",abs(bvn-.0026368442636968644)<1e-12,dict(quad_error=quad_error))

inc=sum(a<b<c for a,b,c in product(range(1,7),repeat=3))
record("QV-F0451","Enumerate 216 ordered rolls",F(inc,216),F(5,54),F(inc,216)==F(5,54))
q=0.0
for _ in range(200):q=(1+q+q*q+q*q*q)/4
record("QV-F0452","PGF iteration from zero and polynomial residual",q,sqrt(2)-1,abs(q-(sqrt(2)-1))<1e-14)
aces=sum(len({p//13 for p in pos})==4 for pos in combinations(range(52),4))
ace_probability=F(aces,comb(52,4))
record("QV-F0453","Enumerate all C(52,4) sets of ace positions",ace_probability,F(2197,20825),ace_probability==F(2197,20825))

def unique_suffix_probability(n):
    counts=[1,0,0,0,0,0,0]
    for _ in range(n):
        nxt=[0]*7
        nxt[6]=6*counts[6]
        for r in range(6):
            for new_length in range(1,r+1):nxt[new_length]+=counts[r]
            nxt[r+1]+=(6-r)*counts[r]
        counts=nxt
    return F(counts[6],6**n)

# Compare the compressed longest-distinct-suffix chain with the full ordered
# last-five sequence DP; they have different state representations.
dist={():1};absorbed=0
for n in range(1,11):
    nxt=Counter();absorbed*=6
    for state,count in dist.items():
        for face in range(6):
            seq=state+(face,)
            if len(seq)==6 and len(set(seq))==6:absorbed+=count
            else:nxt[seq[-5:]]+=count
    dist=nxt
    assert F(absorbed,6**n)==unique_suffix_probability(n)
assert unique_suffix_probability(6)==F(5,324)
record('QV-F0249','Cross-check exact 7-state suffix chain against ordered-last-five DP for n1..10',
       dict(n6=str(unique_suffix_probability(6)),n50=float(unique_suffix_probability(50))),
       '7-state and full ordered-state probabilities agree',True,
       'Original page recovered from live ID1024. The longest distinct suffix is sufficient; adjacent window indicators are dependent.')

(HERE/'probability_verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(json.dumps(dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),
                     verified_catalog_entries=len({c['catalog_id'] for c in checks}),
                     sequential_betting_DP_value=optimal,rand7_seeded_mean=mean),ensure_ascii=False))
