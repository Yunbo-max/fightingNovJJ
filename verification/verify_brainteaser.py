"""Independent small-state/exact checks for reviewed brain teasers."""
from pathlib import Path
from itertools import product,permutations,combinations
from collections import deque,Counter
from fractions import Fraction as F
from functools import lru_cache
from math import sqrt,log,log10
from datetime import date
import json,random

HERE=Path(__file__).resolve().parent
checks=[]
def rec(cid,method,result,ok=True):
    assert ok,(cid,result)
    checks.append(dict(catalog_id=cid,method=method,result=result,passed=True))

codes=[format(i,'010b') for i in range(1,1001)]
rec('QV-F0002','Check injective 10-bit code and 9-bit capacity',{'unique':len(set(codes)),'nine_capacity':2**9},len(set(codes))==1000 and 2**9<1000)

# Correct bin classification for every all-wrong assignment and allowed observation.
for contents in permutations('YRM'):
    if any(a==b for a,b in zip(contents,'YRM')):continue
    seen=contents[2]
    assert seen in 'YR'
    inferred=('R','M','Y') if seen=='Y' else ('M','Y','R')
    assert contents==inferred
rec('QV-F0006','Enumerate all derangements of the three labels','One draw from Mixed-labelled bin succeeds in every case')

for left_true,asked_liar in product((False,True),repeat=2):
    other_answer=left_true if asked_liar else not left_true
    answer=not other_answer if asked_liar else other_answer
    assert answer != left_true
rec('QV-F0027','Truth-table check of the yes/no formulation','Answer is always the negation of left-is-correct')

rooms=[2**b*(2*p-1) for b in range(20) for p in range(1,21)]
rec('QV-F0021','Check rectangular set of pair-map inputs',{'inputs':400,'unique_rooms':len(set(rooms))},len(set(rooms))==400)

@lru_cache(None)
def multiset_results(t):
    if len(t)==1:return frozenset(t)
    out=set()
    for i,j in combinations(range(len(t)),2):
        z=tuple(sorted([x for k,x in enumerate(t) if k not in (i,j)]+[abs(t[i]-t[j])]))
        out.update(multiset_results(z))
    return frozenset(out)
for n in range(2,8):assert all(x%2==(n*(n+1)//2)%2 for x in multiset_results(tuple(range(1,n+1))))
rec('QV-F0026','Exhaustive multiset reduction for n=2..7; literal-set counterexample',{'literal_set_n4':'{1,2,3,4}: remove1,4; existing3 not duplicated -> {2,3} -> {1}, whereas initial sum is even','multiset_invariant':'All small cases preserve sum parity'})

age=[x for x in range(1,101) if x*x<=1970 and x*x-x>=1870]
rec('QV-F0104','Enumerate integer ages1..100',age,age==[44])
rec('QV-F0109','Independent Gregorian standard-library date',str(date(2078,1,1).weekday()),date(2078,1,1).weekday()==5)
two=[n for n in range(10,100) if 2*(n//10)*(n%10)==n]
rec('QV-F0125','Enumerate all90 two-digit integers',two,two==[36])

placements=[]
for axis in range(3):
 for coord in product(range(6),repeat=3):
    if coord[axis]>2:continue
    colours=[]
    for delta in range(4):
        q=list(coord);q[axis]+=delta
        colours.append(sum(v//2 for v in q)%2)
    placements.append(sum(colours))
rec('QV-F0412','Exhaust all324 axis-aligned unit-grid brick placements',{'placements':len(placements),'black_cells_per_brick':sorted(set(placements))},len(placements)==324 and set(placements)=={2})

a=set('012345');b=set('0126789')
missing=[str(d).zfill(2) for d in range(1,32) if not ((str(d).zfill(2)[0] in a and str(d).zfill(2)[1] in b) or (str(d).zfill(2)[0] in b and str(d).zfill(2)[1] in a))]
rec('QV-F0413','Check all31 date glyph pairs',{'missing':missing},not missing)

codes={s*k:(k,s) for k in range(1,11) for s in (-1,1)}
rec('QV-F0416','Check all20 signed bag hypotheses and zero-sample ambiguity',{'distinct_1_to_10':len(codes),'zero_sample_heavy_light':[0*(-1),0*(1)]},len(codes)==20)

def has_mono_triangle(n,mask):
    edges=list(combinations(range(n),2));ix={e:i for i,e in enumerate(edges)}
    for tri in combinations(range(n),3):
        vals=[(mask>>ix[e])&1 for e in combinations(tri,2)]
        if len(set(vals))==1:return True
    return False
assert all(has_mono_triangle(6,mask) for mask in range(2**15))
cycle_edges={tuple(sorted((i,(i+1)%5))) for i in range(5)}
mask=sum((1<<i) for i,e in enumerate(combinations(range(5),2)) if e in cycle_edges)
assert not has_mono_triangle(5,mask)
rec('QV-F0418','Enumerate all32768 colourings ofK6 and explicitC5 counterexample','R(3,3)=6 verified')

deviations=[sum(3**i*x for i,x in enumerate(ds)) for ds in product((-1,0,1),repeat=5)]
rec('QV-F0420','Enumerate all243 balanced-ternary encodings',{'unique':len(set(deviations)),'range':[min(deviations),max(deviations)]},set(deviations)==set(range(-121,122)))

start=(13,15,17);seen={start};queue=deque([start])
while queue:
    s=queue.popleft()
    for i,j in combinations(range(3),2):
        if s[i] and s[j]:
            t=list(s);t[i]-=1;t[j]-=1;t[3-i-j]+=2;t=tuple(t)
            if t not in seen:seen.add(t);queue.append(t)
rec('QV-F0422','Breadth-first enumerate reachable population states',{'reachable':len(seen),'monochromatic':sum(sum(v>0 for v in s)==1 for s in seen)},not any(sum(v>0 for v in s)==1 for s in seen))

@lru_cache(None)
def split_totals(n):
    if n==1:return frozenset([0])
    return frozenset(x*(n-x)+a+b for x in range(1,n) for a in split_totals(x) for b in split_totals(n-x))
assert all(split_totals(n)=={n*(n-1)//2} for n in range(1,25))
rec('QV-F0423','All recursive split sums for n1..24','Unique valueC(n,2) in each case')

rng=random.Random(17)
for _ in range(500):
    n=10;g=[rng.randrange(100) for _ in range(n)];cuts=sorted([0,sum(g)]+[rng.randrange(sum(g)+1) for _ in range(n-1)])
    d=[cuts[i+1]-cuts[i] for i in range(n)]
    pref=[0]
    for x,y in zip(g,d):pref.append(pref[-1]+x-y)
    m=min(range(n),key=lambda i:pref[i]);tank=0
    for k in range(n):
        j=(m+k)%n;tank+=g[j]-d[j];assert tank>=0
rec('QV-F0424','Exercise minimum-prefix construction on500 independently generated configurations','All circular prefixes nonnegative; proof supplied in notes')

for hats in product(range(7),repeat=7):
    total=sum(hats)
    correct=sum(((i-(total-hats[i]))%7)==hats[i] for i in range(7))
    assert correct==1
rec('QV-F0426','Exhaust all823543 assignments for the seven-colour strategy','Exactly one correct for every assignment')

t=(sqrt(5)-1)/2
k=2/log((1+t)/t)
rec('QV-F0432','Substitute positive root back into both distance observations',{'first_hour':k*log((1+t)/t),'two_hours':k*log((2+t)/t)},abs(k*log((2+t)/t)-3)<1e-12)
rec('QV-F0448','Check quantitative decimal-tail error bound',{'log10_upper_bound':-3000*log10(2)},-3000*log10(2)<-900)
roots=[x for x in range(100) if x**3%100==11]
rec('QV-F0449','Enumerate every residue class modulo100',roots,roots==[71])

(HERE/'brainteaser_verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(json.dumps({'checks':len(checks),'all_passed':True,'verified_entries':len({c['catalog_id'] for c in checks})}))
