"""Build a provisional, exposure-aware learning split from the source catalog."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION = '2026-10-29-v1'

# id, title, practical question, prerequisite ids
UNIT_ROWS = [
 ('A01','样本空间与等可能性','一个基本结果是什么，哪些结果才等可能？',[]),
 ('A02','排列组合与角色分配','顺序、角色和重复选择分别怎样计数？',['A01']),
 ('A03','重复元素排列与重数型','相同对象为什么要除阶乘，谁重复又怎么选？',['A02']),
 ('A04','相邻捆绑插空与不相邻','把哪些对象捆绑，怎样选择空位？',['A02','A03']),
 ('A05','圆排列与旋转对称','固定一个人后为何剩下 n−1 个对象要排列？',['A02']),
 ('A06','补集与容斥','至少一个事件怎样避免漏算和重复？',['A01','A02']),
 ('A07','无放回抽样与超几何计数','总体和成功类别确定后怎样数抽样结果？',['A02','A06']),
 ('A08','占位生日与不同类别数','固定抽取次数后出现多少类，何时出现碰撞？',['A03','A06']),
 ('A09','随机子集与逐元素状态','随机选子集与随机选子集大小有什么区别？',['A01','A02']),
 ('A10','标号分组与组合分配','组有无标签，组内顺序是否重要？',['A02','A03']),
 ('A11','隔板法与容量限制','相同物品分入不同盒子怎样数？',['A02','A06']),
 ('A12','格点路径与受限计数','路径怎样对应选择，限制怎样写入递推？',['A02','A06']),
 ('A13','对称性与可交换性','为什么两个人获胜概率相等，平局怎样处理？',['A01','A06']),
 ('B01','条件概率与条件样本空间','给定信息后分母应该换成什么？',['A01','A07']),
 ('B02','全概率与概率树','怎样对所有隐藏情形分类再加权？',['B01']),
 ('B03','贝叶斯的先验似然和后验','怎样从看到的结果反推隐藏原因？',['B02']),
 ('B04','基准率与检测可靠性','检测准确为什么不等于阳性后真的概率？',['B03']),
 ('B05','抽样和报告机制','同一句信息通过不同方式获得为什么答案不同？',['B01','B03']),
 ('B06','条件独立与无条件独立','两个信号能不能把概率直接相乘？',['B01','B02']),
 ('B07','后验赔率与序贯更新','多次新证据怎样累计，又依赖什么条件？',['B03','B06']),
 ('B08','后验预测与推断目标','隐藏原因的概率和下一次结果的概率怎样区分？',['B03','B07']),
 ('C01','PMF PDF CDF与取值域','概率、密度和累积概率分别是什么？',['A01','B01']),
 ('C02','Bernoulli与二项分布','固定次数的独立成功试验怎样建模？',['C01','A02']),
 ('C03','几何与负二项分布','等到第几次成功时怎样定义随机次数？',['C02']),
 ('C04','Poisson计数与稀疏化','固定区间中的随机到达数怎样建模？',['C01','C02']),
 ('C05','均匀分布与区间概率','均匀的是哪个变量和哪个区间？',['C01']),
 ('C06','指数分布与无记忆性','等待时间与多个时钟竞争怎样计算？',['C01','C04']),
 ('C07','Gamma与Erlang分布','等到多次到达的时间怎样建模？',['C06']),
 ('C08','Beta分布与随机参数混合','成功率本身随机时怎样更新和平均？',['C02','B08']),
 ('C09','正态分布与标准化','均值方差怎样决定标准化与线性组合？',['C01']),
 ('C10','联合边缘和条件分布','联合密度怎样变成边缘或条件密度？',['C01','B01']),
 ('C11','变量变换与随机生成','变换后的取值域和Jacobian怎样确定？',['C01','C05','C10']),
 ('C12','卷积与独立变量之和','两个随机数相加为什么通常不再均匀？',['C05','C10']),
 ('C13','生成函数与矩母函数','系数和函数导数怎样编码概率与矩？',['C02','C12']),
 ('C14','几何概率与抽样测度','面积均匀与半径均匀为何不是同一模型？',['C05','C10']),
 ('D01','期望与LOTUS','怎样直接计算随机支付的平均值？',['C01']),
 ('D02','线性期望与指示变量','什么时候不用整个联合分布也能求平均？',['D01','A02']),
 ('D03','方差协方差与相关系数','求和的波动为什么需要交叉项？',['D01','C10']),
 ('D04','独立不相关与依赖构造','不相关为什么不保证独立？',['D03','C10']),
 ('D05','全期望与全方差','先固定信息再平均能把问题拆成什么？',['B02','D01','D03']),
 ('D06','条件期望与联合正态预测','观察到带噪信号后怎样更新均值方差？',['C09','C10','D05']),
 ('D07','最大最小与顺序统计量','最大值的分布和均值怎样从事件推导？',['C01','D01']),
 ('D08','尾和尾积分与无穷期望','什么时候概率很小但期望仍可能无穷？',['D01','C03']),
 ('D09','集齐问题与分阶段等待','已经集齐若干类后下一阶段等多久？',['C03','D02']),
 ('D10','随机和与Wald条件','随机次数能否直接乘单次均值？',['D05','D08']),
 ('D11','概率界与矩不等式','只知道均值方差能给出什么概率保证？',['D03','D08']),
 ('D12','大数定律中心极限定理与误差','平均趋稳与误差缩小分别意味着什么？',['D03','D11']),
 ('E01','状态与第一步递推','哪些信息足以描述剩余问题？',['D05','C03']),
 ('E02','连续模式与重叠等待','失败后哪些已出现的后缀仍然有用？',['E01']),
 ('E03','吸收概率与边界到达','到达哪里和需要多久为何用不同方程？',['E01']),
 ('E04','有限期Bellman与倒推','停止价值和继续价值怎样逐步比较？',['E01','D05']),
 ('E05','接受阈值与重掷费用','有剩余次数和费用时什么结果值得收手？',['E04']),
 ('E06','重抽交换与不放回决策','重抽和交换怎样改变未来分布与机会？',['E04','A07']),
 ('E07','秘书问题与相对排名','只能观察相对排名时怎样设置停止规则？',['E04','D07']),
 ('E08','无限期停止与适用条件','几乎必停为何不保证终值期望守恒？',['D08','D10','E03','E04']),
 ('E09','信息价值采样成本与损失决策','信息能改变后续动作时值多少钱？',['B08','E04']),
]
UNITS = {row[0]: {'unit_id':row[0], 'title':row[1], 'question':row[2], 'prerequisites':row[3], 'train_core_slots':3, 'test_core_slots':2} for row in UNIT_ROWS}

FAMILY_ROUTES = {
 'F0003':'X24','F0004':'C13','F0005':'X24','F0007':'C14','F0008':'D02',
 'F0009':'E02','F0010':'E03','F0012':'B05','F0013':'E04','F0014':'X24',
 'F0015':'C08','F0016':'A13','F0017':'E07','F0018':'E03','F0019':'D09',
 'F0020':'B03','F0021':'X22','F0022':'D02','F0025':'C14','F0027':'E06',
 'F0028':'E09','F0029':'E05','F0032':'X24','F0033':'D02','F0034':'E03',
 'F0035':'C13','F0037':'A01','F0038':'A08','F0040':'D01','F0041':'D06',
 'F0042':'A06','F0043':'C14','F0044':'E01','F0045':'C03','F0046':'D07',
 'F0047':'D02','F0048':'E03','F0049':'B05','F0050':'E03','F0051':'D05',
 'F0052':'E02','F0053':'C11','F0054':'X24','F0056':'D04','F0057':'A12',
 'F0058':'D12','F0060':'X24','F0062':'D07','F0063':'E04','F0064':'D01',
 'F0066':'A01','F0067':'C04','F0068':'D08','F0069':'D11','F0070':'A10',
 'F0071':'D03','F0072':'D05','F0073':'D04','F0074':'E09','F0075':'D06',
 'F0076':'D07','F0077':'X22','F0079':'D07','F0081':'X24','F0085':'X14',
 'F0086':'X24','F0087':'D03','F0089':'E03','F0091':'C13','F0092':'E09',
 'F0093':'E06','F0094':'C11','F0096':'X24','F0100':'X24','F0101':'A02',
 'F0102':'A12','F0104':'D06','F0105':'D02','F0106':'C04','F0107':'X08',
 'F0110':'X24','F0112':'A12','F0113':'X24','F0117':'X24','F0118':'D06',
 'F0119':'A07','F0123':'X24','F0124':'E02','F0125':'X24','F0126':'D08',
 'F0127':'E01','F0131':'X24','F0133':'C14','F0134':'C11','F0136':'D04',
 'F0138':'D03','F0141':'A11','F0145':'E09','F0146':'X18','F0147':'D01',
 'F0149':'X15','F0151':'A12','F0154':'D07','F0155':'E03','F0156':'C13',
 'F0157':'D09','F0159':'D07','F0161':'B03','F0162':'D07','F0165':'X24',
 'F0166':'E09','F0169':'A05','F0170':'A03','F0172':'C06','F0174':'C11',
 'F0179':'D08','F0180':'C13','F0182':'X24','F0184':'X24','F0190':'A04',
 'F0196':'X24','F0197':'X24','F0200':'E06','F0210':'X14','F0212':'A10',
 'F0218':'X24','F0221':'X24','F0223':'X24','F0226':'B08','F0227':'X24',
 'F0231':'X18','F0232':'X24','F0236':'X24','F0258':'D07','F0267':'C04',
 'F0272':'E03','F0273':'X24','F0284':'C11','F0299':'X06','F0381':'X24',
 'F0382':'D05','F0386':'C13','F0388':'D08','F0389':'E06','F0391':'E01',
 'F0392':'E03','F0395':'X24','F0408':'E09','F0409':'C06',
}

# The learner has already seen these templates, even where source IDs differ.
PROTOTYPES = [
 ('dice_prime_product',r'product.*prime|prime.*product','A01',True),
 ('dice_strict_order',r'(?:dice|die).*strictly (?:increasing|decreasing)','A02',True),
 ('friends_adjacent_row',r'two friends.*adjacent.*row','A04',True),
 ('birthday_collision',r'^birthday problem$|shared birthdays|birthday.*collision','A08',True),
 ('poker_four_kind',r'four.of.a.kind','A03',True),
 ('poker_three_kind',r'three.of.a.kind','A03',True),
 ('one_ace_each',r'one ace each|each player.*one ace','A07',True),
 ('dice_distinct_faces',r'distinct outcomes in dice|exactly.*distinct.*(?:dice|faces)','A08',True),
 ('nonadjacent_selection',r'non.adjacent selection|select.*nonconsecutive','A04',True),
 ('circular_group_together',r'group sits together at a circular table','A06',True),
 ('lottery_matching',r'^lucky lottery probability$','A07',True),
 ('suit_three_two',r'two.suit five.card','A02',True),
 ('higher_card',r'higher card wins','A13',True),
 ('ants_triangle',r'ant.*collision.*triangle','A13',True),
 ('finite_exact_head_run',r'run of exactly.*heads in.*flips','A06',True),
 ('subset_contains_element',r'element.*in a random subset','A09',True),
 ('age_order_circle',r'age.ordered circular seating','A05',True),
 ('subset_containment',r'random subset.*contained in another','A09',True),
 ('hidden_coin_bayes',r'bayesian coin|posterior.*double.headed coin|two.headed coin|two coins.*double.headed|coin.*fair vs.*double','B03',True),
 ('two_children_reporting',r'two children|two boys|tuesday boy','B05',True),
 ('uniform_sum',r'(?:pdf|distribution|probability).*sum of.*uniform|sum of two.*uniform','C12',True),
 ('uniform_product',r'(?:pdf|distribution).*product of.*uniform','C11',True),
 ('fixed_points',r'fixed.point|fixed point','D02',True),
 ('uniform_maximum',r'(?:maximum|max).*uniform','D07',True),
 ('two_consecutive_heads_wait',r'(?:wait|expected).*two consecutive heads','E02',True),
 ('three_roll_dice_stop',r'three.roll dice|three.roll.*stopp','E05',True),
]

KNOWN = {3660:'A02',293:'A01',132:'A04',67:'A08',839:'A03',301:'A03',3662:'A07',172:'A08',465:'A04',298:'A06',65:'A01',912:'A06',1068:'A02',600:'A07',230:'A13',3582:'A06',207:'A09',630:'A05',3654:'A13',488:'A09',5:'X24',3628:'X24',51:'X22',460:'X22',883:'A06',1091:'A02',1098:'X06',1099:'C13',1208:'X09',1028:'X22',682:'X22',3708:'X08',507:'X24',787:'X24',3409:'A05'}

def stable(key):
    return hashlib.sha256((VERSION+'|'+str(key)).encode()).hexdigest()

def route(q):
    t=q['title'].lower()
    u=FAMILY_ROUTES[q['family_id']]
    prototype=None; forced=False
    for name,pattern,pu,seen in PROTOTYPES:
        if re.search(pattern,t):
            prototype=name;u=pu;forced=seen;break
    if prototype is None and not u.startswith('X'):
        # Refine broad source categories by the object actually named in the title.
        if re.search(r'circular|round table',t) and q['family_id'] in ('F0037','F0016','F0169'):
            u='A05'
        elif re.search(r'non.adjacent|sit adjacent|all adjacent|adjacent birds',t):u='A04'
        elif re.search(r'subset|binary sample space',t) and q['family_id'] in ('F0016','F0037','F0101'):u='A09'
        elif re.search(r'(?:labeled|labelled) groups|special person per group|dividing students',t):u='A10'
        elif re.search(r'lottery|powerball|card|deck|poker|urn|marble|sock|glove|candy|pair.*shoe|red.*ball|fish',t) and q['family_id']=='F0037':u='A07'
        elif re.search(r'(?:binomial|bernoulli|heads|coin flip|coin toss|penalt|engine)',t) and q['family_id']=='F0037':u='C02'
        elif q['family_id']=='F0020':
            if re.search(r'given|conditional',t):u='B01'
            elif re.search(r'prevalence|disease|infection|mortality|unsafe driver|covid|positive test|witness|smoker|rare events',t):u='B04'
            elif re.search(r'forecasters|corroboration|disagree|independent tests|signals|sequential|trade direction|chain of liars',t):u='B07'
            elif re.search(r'posterior heads|second heads|next|prediction|fair value|return probability|up day|unknown bias',t):u='B08'
            elif re.search(r'painted cube|other side|other ball|weekend|party|trips|mealtimes|timestamp',t):u='B05'
        elif re.search(r'geometric|negative binomial',t) and q['family_id'] in ('F0067','F0156','F0045'):u='C03'
        elif re.search(r'exponential|memoryless',t) and q['family_id'] in ('F0067','F0267'):u='C06'
        elif re.search(r'gamma|erlang',t):u='C07'
        elif re.search(r'beta',t) and q['family_id'] in ('F0015','F0161','F0020'):u='C08'
        elif re.search(r'pdf|density|distribution',t) and q['family_id'] in ('F0094','F0284','F0134','F0174'):u='C11'
        elif re.search(r'mixture.*normal|normal.*mixture',t):u='D05'
        elif q['family_id']=='F0104':
            if re.search(r'maximum|second maximum',t):u='D07'
            elif re.search(r'mgf|moment',t):u='C13'
            elif 'covariance' in t:u='D03'
            elif 'absolute' in t:u='D01'
        elif q['family_id'] in ('F0013','F0063'):
            if re.search(r'infinite|unlimited',t):u='E08'
            elif re.search(r'die|dice|threshold|uniform|bill|cash out|jackpot',t):u='E05'
            elif re.search(r'card|bag|marble|red.black|red.or.pass|blue.red',t):u='E06'
    if q['id'] in KNOWN:u=KNOWN[q['id']]
    return u,prototype,forced

def normalize_title(title):
    t=title.lower().replace('–','-').replace('—','-')
    numbers='one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen twenty thirty forty fifty hundred thousand'.split()
    for word in numbers:t=re.sub(r'\b'+word+r'\b',' NUM ',t)
    t=re.sub(r'\d+(?:\.\d+)?',' NUM ',t)
    tokens=re.findall(r'[a-z]+',t)
    stops={'the','a','an','of','in','on','for','from','to','is','are','and','with','its','it','that','probability','expected','value'}
    return ' '.join(w for w in tokens if w not in stops)

def main():
    raw=[x for p in sorted((ROOT/'data/catalog').glob('questions-*.json')) for x in json.loads(p.read_text()) if x['chapter']<=5]
    assert len(raw)==1155 and len({q['id'] for q in raw})==1155
    assert {q['family_id'] for q in raw} <= set(FAMILY_ROUTES)
    prior=json.loads((ROOT/'state/training-2026-10-28.json').read_text())
    exposed={x['source_catalog_id'] for x in prior['questions'] if x.get('attempts') or x.get('assignment_status')=='issued_unanswered'}
    for b in prior.get('superseded_batches',[]):
        exposed.update(x['source_catalog_id'] for x in b['questions'])
    rows=[]
    for q in raw:
        unit,prototype,forced=route(q)
        rows.append({'id':q['id'],'unit':unit,'clone_group':prototype or normalize_title(q['title']),'source_read':q['question_read'],'exposed':q['id'] in exposed,'seen_template':forced,'difficulty':q['difficulty'],'title':q['title'],'family':q['family_id']})
    # Conservative title-level near-duplicate clustering. Full-stem review remains
    # mandatory before issuing any held-out test; family alone is not a clone.
    parent={r['id']:r['id'] for r in rows}
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b:parent[max(a,b)]=min(a,b)
    buckets=defaultdict(list)
    for r in rows:buckets[r['unit']].append(r)
    for bucket in buckets.values():
        for i,a in enumerate(bucket):
            for b in bucket[i+1:]:
                if a['clone_group']==b['clone_group']:union(a['id'],b['id']);continue
                if a['seen_template'] or b['seen_template']:continue
                aa=set(normalize_title(a['title']).split());bb=set(normalize_title(b['title']).split())
                if a['family']==b['family'] and min(len(aa),len(bb))>=3 and len(aa&bb)/len(aa|bb)>=0.78:union(a['id'],b['id'])
    groups=defaultdict(list)
    for r in rows:
        r['clone_group']='G'+str(find(r['id'])).zfill(4)
        groups[r['clone_group']].append(r)
    forced_groups={g for g,rs in groups.items() if any(x['exposed'] or x['seen_template'] for x in rs)}
    test_groups=set()
    unit_stats=[]
    for unit in UNITS:
        rs=[r for r in rows if r['unit']==unit]
        gs={r['clone_group'] for r in rs}
        candidates=sorted(gs-forced_groups,key=stable)
        target=round(len(rs)*0.2)
        possible={0:()}
        for g in candidates:
            size=len(groups[g])
            for n,chosen in list(possible.items())[::-1]:
                if n+size not in possible:possible[n+size]=chosen+(g,)
        valid=[(n,ch) for n,ch in possible.items() if n<len(rs) and (n>0 or len(gs)<2 or not candidates)]
        if valid:
            n,ch=min(valid,key=lambda v:(abs(v[0]-target),v[0]>target,stable('|'.join(v[1]))))
            test_groups.update(ch)
    eligible=[r for r in rows if not r['unit'].startswith('X')]
    target=round(len(eligible)*0.2)
    # Use singleton groups to make the whole-bank split as close to 80/20 as
    # possible without removing a unit's only train or only test group.
    for direction in (1,-1):
        for g in sorted(groups,key=stable):
            current=sum(len(groups[x]) for x in test_groups)
            if current==target:break
            rs=groups[g];u=rs[0]['unit']
            if u.startswith('X') or len(rs)!=1 or g in forced_groups:continue
            ug={x['clone_group'] for x in eligible if x['unit']==u}
            if current<target and direction==1 and g not in test_groups and len(ug-test_groups)>1:test_groups.add(g)
            elif current>target and direction==-1 and g in test_groups and len(ug&test_groups)>1:test_groups.remove(g)
    for r in rows:
        r['split']='deferred' if r['unit'].startswith('X') else ('test' if r['clone_group'] in test_groups else 'train')
    for unit,data in UNITS.items():
        rs=[r for r in rows if r['unit']==unit]
        counts=Counter(r['split'] for r in rs)
        ready=Counter(r['split'] for r in rs if r['source_read'])
        data.update({'catalog_count':len(rs),'train_count':counts['train'],'test_count':counts['test'],'read_train_stems':ready['train'],'read_test_stems':ready['test'],'needs_custom_test_supplement':counts['test']<2})
    # Unit prerequisite graph is a DAG; a prerequisite can be taught earlier
    # inside the same broad chapter without changing the five-part mainline.
    done=set()
    for unit in UNITS:
        assert set(UNITS[unit]['prerequisites'])<=done,(unit,UNITS[unit]['prerequisites'])
        done.add(unit)
    sets={name:sorted(r['id'] for r in rows if r['split']==name) for name in ('train','test','deferred')}
    assert set(sets['train']).isdisjoint(sets['test'])
    assert set(sets['train'])|set(sets['test'])|set(sets['deferred'])=={r['id'] for r in rows}
    assert not (set(sets['test']) & exposed)
    assert all(len({r['split'] for r in rs})==1 for rs in groups.values())
    assert all(not r['seen_template'] for r in rows if r['split']=='test')
    summary={'version':VERSION,'source_catalog_total':len(rows),'mainline_total':len(eligible),'train_total':len(sets['train']),'test_total':len(sets['test']),'deferred_total':len(sets['deferred']),'read_train_stems':sum(r['source_read'] and r['split']=='train' for r in rows),'read_test_stems':sum(r['source_read'] and r['split']=='test' for r in rows),'read_deferred_stems':sum(r['source_read'] and r['split']=='deferred' for r in rows),'unit_count':len(UNITS),'clone_group_count':len(groups),'learner_exposed_catalog_ids':sorted(exposed),'core_plan_train_slots':3*len(UNITS),'core_plan_test_slots':2*len(UNITS),'routing_status':'provisional family and title routing; review actual stem before teaching or testing','test_novelty_status':'title-level clone grouping and known-exposure exclusions; full-stem audit required before each test','no_new_learner_answers':True}
    (ROOT/'sets').mkdir(exist_ok=True)
    for name,ids in sets.items():
        payload={'version':VERSION,'split':name,'count':len(ids),'ids':ids,'by_unit':{u:[r['id'] for r in rows if r['unit']==u and r['split']==name] for u in sorted({r['unit'] for r in rows if r['split']==name})},'read_stem_ids':[r['id'] for r in rows if r['split']==name and r['source_read']],'not_yet_read_original_ids':[r['id'] for r in rows if r['split']==name and not r['source_read']]}
        if name=='test':payload['release_rule']='Before release, check the full stem, actual conditions, independently validated reference answer, prerequisite coverage, and near-duplicate learner exposure. Show an English stem without method hints or solutions until the first learner submission. Replace a pending candidate if its original is unavailable or its assumptions cannot support an unambiguous answer; label any independently authored counterpart explicitly.'
        (ROOT/f'sets/{name}.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'data/learning_units.json').write_text(json.dumps(list(UNITS.values()),ensure_ascii=False,indent=2)+'\n')
    compact=[{k:r[k] for k in ('id','unit','split','clone_group','source_read','exposed','seen_template')} for r in rows]
    (ROOT/'data/microcourse_assignments.json').write_text('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in compact)+'\n]\n')
    (ROOT/'data/microcourse_split_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'data/microcourse_family_routes.json').write_text(json.dumps(FAMILY_ROUTES,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False))
    print('SMALL_UNITS',json.dumps([{k:u[k] for k in ('unit_id','title','catalog_count','train_count','test_count','read_test_stems')} for u in UNITS.values()],ensure_ascii=False))

if __name__=='__main__':main()
