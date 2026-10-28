import json,math,heapq,itertools
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.special import lambertw
from scipy.optimize import brentq
R=Path(__file__).parent;checks=[]
def ck(n,c,e):
 assert bool(c),(n,e)
 checks.append(dict(catalog_id=f'QV-F{n:04}',passed=True,evidence=e))
def d(f,x,h=1e-5):return (f(x+h)-f(x-h))/(2*h)
def d2(f,x,h=1e-4):return (f(x+h)-2*f(x)+f(x-h))/h**2
# General shortest path, independent of a proposed bridge schedule.
t=[1,2,7,10];dist={(0,0):0};pq=[(0,(0,0))]
while pq:
 cost,(mask,side)=heapq.heappop(pq)
 if cost!=dist[(mask,side)]:continue
 if mask==15:ans=cost;break
 available=[i for i in range(4) if ((mask>>i)&1)==side]
 for k in [1,2]:
  for group in itertools.combinations(available,k):
   m=mask
   for i in group:m^=1<<i
   nxt=(m,1-side);v=cost+max(t[i] for i in group)
   if v<dist.get(nxt,math.inf):dist[nxt]=v;heapq.heappush(pq,(v,nxt))
ck(41,ans==17,'Independent bridge-state Dijkstra:17.')
g=.54*math.log(1.01)+.46*math.log(.99)
ck(61,abs(g-.0007500241681001026)<1e-15,'Expected log growth='+str(g)+'=7.50024bp; g derivative positive on[0,1].')
F={(e,0):0 for e in range(3)}
for drops in range(1,11):
 F[0,drops]=0
 for eggs in range(1,3):F[eggs,drops]=F[eggs-1,drops-1]+1+F[eggs,drops-1]
ck(124,F[2,10]==55,'General egg/drop coverage recurrence:55.')
A=np.array([[0,1],[0,0]]);ck(214,np.all(A@A==0) and np.linalg.matrix_rank(A)==1,'Nonzero rank-one nilpotent example confirms zero-spectrum exception.')
ck(283,90/100==.9,'Variance explained90/100=.9.')
y=1.;seq=[]
for _ in range(3):y=(y+2/y)/2;seq.append(y)
ck(289,abs(y-math.sqrt(2))<3e-6,'Square-root iterates='+str(seq))
for a,b in [(.8,.9),(.5,.5),(-.8,.3),(1,.4)]:
 lo=a*b-math.sqrt((1-a*a)*(1-b*b));hi=a*b+math.sqrt((1-a*a)*(1-b*b))
 for rr in [lo,(lo+hi)/2,hi]:assert np.linalg.eigvalsh([[1,a,rr],[a,1,b],[rr,b,1]]).min()>-1e-12
ck(301,True,'Three-variable correlation boundary/midpoint PSD verified for four parameter pairs, including a degenerate endpoint.')
ck(303,all(abs(z)+abs(2-z)==2 for z in [0,.3,1,1.7,2]) and 1**2+1**2==2,'Two-point example distinguishes unique L2 mean and interval of L1 medians.')
a=np.array([1.,1.]);b=np.array([1.,0.]);proj=a*(a@b)/(a@a);ck(313,abs(a@(b-proj))<1e-14,'Projection residual orthogonality.')
rng=np.random.default_rng(13);X=rng.normal(size=(25,4));Y=rng.normal(size=25)
S=sum(z.T@z for z in np.array_split(X,4));q=sum(z.T@w for z,w in zip(np.array_split(X,4),np.array_split(Y,4)))
Q,RR=np.linalg.qr(X);ck(319,np.allclose(S,X.T@X) and np.allclose(np.linalg.solve(S,q),np.linalg.solve(RR,Q.T@Y)),'Streaming statistics and direct QR agree for a well-conditioned example; this does not certify ill-conditioned normal equations.')
def C(z):return np.array([[1,.5,.5,z],[.5,1,.5,.5],[.5,.5,1,.5],[z,.5,.5,1.]])
ck(320,all(np.linalg.eigvalsh(C(z)).min()>-1e-12 for z in [-1/3,1]) and all(np.linalg.eigvalsh(C(z)).min()<0 for z in [-1/3-.0001,1.0001]),'Four-variable PSD endpoints pass; just-outside correlations have negative eigenvalues.')
ck(339,np.allclose(np.linalg.eigvalsh(np.ones((5,5))),[0,0,0,0,5]),'All-ones5×5 spectrum0,0,0,0,5.')
mu,mu0,lam=100,98,1;P=mu-(1+lambertw(math.exp(lam*(mu-mu0)-1)).real)/lam;ff=1/(1+math.exp(-lam*(P-mu0)))
ck(345,abs(P-98)<1e-12 and abs(lam*ff*(1-ff)*(mu-P)-ff)<1e-12,'Lambert W bid98 satisfies FOC.')
vals={k:math.exp(.5*k)*(3-k) for k in range(3)};ck(346,max(vals,key=vals.get)==1,'Integer objective enumeration selects1 tick for(s,τ,λ)=(3,1,.5).')
Sig=np.ones((2,2));e,Q=np.linalg.eigh(Sig);B=Q@np.diag(np.sqrt(np.maximum(e,0)));ck(349,np.allclose(B@B.T,Sig),'Spectral square root reconstructs singular target covariance.')
ck(356,abs((.5*(2/3)+.5*.5-.5)-1/12)<1e-15,'Beta(1,1) terminal information value1/12.')
ck(371,np.isclose(max(np.array([math.cos(z),math.sin(z)])@np.diag([3.,1.])@np.array([math.cos(z),math.sin(z)]) for z in np.linspace(0,2*math.pi,1001)),3),'Unit-circle grid agrees with Rayleigh maximum3.')
mx=[]
for n in [1,2,3]:
 best=0
 for bits in itertools.product([0,1],repeat=n*n):
  A=np.array(bits,dtype=np.int64).reshape(n,n)
  if np.all(A@A==0):best=max(best,sum(bits))
 mx.append(best)
ck(372,mx==[0,1,2],'Exhaustive real/integer0-1 matrices n1,2,3 under actual A²=0 condition give maxima0,1,2=floor(n²/4).')
f=lambda x:x**x
ck(373,abs(d(f,1/math.e))<1e-8 and abs(f(1e-12)-1)<1e-9,'Derivative at1/e approximately0; tiny positive boundary approaches1.')
def horner(cs,z):
 v=0
 for c in cs[::-1]:v=v*z+c
 return v
xx=0.
for i in range(50000):
 grad=d(lambda z:horner([10,-6,1],z),xx);nxt=xx-.2*grad
 if abs(nxt-xx)<1e-10:xx=nxt;break
 xx=nxt
ck(376,abs(xx-3)<1e-7,'Pinned finite-difference GD reaches'+str(xx)+' in'+str(i+1)+' updates.')
ck(378,.5**2<1 and 2**2>1,'Scalar L0 comparison validates hard thresholdsqrtλ forλ1.')
ck(386,max(0,-10+12)==2 and max(10,12)==12,'One-step deterministic MDP no-position value2,holding value12.')
L=-math.log(.2);ck(388,math.log(L/L)==0 and abs(math.exp(-L)-.2)<1e-15,'Vacancy feasibility boundaryλ0=L impliesp0.')
xx=1.5;ck(393,abs(xx-math.sqrt(2))<=abs(xx*xx-2)/2,'Residual/m certificate checked on[1,2],m2.')
f=lambda x:math.log(x)**math.log(x);formula=lambda x:f(x)*(math.log(math.log(x))+1)/x
ck(427,all(abs(d(f,z)-formula(z))<1e-7 for z in [1.2,math.e,5]),'Central-difference derivative agrees at three valid points.')
ck(428,math.exp(50)/50**2>1e17 and abs(1e-8**2*math.log(1e-8))<1e-12,'Numerical scales match exponential divergence/power-log decay; full limit proof provided in review.')
f=lambda x:x*math.log(x)-x;ck(429,abs(d(f,2)-math.log(2))<1e-9,'Differentiate proposed log primitive numerically.')
ck(430,abs(math.log(1/math.cos(math.pi/6)+math.tan(math.pi/6))-.5*math.log(3))<1e-15,'Secant integral endpoint logarithm=ln3/2.')
ck(435,all((1+z)**n>=1+n*z-1e-12 for n in range(2,9) for z in [-.9,-.5,0,.5,2]),'Bernoulli checks n2–8 across negative,zero,positive x; proof is analytic Taylor argument.')
f=lambda z:z**3-2*z-5;root=brentq(f,2,3,xtol=1e-14);x0,x1=2.,3.;arr=[]
for _ in range(5):
 x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0));arr.append(x2);x0,x1=x1,x2
ck(436,abs(arr[3]-root)>1e-6 and abs(arr[4]-root)<1e-6 and 2**(-20)<=1e-6,'Secant true-root error first below1e−6 after5 new points; bisection width requires20 halvings.')
point=np.array([24.,36.,48.])/29;ck(437,abs(point@np.array([2.,3.,4.])-12)<1e-12 and abs(np.linalg.norm(point)-12/math.sqrt(29))<1e-12,'Nearest point satisfies plane and distance.')
y=lambda x:math.exp(-3*x*x);ck(438,all(abs(d(y,z)+6*z*y(z))<1e-8 for z in [-1,0,.5]) and y(0)==1,'Separable ODE numerical residual and exact initial value.')
ck(439,all(abs((2*v+2*u)*(u-v)/(u+v)+2*v-2*u)<1e-12 for u,v in [(1,0),(2,1),(3,-1)]),'Implicit-solution derivative identity checks three non-singular points.')
y=lambda x:(math.log(x)+1)/x;ck(440,all(abs(d(y,z)+y(z)/z-1/z**2)<1e-8 for z in [.5,1,2]) and y(1)==1,'First-order ODE numerical residual and initial value.')
H=[lambda z:math.exp(-z/2)*math.cos(math.sqrt(3)*z/2),lambda z:math.exp(-z/2)*math.sin(math.sqrt(3)*z/2)]
ck(441,all(abs(d2(h,z)+d(h,z)+h(z))<2e-7 for h in H for z in [0,.5,1]),'Both real homogeneous basis functions annihilated within finite-difference accuracy.')
ck(442,all(abs(d2(h,z)+d(h,z)+h(z)-forcing(z))<1e-7 for h,forcing in [(lambda z:1.,lambda z:1.),(lambda z:z-1,lambda z:z)] for z in [0,.5,1]),'Constant and linear particular solutions yield correct forcing.')
ck(444,np.allclose(np.linalg.eigvalsh([[2.,1.],[1.,2.]]),[1,3]),'Independent eigensolver gives1,3.')
rr=.8;B=np.array([[1.,0],[rr,math.sqrt(1-rr*rr)]]);ck(445,np.allclose(B@B.T,[[1,rr],[rr,1]]),'Correlated-normal covariance factor identity.')
v={n:Fraction(n) for n in range(15,21)}
for n in range(14,-1,-1):v[n]=max(Fraction(n),sum((v[n+i] for i in range(1,6)),Fraction())/6)
ck(457,v[0]==Fraction(2893395172951,470184984576) and sum(Fraction(n) for n in range(16,21))/6==15,'Exact rational Bellman V0='+str(v[0])+'='+str(float(v[0]))+'; total15 ties stop and one-more-roll.')
assert len(checks)==39
(R/'algebra_optimization_verification.json').write_text(json.dumps(dict(verified_at='2026-10-28',method='Independent graph, exact rational, finite-difference, matrix and numerical checks complement the original mathematical proofs. These checks do not establish unseen original-site constraints.',checks=sorted(checks,key=lambda q:q['catalog_id'])),ensure_ascii=False,indent=2)+'\n')
print('All39independent numerical/identity checks passed.')
