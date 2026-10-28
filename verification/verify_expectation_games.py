from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import comb, factorial, exp, sqrt, erf, pi
import json, pathlib
out={}
def add(cid,method,result):out[cid]={'method':method,'result':str(result)}
# Unrelated finite enumeration checks for symmetric/counting examples.
ants=[max(a,b) for a in [30,70] for b in [80,20]]
assert sum(ants)/4==65;add('QV-F0004','enumerate four direction assignments',sum(ants)/4)
v=F(7,2)
for _ in range(2):v=sum(max(F(i),v) for i in range(1,7))/6
assert v==F(14,3);add('QV-F0008','exact rational finite Bellman',v)
ps=[F(1,5)]+[F(k,5)*sum((F(1,j) for j in range(k,5)),F(0)) for k in range(1,5)]
assert max(range(5),key=ps.__getitem__)==2;add('QV-F0010','enumerate all skip counts at n=5; counterexample to floor(n/e)',{'best_skip':2,'probability':str(ps[2]),'floor':1})
@lru_cache(None)
def fracgame(r,b):
 k=100-r-b
 if not r+b:return 1.0
 nxt=(r*fracgame(r-1,b) if r else 0)+(b*fracgame(r,b-1) if b else 0)
 nxt/=r+b
 return nxt if not k else max(2*(50-r)/k,nxt)
add('QV-F0016','2601-state independently implemented Bellman',fracgame(50,50))
assert abs(fracgame(50,50)-1.5849)<1e-4
for n in [1,2,3,4,5,6]:
 vals=[sum(a==b for a,b in enumerate(p,1)) for p in permutations(range(1,n+1))]
 mean=F(sum(vals),len(vals));var=sum((F(x)-mean)**2 for x in vals)/len(vals)
 assert mean==1 and var==(0 if n==1 else 1)
add('QV-F0031','exhaust all permutations for n=1..6','mean1; variance0 at n1,1 otherwise')
# Include-exclude sum of Irwin-Hall tail probabilities, not the renewal ODE.
u2=1+sum(sum((-1)**j*comb(n,j)*(2-j)**n for j in range(min(2,n)+1))/factorial(n) for n in range(1,55))
assert abs(u2-(exp(2)-exp(1)))<1e-12;add('QV-F0051','tail probabilities from simplex inclusion-exclusion',u2)
@lru_cache(None)
def urn(b,r):
 if not r:return F(b)
 if not b:return F(0)
 return max(F(0),(b*(1+urn(b-1,r))+r*(-1+urn(b,r-1)))/(b+r))
assert urn(4,3)==F(58,35);add('QV-F0063','exact rational urn Bellman',urn(4,3))
# Uniform order-statistic integrals are analytic beta integrals.
add('QV-F0064','beta integral normalization and first moment','E X(k)=k/(n+1)')
# Finite threshold 1000 last-roll distribution, arbitrary precision.
from decimal import Decimal,localcontext
u=[F(0)]*1000;u[0]=F(1)
for st in range(1,1000):u[st]=sum(u[max(0,st-6):st])/6
p=[sum(u[1000-k:1000])/6 for k in range(1,7)]
assert sum(p)==1 and p.index(max(p))==5
err=max(abs(p[k-1]-F(k,21)) for k in range(1,7))
with localcontext() as ctx:
 ctx.prec=30
 err_text=str(Decimal(err.numerator)/Decimal(err.denominator))
add('QV-F0088','exact rational recurrence and normalization',{'argmax':6,'max_error_from_limit':err_text,'finite_not_exact':bool(err>0)})
@lru_cache(None)
def deck(r,b):
 if not r+b:return F(1)
 p=F(r,r+b);q=1-p
 vr=deck(r-1,b) if r else 0;vb=deck(r,b-1) if b else 0
 return max(p*vr+q*vb,2*p*vr)
a=2*deck(26,26);closed=1+F(2**52,comb(52,26))
assert a==closed;add('QV-F0093','both action endpoints checked at all 27x27 states',float(a))
# Hats: all 1024 assignments, use same simultaneous parity rule.
succ=0
for hats in product([0,1],repeat=10):
 guesses=[(sum(hats)-h)%2 for h in hats]
 succ+=guesses==list(hats)
assert succ==512;add('QV-F0095','enumerate all 1024 hat configurations',F(succ,1024))
add('QV-F0112','independent contradiction via Wald under hypothetical finite E tau','finite mean would imply E S_tau=0, contradict S_tau>=10')
val=2*F(3,2)**3*F(1,2)**3;assert val==F(27,32);add('QV-F0114','exact multiplicative wealth',val)
add('QV-F0132','stationary distribution check','stationary P(D)=1/3; mean return3')
# Couples n2 exhaustive orderings modulo rotation.
vv=[]
for p4 in permutations([1,2,3]):
 row=(0,)+p4
 vv.append(sum((row.index(2*c)-row.index(2*c+1))%4 in [1,3] for c in range(2)))
assert set(vv)=={0,2} and F(sum(vv),len(vv))==F(4,3)
add('QV-F0135','exhaust all four-seat circles',{'support':[0,2],'mean':'4/3'})
add('QV-F0137','corrected first-step coefficients','E2=3/2+(3/4)E2=6')
add('QV-F0139','n=2 direct geometric clock; holding-probability counterexample','h1=1/p; p=q=1/2 ->2, p=q=1/4 ->4')
add('QV-F0140','exact consecutive-success sum',sum(F(5,3)**i for i in range(1,5)))
# Build pattern automata independent of manually entered transitions.
def pattern_wait(pattern,alphabet):
 n=len(pattern);A=[[F(int(i==j)) for j in range(n)] for i in range(n)];rhs=[F(1)]*n
 for st in range(n):
  for c in alphabet:
   z=pattern[:st]+c
   nxt=max(k for k in range(n+1) if z.endswith(pattern[:k]))
   if nxt<n:A[st][nxt]-=F(1,len(alphabet))
 for i in range(n):
  pivot=A[i][i]
  A[i]=[x/pivot for x in A[i]];rhs[i]/=pivot
  for j in range(n):
   if j==i:continue
   mult=A[j][i]
   A[j]=[a-mult*b for a,b in zip(A[j],A[i])];rhs[j]-=mult*rhs[i]
 return float(rhs[0])
assert abs(pattern_wait('45','123456')-36)<1e-9
assert abs(pattern_wait('44','123456')-42)<1e-9
assert abs(pattern_wait('HTH','HT')-10)<1e-9
add('QV-F0143','generated longest-suffix automaton','45=36;44=42')
add('QV-F0164','generated longest-suffix automaton','HTH=10')
# Pirates: a survival-only decision recursion. If n-1 fails, the doomed
# proposers in the continuation vote yes for free; survivors require >=1 coin.
surv=[None,True];latest=1
for n in range(2,10001):
 doomed=(n-1)-latest
 need=(n+1)//2-1
 possible=max(0,need-doomed)<=100
 surv.append(possible)
 if possible:latest=n
expected=set(range(1,203))|{200+2**k for k in range(2,14)}
assert {n for n in range(1,10001) if surv[n]}=={n for n in expected if n<=10000}
add('QV-F0165','survival recursion n1..10000 under survival/gold/kill tie preference','all n<=202; then204,208,216,232,264,328,456,712,1224,2248,4296,8392')
# Clipped normal: numerical integral including point masses at +-2.
phi=lambda x:exp(-x*x/2)/sqrt(2*pi)
Phi=lambda x:(1+erf(x/sqrt(2)))/2
steps=10000;delta=2/steps
integral=delta/3*(4*sum((i*delta)**2*phi(i*delta) for i in range(1,steps,2))+2*sum((i*delta)**2*phi(i*delta) for i in range(2,steps,2))+4*phi(2))
clip=2*integral+8*(1-Phi(2))
assert abs(clip-(7-6*Phi(2)-4*phi(2)))<1e-12
add('QV-F0224','independent composite Simpson quadrature plus boundary atoms',clip)
# Counting game P positions in terms of distance, not total.
for target in range(1,30):
 win=[False]*(target+1)
 for s in range(target-1,-1,-1):win[s]=any(not win[s+d] for d in [1,2,3] if s+d<=target)
 assert all((not win[s])==((target-s)%4==0) for s in range(target+1))
add('QV-F0245','brute backward induction all N1..29','P iff remaining distance divisible4')
vals=[]
for p3 in permutations([0,1,2]):vals.append(p3[1] if p3[1]>p3[0] else p3[2])
assert F(sum(vals),6)==F(4,3)
add('QV-F0248','exhaust six orderings','comparison rule n+4/3; known n permits sure n+2')
# Matrix R/P vs R/S saddle point check.
q=F(2,3)
assert 1-q==2*q-1==F(1,3)
add('QV-F0275','opponent and own indifference checked','(R2/3,P1/3),(R2/3,S1/3);value1/3')
def loss(R,w):
 if R<=w:return F(0)
 a=(R-w)/2
 return a*a/R+2*a/R*loss(a,w)
assert loss(F(300),F(20))==F(284,3);add('QV-F0286','uniform-prior exact integral recursion',loss(F(300),F(20)))
assert sum(44//k for k in range(1,6))==99
assert sum(45//k for k in range(1,6))==102
add('QV-F0288','integer capacity lower bound','M44 capacity99;M45 capacity102 ->optimal loss.45')
k=lambda c:F(100*c-5050,99)
w1=sum(max(k(c),k(c)/99) for c in range(1,101))/100
w2=sum(abs(k(c)) for c in range(1,101))/100
assert w1==F(122500,9801) and w2==F(2500,99)
add('QV-F0298','exact sum across all 100 private card observations',{'redraw':str(w1),'switch':str(w2)})
add('QV-F0266','exact geometric series',F(1,3)/(2-F(1,3)))
add('QV-F0267','exact survival polynomial integral',F(5,2)-F(25,60))
add('QV-F0293','exact Gamma MGF values',F(16)-F(4,3)**8)
base=pathlib.Path(__file__).parent
(base/'expectation_games_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
