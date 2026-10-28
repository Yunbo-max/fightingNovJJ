"""Bounded exact checks supporting original combinatorics notes."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, factorial, prod
from pathlib import Path
import json

def count_digit_by_cycles(n, d, base=10):
    if base < 2 or not 0 <= d < base:
        raise ValueError('invalid digit/base')
    total, place = 0, 1
    while place <= n:
        period = base * place
        full, remaining = divmod(n + 1, period)
        total += full * place + min(place, max(0, remaining - d * place))
        if d == 0:
            total -= place
        place *= base
    return total

def fancy_floor(n):
    place = 1
    while place * 4 <= n:
        place *= 4
    answer, tight = 0, True
    while place:
        digit = n // place % 4
        if not tight:
            answer += place
        elif digit < 2:
            answer += digit * place
        else:
            answer += place
            tight = False
        place //= 4
    return answer

def digits_in_base(n, base):
    if n == 0:
        return [0]
    out = []
    while n:
        n, digit = divmod(n, base)
        out.append(digit)
    return out

def main():
    records = []
    def add(cid, result):
        records.append({'catalog_id':cid,'passed':True,'result':result})

    good = [x for x in combinations_with_replacement(range(1,7),6)
            if {a+b for a in x for b in x} == set(range(2,13))]
    assert len(good) == 11
    add('QV-F0045', {'multisets_checked':462,'valid':len(good)})

    @lru_cache(None)
    def split_scores(n):
        if n == 1:
            return frozenset([0])
        return frozenset(a*(n-a)+x+y for a in range(1,n)
                         for x in split_scores(a) for y in split_scores(n-a))
    assert all(split_scores(n)=={comb(n,2)} for n in range(1,11))
    add('QV-F0074', {'all_split_size_trees_n1_to10':'one total each'})

    catalans=[]
    for n in range(7):
        count=0
        for left_positions in combinations(range(2*n),n):
            left=set(left_positions); balance=0; valid=True
            for i in range(2*n):
                balance += 1 if i in left else -1
                if balance < 0:
                    valid=False
                    break
            count += valid
        assert count==comb(2*n,n)//(n+1)
        catalans.append(count)
    add('QV-F0131',catalans)

    test_counts=[]
    for first_bad in range(1,101):
        low,high,tests=1,100,0
        while low<high:
            mid=(low+high)//2; tests+=1
            if mid>=first_bad: high=mid
            else: low=mid+1
        assert low==first_bad
        test_counts.append(tests)
    assert max(test_counts)==7
    add('QV-F0160',{'cases':100,'max_tests':7})

    for a in ((0,-1,3,5),(1,1,2,2,3),(-3,-2,-1),(2,4),(1,3,5)):
        o=sum(x%2!=0 for x in a)
        c3=lambda n: comb(n,3) if n>=3 else 0
        assert sum(prod(x)%2==0 for x in combinations(a,3))==c3(len(a))-c3(o)
    add('QV-F0235','parity formula checked on signs, zeros, duplicates, length<3')

    target_orders=factorial(15)//prod(factorial(x) for x in range(1,6))
    assert target_orders==37837800
    add('QV-F0237',target_orders)

    pair_sum=sum(range(31,41)); total=F(pair_sum,4)
    assert total==F(355,4) and (2*total).denominator!=1
    add('QV-F0253',{'forced_total':str(total),'not_half_integer':True,
         'conclusion':'no five weights can have all these integer pairwise sums'})

    assert len(list(product(range(3),repeat=5)))==243
    assert sum(comb(5,k)*2**k for k in range(6))==243
    add('QV-F0256',243)

    two_suits=12*comb(13,3)*comb(13,2)
    assert two_suits==267696
    add('QV-F0257',two_suits)

    assert all(sum((2*i)**2-(2*i-1)**2 for i in range(1,n+1))==n*(2*n+1)
               for n in range(1,101))
    add('QV-F0258',5050)

    cases=0
    for base in range(2,11):
        cumulative=[0]*base
        for n in range(1,301):
            for d in digits_in_base(n,base): cumulative[d]+=1
            for d in range(base):
                assert count_digit_by_cycles(n,d,base)==cumulative[d]
                cases+=1
    assert count_digit_by_cycles(1000,4)==300
    add('QV-F0261',{'base_N_digit_cases':cases,'digit4_through1000':300})

    lengths=[len(str(2**1000)),len(str(5**1000))]
    assert lengths==[302,699] and sum(lengths)==1001
    add('QV-F0263',{'independent_title_reconstruction':lengths,'total_digits':1001})

    students=factorial(12)//factorial(3)**4
    assert students==369600
    add('QV-F0264',students)

    latest=0
    for n in range(1,10001):
        if set(digits_in_base(n,4))<={0,1}: latest=n
        assert fancy_floor(n)==latest
    add('QV-F0269',{'all_N1_to10000':'exact agreement'})

    for n in range(3,151):
        actual=sum(1 for x in range(1,n//3+1)
                   for y in range(x,(n-x)//2+1) if y<=n-x-y)
        equal_all=int(n%3==0)
        exactly_two=(n-1)//2-equal_all
        formula=F(comb(n-1,2),6)+F(exactly_two,2)+F(5*equal_all,6)
        assert actual==formula
    add('QV-F0270',{'exact_tie_corrected_formula_N3_to150':'checked','limit':'1/12'})

    people=set(range(5)); blocked=[set(x) for x in combinations(range(5),2)]
    for size in range(6):
        for coalition in combinations(range(5),size):
            group=set(coalition)
            opens=all(bool(group & (people-pair)) for pair in blocked)
            assert opens==(size>=3)
    assert all(sum(i not in pair for pair in blocked)==6 for i in people)
    add('QV-F0276',{'coalitions_checked':32,'locks':10,'keys_per_person':6})

    valid=[x for x in range(1,101) if not set(str(x))&{'7','8'}]
    assert sum(valid)==2740 and len(valid)==64
    add('QV-F0278',{'sum':2740,'included_count':64})

    def canon(tree):
        if len(tree)==1: return tree[0]
        m=len(tree)//2
        return tuple(sorted((canon(tree[:m]),canon(tree[m:]))))
    counts={}
    for n in (2,4,8):
        count=len({canon(p) for p in permutations(range(n))})
        assert count==factorial(n)//2**(n-1)
        counts[n]=count
    add('QV-F0290',counts)

    multiple=66*((600000+65)//66)
    assert multiple==600006 and multiple%66==0 and multiple-66<600000
    add('QV-F0311',{'independent_title_reconstruction':multiple,'previous':multiple-66})

    a,b=1,1
    for n in range(21):
        direct=sum(comb(n-k,k) for k in range(n//2+1))
        assert direct==a
        a,b=b,a+b
    assert sum(comb(10-k,k) for k in range(6))==89
    add('QV-F0447',{'n0_to20':'recurrence versus count by two-hops','n10':89})

    out={'checks_passed':len(records),'checks':records,
         'scope':'bounded exact checks, not a proof substitute for every general statement; reconstructed title-only examples are labeled'}
    target=Path(__file__).with_name('combinatorics_checks_report.json')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks_passed':len(records),'report':str(target)}))

if __name__=='__main__': main()
