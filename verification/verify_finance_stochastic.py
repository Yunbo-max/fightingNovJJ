"""Independent equation, quadrature and numerical checks; no website code copied."""
import json, math
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parent
out={}

def bs(S,K,r,sig,T,q=0):
    if T==0:return max(S-K,0)
    if sig==0:return max(S*math.exp(-q*T)-K*math.exp(-r*T),0)
    d1=(math.log(S/K)+(r-q+.5*sig*sig)*T)/(sig*math.sqrt(T));d2=d1-sig*math.sqrt(T)
    return S*math.exp(-q*T)*norm.cdf(d1)-K*math.exp(-r*T)*norm.cdf(d2)

def tree(S,K,r,sig,T,N,put=False,american=False):
    dt=T/N;u=math.exp(sig*math.sqrt(dt));d=1/u
    prob=(math.exp(r*dt)-d)/(u-d)
    if not 0<=prob<=1: raise ValueError('CRR step violates no-arbitrage')
    vals=np.maximum((K-S*u**(2*np.arange(N+1)-N)) if put else (S*u**(2*np.arange(N+1)-N)-K),0.)
    for level in range(N-1,-1,-1):
        vals=math.exp(-r*dt)*((1-prob)*vals[:-1]+prob*vals[1:])
        if american:
            stocks=S*u**(2*np.arange(level+1)-level)
            vals=np.maximum(vals,np.maximum(K-stocks if put else stocks-K,0.))
    return float(vals[0])

exact=bs(100,100,.05,.2,1)
out['BS_CRR']={'closed_form':exact,'crr200':tree(100,100,.05,.2,1,200),'american_call_crr200':tree(100,100,.05,.2,1,200,american=True)}
assert abs(out['BS_CRR']['crr200']-10.4405912599)<1e-8
assert abs(out['BS_CRR']['crr200']-out['BS_CRR']['american_call_crr200'])<1e-10
try: tree(100,100,1,.01,1,1)
except ValueError: out['CRR_invalid_probability_rejected']=True
else: raise AssertionError('invalid probability not rejected')

def exit_moments(mu,L,U):
    if mu==0:return L/(L+U),L*U
    p=-math.expm1(-2*mu*L)/(-math.expm1(-2*mu*(L+U)))
    return p,((L+U)*p-L)/mu
for mu in [-2.,-.1,.1,.5,2.]:
    for b in [.01,.1,1.,3.]:
        p,t=exit_moments(mu,b,b)
        assert abs(b*(2*p-1)/t-mu)<1e-9
out['barrier_rate_identity']='mu (algebra: mu E[tau] = b(2p-1)); numerical sweep passed'
p,t=exit_moments(.5,1,2)
out['barrier_example']={'p':p,'mean_time':t,'fixed_lower_upper_infinite_p':1-math.exp(-1)}
out['first_passage_probability']=2*norm.cdf(-1)
out['finite_walk_return']=str((Fraction(16,17)+Fraction(82,83))/2)
assert out['finite_walk_return']=='1361/1411'
out['dice_product']={'positive_ordered_pairs':sum(i*j>9700 for i in range(1,101) for j in range(1,101)),'payoff_sum':sum(max(i*j-9700,0) for i in range(1,101) for j in range(1,101))}
assert out['dice_product']=={'positive_ordered_pairs':8,'payoff_sum':1005}
x,y=Fraction(7,13),Fraction(6,13)
assert x==(1+6*y+29*x)/36 and y==(1+29*x)/36
out['dice_pattern']={'x':str(x),'y':str(y)}

# Independent full partition-chain solve for neutral recoloring.
def partitions(n,maximum=None):
    if n==0: yield ();return
    for k in range(min(n, maximum or n),0,-1):
        for tail in partitions(n-k,k):yield (k,)+tail

def recolor_mean(n):
    states=list(partitions(n));trans=[s for s in states if len(s)>1];idx={s:i for i,s in enumerate(trans)}
    d=len(trans)
    A=[[Fraction(int(i==j)) for j in range(d)]+[Fraction(1)] for i in range(d)]
    for state in trans:
        row=idx[state]
        for receiver,c1 in enumerate(state):
            for donor,c2 in enumerate(state):
                multiplicity=c1*(c2-(receiver==donor))
                if not multiplicity:continue
                nxt=list(state)
                if receiver!=donor:nxt[receiver]-=1;nxt[donor]+=1
                nxt=tuple(sorted((c for c in nxt if c),reverse=True))
                if len(nxt)>1:A[row][idx[nxt]]-=Fraction(multiplicity,n*(n-1))
    for col in range(d):
        pivot=next(i for i in range(col,d) if A[i][col])
        A[col],A[pivot]=A[pivot],A[col]
        z=A[col][col];A[col]=[x/z for x in A[col]]
        for row in range(d):
            if row!=col:
                factor=A[row][col]
                A[row]=[a-factor*b for a,b in zip(A[row],A[col])]
    return A[idx[(1,)*n]][-1]
out['recolor_partition_chain']={str(n):str(recolor_mean(n)) for n in range(2,8)}
assert all(int(v)==(int(n)-1)**2 for n,v in out['recolor_partition_chain'].items())

# Quadrature of independently derived pathwise and LR Greeks.
S,K,r,sig,T=100,100,.05,.2,1
rootT=math.sqrt(T);disc=math.exp(-r*T);cut=(math.log(K/S)-(r-.5*sig*sig)*T)/(sig*rootT)
def st(z):return S*math.exp((r-.5*sig*sig)*T+sig*rootT*z)
pwdelta=quad(lambda z:disc*st(z)/S*norm.pdf(z),cut,12,epsabs=1e-10)[0]
pwvega=quad(lambda z:disc*st(z)*(rootT*z-sig*T)*norm.pdf(z),cut,12,epsabs=1e-10)[0]
lrvega=quad(lambda z:disc*(st(z)-K)*((z*z-1)/sig-z*rootT)*norm.pdf(z),cut,12,epsabs=1e-10)[0]
d1=(math.log(S/K)+(r+.5*sig*sig)*T)/(sig*rootT)
analytic_delta=norm.cdf(d1);analytic_vega=S*norm.pdf(d1)*rootT
assert abs(pwdelta-analytic_delta)<1e-9
assert abs(lrvega-analytic_vega)<1e-8 and abs(pwvega-analytic_vega)<1e-8
out['greeks_quadrature']={'delta_pathwise':pwdelta,'delta_closed':analytic_delta,'vega_pathwise':pwvega,'vega_LR':lrvega,'vega_closed':analytic_vega}

def iv_call(price,S,K,T):return brentq(lambda v:bs(S,K,0,v,T)-price,1e-7,3)
out['skew']={'ATM_IV':iv_call(3.99,100,100,.25),'90_IV':iv_call(11.45,100,90,.25),'110_IV':iv_call(.48,100,110,.25),'P90_at_20pct':bs(100,90,0,.2,.25)-10}
out['random_vol']={str(k):{'constant':bs(100,k,0,.3,1),'mixture':.5*(bs(100,k,0,.2,1)+bs(100,k,0,.4,1))} for k in [100,130]}
v=math.sqrt(.2**2+.3**2-2*.5*.2*.3)
out['margrabe_equal_spots']=100*(2*norm.cdf(v/2)-1)
out['ATM_quarter_year_call']=bs(100,100,0,.2,.25)
out['gamma_peak_ratio_r0_q0_sig20_T1']=math.exp(-1.5*.2**2)

def explicit_call(J,a_target=.45):
    # Derive heat transform directly from V=K exp(alpha*x+beta*tau) u.
    r,sig,T,K=.05,.2,1.,100.;xmin,xmax=-3.,3.
    k=2*r/(sig*sig);alpha=(1-k)/2;beta=-(k+1)**2/4
    dx=(xmax-xmin)/J;tau_total=.5*sig*sig*T
    N=math.ceil(tau_total/(a_target*dx*dx));dt=tau_total/N;a=dt/(dx*dx)
    grid=np.linspace(xmin,xmax,J+1)
    heat=np.maximum(np.exp(grid)-1,0)*np.exp(-alpha*grid)
    for n in range(N):
        nxt=heat.copy()
        nxt[1:-1]=a*heat[:-2]+(1-2*a)*heat[1:-1]+a*heat[2:]
        t_heat=(n+1)*dt
        nxt[0]=0
        nxt[-1]=(math.exp(xmax)-math.exp(-k*t_heat))*math.exp(-alpha*xmax-beta*t_heat)
        heat=nxt
    values=K*np.exp(alpha*grid+beta*tau_total)*heat
    return {'N':N,'a':a,'value':float(np.interp(0,grid,values))}
out['explicit_grid']={str(j):explicit_call(j) for j in [600,1200,2400]}
err1=out['explicit_grid']['600']['value']-exact;err2=out['explicit_grid']['1200']['value']-exact
out['grid_error_ratio']=err1/err2
out['Richardson']=(4*out['explicit_grid']['1200']['value']-out['explicit_grid']['600']['value'])/3
assert 3.8<out['grid_error_ratio']<4.2
assert abs(out['Richardson']-exact)<1e-5

# KKT-free check of the complete two-odds profit in both demand regimes.
odds=np.linspace(1.00001,15.,1600);oy=odds[:,None];on=odds[None,:]
nonoverlap=1/oy+1/on>=1
out['overround_global_grid']={}
for p in [.1,.5,.9]:
    profit=np.where(nonoverlap,(1-1/oy)*(1-p*oy)+(1-1/on)*(1-(1-p)*on),1-(p*oy*oy+(1-p)*on*on)/(oy+on))
    optimum=3-2*math.sqrt(p)-2*math.sqrt(1-p)
    gridmax=float(profit.max())
    assert 0<=optimum-gridmax<.0001
    out['overround_global_grid'][str(p)]={'analytic':optimum,'grid_max':gridmax}

# Complete deterministic lamp orbit, independently checking the stated period.
state=((1,1,1,1),0);seen={};orbit=[]
while state not in seen:
    seen[state]=len(orbit);orbit.append(state)
    lamps,position=state
    lamps=list(lamps);destination=(position+1)%4
    lamps[destination]^=lamps[position]
    state=(tuple(lamps),destination)
assert seen[state]==0 and len(orbit)==60
matrix=np.array([[0,1,1,1],[1,1,0,0],[1,1,1,0],[1,1,1,1]],dtype=int)
for i in range(0,60,4):
    current=np.array(orbit[i][0]);expected=np.array(orbit[(i+4)%60][0])
    assert np.array_equal(matrix@current%2,expected)
out['lamppost']={'transient':0,'minimal_full_state_period':60,'distinct_full_states':60,'four_step_states':[''.join(map(str,orbit[i][0])) for i in range(0,60,4)]}

records=json.loads((ROOT.parent/'reviews'/'finance_stochastic_reviews.json').read_text())
assert len(records)==51 and len({x['catalog_id'] for x in records})==51
for row in records:
    assert isinstance(row['status'],str) and isinstance(row['errors_conditions'],list)
    assert row['status'] in ['independently_verified','solution_reviewed','title_only']
    if row['status']!='title_only':assert row['url'].startswith('https://quantvault.org/problem-')
out['catalog_validation']={'records':51,'full_solution_read':sum(x['access']=='public_full_solution' for x in records),'title_only':sum(x['status']=='title_only' for x in records)}
(ROOT/'finance_stochastic_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
