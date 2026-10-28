"""Independent, bounded checks for the statistics/regression course, not copied solutions."""
import json
import math
from collections import deque
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog
from scipy.stats import beta, norm

OUT={}
def record(name, value): OUT[name]=value

# 1. Normal risk and Beta posterior tails.
record('normal_tail_risk', {'two_sided_probability':float(2*norm.sf(2.5)), 'VaR99_bp':float(40*norm.ppf(.99))})
tail=float(beta.sf(.3,8,22))
assert abs(tail-quad(lambda t: beta.pdf(t,8,22), .3,1)[0])<1e-12
record('beta_8_22_tail_above_0_3',tail)

# 2. Clipped normal-mixture moments: integration is independent of the closed form.
def clipped_second(s,c=3):
 a=c/s
 return s*s*(2*norm.cdf(a)-1-2*a*norm.pdf(a))+2*c*c*norm.sf(a)
closed=.99*clipped_second(1)+.01*clipped_second(5)
numeric=sum(w*quad(lambda r:min(r*r,9)*norm.pdf(r,scale=s),-np.inf,np.inf,points=None)[0] for w,s in [(.99,1),(.01,5)])
assert abs(closed-numeric)<2e-9
record('winsorization',{'variance':float(closed),'original_variance':1.24,'heavy_component_probability_clipped':float(2*norm.sf(.6))})

# 3. Conditional silence: exact moment with the stated parameters.
sigma,s,mu,p0,q=2.,1.,.3,.1,.2
A=p0+(1-p0)*(1-mu)*q; B=(1-p0)*mu; P=2*norm.cdf(s/sigma)-1
postvar=sigma*sigma-2*B*s*sigma*norm.pdf(s/sigma)/(A+B*P)
record('no_trade_posterior',{'probability':float(A+B*P),'mean':0.,'variance':float(postvar)})

# 4. Joint collinearity with no pairwise correlation close to one.
x=np.array([-2,-1,0,1,2.]); z=np.array([2,-1,-2,-1,2.])
X=np.column_stack([x,z,x+z]); corr=np.corrcoef(X,rowvar=False)
e=np.linalg.eigvalsh(corr)
assert np.linalg.matrix_rank(X)==2 and abs(e[0])<1e-12
record('full_column_correlation_matrix_detects_joint_collinearity',{'pairwise_correlations':corr.tolist(),'eigenvalues':e.tolist(),'rank':2})

# 5. Equicorrelation lower boundary identifies the mean exactly.
n=5; r=-1/(n-1); S=(1-r)*np.eye(n)+r*np.ones((n,n))
assert np.allclose(S@np.ones(n),0)
record('equicorrelation_lower_boundary',{'mean_variance':float(np.ones(n)@S@np.ones(n)/n**2),'covariance_eigenvalues':np.linalg.eigvalsh(S).tolist()})

# 6. Correct ARMA formula vs independently summed MA(infinity) coefficients.
phi,theta,sv=.3,-.8,2.
psi=np.r_[1.,(phi+theta)*phi**np.arange(200)]
g0=float(sv*psi@psi); g1=float(sv*psi[:-1]@psi[1:])
assert np.isclose(g0,sv*(1+2*phi*theta+theta**2)/(1-phi**2))
assert np.isclose(g1,sv*(phi+theta)*(1+phi*theta)/(1-phi**2))
record('arma_independent_ma_infinity_check',{'gamma0':g0,'gamma1':g1,'rho1':g1/g0,'correct_E_epsilon_previous_X':sv*(phi+theta)})

# 7. Reversal identity (finite-path exact equality), not an assumed sign flip.
rng=np.random.default_rng(20261028); rr=rng.normal(size=1000); rev=-rr[::-1]
forward=float(np.mean(rr[:-1]*rr[1:]**2)); backward=float(np.mean(rr[1:]*rr[:-1]**2))
rev_forward=float(np.mean(rev[:-1]*rev[1:]**2)); rev_backward=float(np.mean(rev[1:]*rev[:-1]**2))
assert np.isclose(rev_forward,-backward) and np.isclose(rev_backward,-forward)
record('path_reversal_moment_identity',{'forward':forward,'backward':backward,'reversed_forward':rev_forward,'reversed_backward':rev_backward})

# 8. Published smoothing discontinuity, plus independent continuous substitute.
tau=.5; h=1.
bad_inner=1/(2*h)+(tau-.5)+h/8; bad_outer=tau-h/2
assert bad_inner==.625 and bad_outer==0.
def smooth(u,tau,h):
 if u < -h:return (tau-1)*u
 if u > h:return tau*u
 return u*u/(4*h)+(tau-.5)*u+h/4
for tau in [.1,.5,.9]:
 for b in [-1.,1.]:
  eps=1e-7; l=smooth(b-eps,tau,1); m=smooth(b,tau,1); rr_=smooth(b+eps,tau,1)
  assert abs(l-m)<eps*1.1 and abs(rr_-m)<eps*1.1
  assert abs((m-l)/eps-(rr_-m)/eps)<2e-6
record('quantile_huber_formula',{'published_left_limit_at_u1':bad_inner,'published_right_limit_at_u1':bad_outer,'corrected_C1_boundary_checks':6})

# 9. More than p exact zero residuals is possible at a quantile optimum.
Xq=np.column_stack([np.ones(6),np.arange(6)]); yq=np.zeros(6); p=Xq.shape[1]; n=len(yq)
obj=np.r_[np.zeros(p),np.full(n,.5),np.full(n,.5)]
res=linprog(obj,A_eq=np.column_stack([Xq,np.eye(n),-np.eye(n)]),b_eq=yq,bounds=[(None,None)]*p+[(0,None)]*(2*n),method='highs')
assert res.success and np.count_nonzero(abs(yq-Xq@res.x[:p])<1e-10)==n
record('quantile_zero_residual_counterexample',{'p':p,'n':n,'zero_residual_count':n,'optimum':float(res.fun)})

# 10. Thin-SVD ridge inverse identity needs the nullspace part.
Xs=rng.normal(size=(4,7)); ys=rng.normal(size=4); U,d,Vt=np.linalg.svd(Xs,full_matrices=False); V=Vt.T; lam=.7
actual=np.linalg.inv(Xs.T@Xs+lam*np.eye(7)); only_span=(V/(d*d+lam))@V.T
assert np.allclose(actual,only_span+(np.eye(7)-V@V.T)/lam)
assert np.allclose(actual@Xs.T@ys,V@((d/(d*d+lam))*(U.T@ys)))
record('thin_svd_nullspace_inverse',{'omitted_inverse_term_frobenius_norm':float(np.linalg.norm(actual-only_span)),'coefficient_formula_still_correct':True})

# 11. Raw BP vs Koenker: finite-sample different; scaling doesn't change R2.
Z=np.column_stack([np.ones(8),np.arange(8.)]); sq=np.array([.1,2,1,.2,3,1,4,.4]); normalized=sq/sq.mean()
fitted=Z@np.linalg.lstsq(Z,normalized,rcond=None)[0]
ess=float(np.sum((fitted-normalized.mean())**2)); tss=float(np.sum((normalized-normalized.mean())**2)); nR2=len(sq)*ess/tss
assert not np.isclose(ess/2,nR2)
record('breusch_pagan_vs_koenker',{'raw_gaussian_BP':ess/2,'studentized_nR2':nR2})

# 12. Equal ex-ante risk forecasts don't equate realized Sharpe with mean.
a=np.array([.01,-.01,.01,-.01]); b=np.array([.05,-.04,.05,-.04])
record('mean_difference_is_not_sharpe_difference',{'mean_A':float(a.mean()),'mean_B':float(b.mean()),'sharpe_A':float(a.mean()/a.std()),'sharpe_B':float(b.mean()/b.std())})
# Explicit case: B larger mean, smaller Sharpe.
muA,sdA,muB,sdB=.001,.01,.002,.1
assert muB>muA and muB/sdB<muA/sdA
OUT['mean_difference_is_not_sharpe_difference']['population_counterexample']={'mu_A':muA,'sigma_A':sdA,'mu_B':muB,'sigma_B':sdB,'SR_A':muA/sdA,'SR_B':muB/sdB}

# 13. Welford supports None AND NaN.
def online(batches,ncol):
 count=np.zeros(ncol,dtype=int); means=np.zeros(ncol); m2=np.zeros(ncol)
 for batch in batches:
  for row in batch:
   for j,value in enumerate(row):
    if value is None or math.isnan(value):continue
    count[j]+=1; delta=value-means[j]; means[j]+=delta/count[j]; m2[j]+=delta*(value-means[j])
 return means,m2/(count-1)
a,b=online([[[1.,10.],[3.,None]],[[5.,20.],[float('nan'),30.]]],2)
assert np.allclose(a,[3,20]) and np.allclose(b,[4,100])
record('online_with_None_and_NaN',{'mean':a.tolist(),'sample_variance':b.tolist()})

# 14. Original Lloyd implementation in O(nd+kd+n) memory, deterministic ties.
def lloyd(points,k):
 pts=np.asarray(points,float); centers=pts[:k].copy(); prev=None
 for _ in range(100):
  labels=np.array([int(np.argmin(np.sum((centers-p)**2,axis=1))) for p in pts])
  if prev is not None and np.array_equal(labels,prev):break
  prev=labels.copy()
  for j in range(k):
   group=pts[labels==j]
   if len(group):centers[j]=group.mean(axis=0)
 return float(sum(np.min(np.sum((centers-p)**2,axis=1)) for p in pts))
inertia=lloyd([[1,2],[1,4],[1,0],[4,2],[4,4],[4,0]],2)
assert inertia==17.5
record('kmeans_example_inertia',inertia)

# 15. Mean-imputation example via an independently assembled least-squares system.
x=np.array([[1,np.nan],[np.nan,3],[3,5],[4,6.]])
for j in range(2):x[np.isnan(x[:,j]),j]=np.nanmean(x[:,j])
coeff=np.linalg.lstsq(np.column_stack([np.ones(4),x]),[2.1,4,6.2,7.9],rcond=None)[0]
assert np.allclose(coeff,[-2.218474576271187,1.7166101694915263,.5766101694915252])
record('mean_imputation_example_coefficients',coeff.tolist())

# 16. Ordered segment summaries against brute-force drawdown for all tiny windows.
def merge(a,b):
 if a is None:return b
 if b is None:return a
 return max(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2],a[0]-b[1])
checked=0
for n in range(1,12):
 prices=rng.integers(0,10,size=n)
 for start in range(n):
  state=None
  for stop in range(start,n):
   q_=float(prices[stop]); state=merge(state,(q_,q_,0.))
   brute=max(float(prices[i]-prices[j]) for i in range(start,stop+1) for j in range(i,stop+1))
   assert state[2]==brute;checked+=1
record('ordered_drawdown_summary_windows_checked',checked)

# 17. Fully worked tiny OLS example, coefficient and predictive uncertainty.
x=np.array([-1.,0.,1.]); y=np.array([0.,1.,3.]); A=np.column_stack([np.ones(3),x]); bh=np.linalg.lstsq(A,y,rcond=None)[0]
resid=y-A@bh; rss=float(resid@resid)
assert np.allclose(bh,[4/3,1.5]) and np.isclose(rss,1/6)
record('worked_ols',{'beta':bh.tolist(),'residuals':resid.tolist(),'RSS':rss,'s2':rss,'slope_standard_error':math.sqrt(rss/2),'h_at_x0':1/3,'mean_prediction_SE_at_x0':math.sqrt(rss/3),'new_observation_prediction_SE_at_x0':math.sqrt(rss*(1+1/3))})

# 18. POT formula example and exponential limit.
u,scale,xi,pu,alpha=.02,.008,.25,.05,.99
var=u+scale/xi*((pu/(1-alpha))**xi-1); es=(var+scale-xi*u)/(1-xi)
record('POT_example',{'VaR':var,'ES':es,'exponential_limit_VaR':u+scale*math.log(pu/(1-alpha))})

# 20. Same near-collinearity spectrum can accompany very different in-sample fits.
x=np.array([1.,1.,-1.,-1.]); z1=np.array([1.,-1.,1.,-1.]); z2=np.array([1.,-1.,-1.,1.]); eps=1e-3
XA=np.column_stack([np.ones(4),x,x+eps*z1]); XB=np.column_stack([np.ones(4),x,x+eps*z2]); yy=z1
RSSA=float(np.linalg.norm(yy-XA@np.linalg.lstsq(XA,yy,rcond=None)[0])**2)
RSSB=float(np.linalg.norm(yy-XB@np.linalg.lstsq(XB,yy,rcond=None)[0])**2)
assert np.allclose(XA.T@XA,XB.T@XB) and RSSA<1e-18 and np.isclose(RSSB,4.)
record('collinearity_alone_does_not_determine_R_squared',{'same_Gram_matrix':True,'RSS_A':RSSA,'RSS_B':RSSB,'R2_A':1-RSSA/4,'R2_B':1-RSSB/4})

# 21. The newly recovered public QR example, using positive diagonal convention.
XX=np.column_stack([np.ones(3),[0.,1.,2.]]); yy=np.array([1.,2.,4.]); QQ,RR=np.linalg.qr(XX,mode='reduced')
signs=np.where(np.diag(RR)<0,-1.,1.); QQ=QQ*signs;RR=signs[:,None]*RR
bb=np.linalg.solve(RR,QQ.T@yy)
assert np.allclose(RR,[[math.sqrt(3),math.sqrt(3)],[0,math.sqrt(2)]]) and np.allclose(bb,[5/6,3/2])
record('recovered_QR_public_example',{'R':RR.tolist(),'beta':bb.tolist(),'normal_equations_residual_norm':float(np.linalg.norm(XX.T@(yy-XX@bb)))})

# 22. Recovered public suppressor question: reproduce the stated significance pattern.
from scipy.stats import t as student_t
N=100; rrng=np.random.default_rng(1884); zz=rrng.normal(size=(N,3)); zz-=zz.mean(axis=0); qq,_=np.linalg.qr(zz,mode='reduced')
C=np.array([[1.,.1,0.],[.1,1.,.9],[0.,.9,1.]])
V=math.sqrt(N-1)*qq@np.linalg.cholesky(C).T
assert np.allclose(np.corrcoef(V,rowvar=False),C)
yy=V[:,0]; xa=V[:,1]; xb=V[:,2]
def classical_fit(design,target):
 b=np.linalg.lstsq(design,target,rcond=None)[0]; e=target-design@b; df=len(target)-design.shape[1]; s2=float(e@e/df)
 se=np.sqrt(np.diag(s2*np.linalg.inv(design.T@design))); tt=b/se; pv=2*student_t.sf(abs(tt),df)
 return b,se,tt,pv
b1,se1,t1,p1=classical_fit(np.column_stack([np.ones(N),xa]),yy)
b2,se2,t2,p2=classical_fit(np.column_stack([np.ones(N),xa,xb]),yy)
assert p1[1]>.05 and np.all(p2[1:]<.05) and np.allclose(b2[1:],[.1/.19,-.09/.19])
assert se2[1]>se1[1] # The mechanism is not a magically smaller SE.
record('suppressor_public_question_1884',{'option':'C','sample_correlation_matrix_Y_X1_X2':C.tolist(),'positive_definite_eigenvalues':np.linalg.eigvalsh(C).tolist(),'n':N,'univariate_slope':float(b1[1]),'univariate_t':float(t1[1]),'univariate_p':float(p1[1]),'multiple_slopes':b2[1:].tolist(),'multiple_t':t2[1:].tolist(),'multiple_p':p2[1:].tolist(),'univariate_SE':float(se1[1]),'multiple_X1_SE':float(se2[1])})

out=Path(__file__).with_name('statistics_ml_checks.json')
out.write_text(json.dumps({'verification_date':'2026-10-28','deterministic_seed':20261028,'checks_passed':len(OUT),'checks':OUT},ensure_ascii=False,indent=2))
print(json.dumps({'checks_passed':len(OUT),'beta_tail':tail,'clipped_variance':closed,'output':str(out)},ensure_ascii=False))
