"""Original teaching implementations and small independent counterexamples.

Run directly to reproduce coding_checks_report.json. These are bounded checks,
not a claim that every QuantVault implementation has been executed.
"""
from collections import deque
from decimal import Decimal as D
from itertools import product
from math import exp, log, isclose, asin, pi, sqrt
from pathlib import Path
import json

def longest_sum_k(a, target):
    first = {0: -1}
    prefix = best = 0
    for j, x in enumerate(a):
        prefix += x
        if prefix - target in first:
            best = max(best, j - first[prefix - target])
        first.setdefault(prefix, j)
    return best

def shortest_exact_k(a, k):
    if k <= 0:
        return -1
    counts = {}
    left, best = 0, len(a) + 1
    for right, x in enumerate(a):
        counts[x] = counts.get(x, 0) + 1
        while len(counts) == k:
            best = min(best, right - left + 1)
            y = a[left]
            counts[y] -= 1
            if counts[y] == 0:
                del counts[y]
            left += 1
    return best if best <= len(a) else -1

def merge_summary(left, right):
    """Summary of concatenation; order matters."""
    if left is None:
        return right
    if right is None:
        return left
    lmax, lmin, ldd = left
    rmax, rmin, rdd = right
    return max(lmax, rmax), min(lmin, rmin), max(ldd, rdd, lmax - rmin)

class DrawdownQueue:
    def __init__(self):
        self.front = []
        self.back = []
        self.size = 0

    def push(self, x):
        prior = self.back[-1][1] if self.back else None
        self.back.append((x, merge_summary(prior, (x, x, 0))))
        self.size += 1

    def pop(self):
        if not self.front:
            while self.back:
                x, _ = self.back.pop()
                prior = self.front[-1][1] if self.front else None
                self.front.append((x, merge_summary((x, x, 0), prior)))
        self.front.pop()
        self.size -= 1

    def drawdown(self):
        left = self.front[-1][1] if self.front else None
        right = self.back[-1][1] if self.back else None
        summary = merge_summary(left, right)
        return summary[2] if summary else 0

def rolling_drawdown(values, width):
    if width <= 0:
        raise ValueError('width must be positive')
    q, result = DrawdownQueue(), []
    for value in values:
        q.push(value)
        if q.size > width:
            q.pop()
        result.append(q.drawdown())
    return result

def fifo_demo(trades):
    """Decimal reference; fees recognized once at trade arrival.

    Zero quantity is a complete no-op. Invalid/nonfinite records are skipped
    with an audit message. This is an explicit teaching contract.
    """
    lots, warnings = deque(), []
    realized = peak = dd = D(0)
    for i, trade in enumerate(trades):
        price, qty = D(str(trade[0])), D(str(trade[1]))
        fee = D(str(trade[2])) if len(trade) > 2 else D(0)
        if not all(v.is_finite() for v in (price, qty, fee)) or fee < 0:
            warnings.append(f'invalid record {i}')
            continue
        if qty == 0:
            continue
        trade_pnl = -fee
        remaining = qty
        while lots and remaining and (lots[0][1] > 0) != (remaining > 0):
            old_price, old_qty = lots[0]
            side = D(1) if old_qty > 0 else D(-1)
            matched = min(abs(old_qty), abs(remaining))
            trade_pnl += matched * (price - old_price) * side
            old_qty -= side * matched
            remaining += side * matched
            if old_qty == 0:
                lots.popleft()
            else:
                lots[0][1] = old_qty
        if remaining:
            lots.append([price, remaining])
        realized += trade_pnl
        peak = max(peak, realized)
        dd = max(dd, peak - realized)
    position = sum((q for _, q in lots), D(0))
    cost = sum((p * abs(q) for p, q in lots), D(0))
    return {'realized': realized, 'position': position,
            'average_cost': cost / abs(position) if position else D(0),
            'max_drawdown': dd, 'warnings': warnings}

def bisection(f, a, b, tol):
    if tol <= 0 or a >= b:
        raise ValueError('invalid bracket or tolerance')
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if (fa > 0) == (fb > 0):
        raise ValueError('root must be bracketed')
    while b - a > tol:
        mid = a + (b - a) / 2
        if mid == a or mid == b:
            break
        fm = f(mid)
        if fm == 0:
            return mid
        if (fa > 0) == (fm > 0):
            a, fa = mid, fm
        else:
            b = mid
    return a + (b - a) / 2

def trunc_div(a, b):
    q = abs(a) // abs(b)
    return -q if (a < 0) != (b < 0) else q

def check_all():
    records = []
    def add(name, details):
        records.append({'check': name, 'passed': True, 'details': details})

    tested = 0
    for n in range(7):
        for a in product(range(3), repeat=n):
            for k in range(1, 5):
                valid = [j-i for i in range(n) for j in range(i+1,n+1)
                         if len(set(a[i:j])) == k]
                assert shortest_exact_k(a, k) == (min(valid) if valid else -1)
                tested += 1
    add('shortest_exact_k_exhaustive', {'arrays_and_K': tested})

    tested = 0
    for n in range(1, 7):
        for a in product((0, 2, 5), repeat=n):
            for w in range(1, 6):
                expected = []
                for r in range(n):
                    x = a[max(0,r-w+1):r+1]
                    expected.append(max(x[i]-x[j] for i in range(len(x))
                                        for j in range(i,len(x))))
                assert rolling_drawdown(a, w) == expected
                tested += 1
    add('ordered_drawdown_queue_exhaustive', {'arrays_and_windows': tested})

    assert longest_sum_k([2,-1,1,2], 2) == 3
    assert longest_sum_k([0,0], 0) == 2
    add('longest_sum_k', {'signed_values': True, 'zero_prefixes': True})

    x = fifo_demo([(10,3),(14,-2),(8,-3),(6,2)])
    assert x['realized'] == 10 and x['position'] == 0 and x['max_drawdown'] == 2
    tiny = fifo_demo([(0,'7.5e-13'),('1e15','-7.5e-13')])
    assert tiny['realized'] == 750
    add('fifo_reference_and_tiny_lots', {'example': str(x), 'tiny_correct_pnl': str(tiny['realized']),
        'source_threshold_result': 0, 'reason': 'both new lots fall below the unconditional 1e-12 append threshold'})

    f = lambda x: 1e-200 * (x - .25)
    a, b, fa = 0.0, 1.0, f(0)
    while b-a > 1e-10:
        mid = (a+b)/2
        if fa*f(mid) <= 0:
            b = mid
        else:
            a, fa = mid, f(mid)
    bad_root = (a+b)/2
    correct = bisection(f, 0, 1, 1e-10)
    assert abs(bad_root-.25) > .2 and correct == .25
    add('bisection_product_underflow', {'source_formula_result': bad_root, 'correct': correct})

    logits = [1e16,1e16]
    m = max(logits)
    z = sum(exp(x-m) for x in logits)
    bad_ce = m + log(z) - logits[0]
    good_ce = (m-logits[0]) + log(z)
    assert bad_ce == 0 and isclose(good_ce, log(2))
    add('cross_entropy_cancellation', {'source_formula': bad_ce, 'shifted_formula': good_ce})

    a = 2**53+1
    assert int(a/1) != a and trunc_div(a,1) == a and trunc_div(-7,2) == -3
    add('rpn_float_division', {'input_numerator': a, 'source_formula': int(a/1), 'correct': a})

    cell = [7]
    cell[0] = cell[0] + cell[0]
    cell[0] = cell[0] - cell[0]
    cell[0] = cell[0] - cell[0]
    assert cell[0] == 0
    add('arithmetic_swap_alias', {'initial': 7, 'same_storage_result': cell[0]})

    present, n = {0}, 0
    trace = []
    for _ in range(4):
        assert n in present
        trace.append(n)
        n *= 2
    add('doubling_fixed_point', {'trace': trace, 'conclusion': 'state repeats forever under stated loop'})

    delta = 100
    derivative = lambda q: delta / (2*pi*sqrt(q*(1-q)))
    assert derivative(.0001) > derivative(.5)
    add('tdigest_scale_derivative', {'at_q_0_0001': derivative(.0001), 'at_q_0_5': derivative(.5),
        'invariant': 'k(q_right)-k(q_left)<=1 for non-singleton clusters; derivative larger means smaller allowed rank span'})

    # Scalar operation counts establish the unequal-length multiplication cost.
    count = lambda m: sum(shift+1 for shift in range(m))
    assert count(200) > 3.9*count(100)
    add('partial_product_string_lengths', {'lengths_n1_m100': count(100), 'lengths_n1_m200': count(200),
        'conclusion': 'copying and adding growing shifted strings can be quadratic in longer operand'})
    n,d=1.0,1e-40
    threshold=n-sqrt(2*n*d)
    assert threshold==n
    try:
        (n+threshold)/2-d*threshold/(n-threshold)
        raise AssertionError('expected source division by zero')
    except ZeroDivisionError:
        pass
    good_price=n-sqrt(2*n*d)+d
    assert good_price==1.0
    assert 100-sqrt(2*100*8)+8==68
    add('uniform_resampling_cancellation', {'source_divisor':n-threshold,'safe_price':good_price,'ordinary_example':68})
    return records

if __name__ == '__main__':
    results = check_all()
    output = {'checks_passed': len(results), 'checks': results,
              'scope': 'bounded original teaching checks and minimal counterexamples; not an exhaustive audit of all 48 source solutions'}
    target = Path(__file__).with_name('coding_checks_report.json')
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks_passed':len(results),'report':str(target)}))
