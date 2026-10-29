"""Write the learner-facing guide and first unit from the checked split."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
from itertools import permutations
import json

ROOT=Path(__file__).resolve().parents[1]
units=json.loads((ROOT/'data/learning_units.json').read_text())
summary=json.loads((ROOT/'data/microcourse_split_summary.json').read_text())
assignments=json.loads((ROOT/'data/microcourse_assignments.json').read_text())
raw={x['id']:x for p in sorted((ROOT/'data/catalog').glob('questions-*.json')) for x in json.loads(p.read_text())}
domains={'A':'组合概率','B':'条件概率与贝叶斯','C':'随机变量与分布','D':'期望与矩','E':'递推与最优停止'}
domain_topics={'A':'C与A、重复排列、捆绑、圆排列、容斥、抽样、子集、分配与路径','B':'条件样本空间、全概率、Bayes、基准率、报告机制、独立、更新与预测','C':'离散和连续分布、联合条件分布、变换、卷积、生成函数与几何概率','D':'期望、方差协方差、条件期望、顺序统计、集齐、尾界与极限','E':'状态递推、重叠、吸收、Bellman、阈值、重抽、秘书、无限期与信息'}
later={'X06':'微积分','X08':'线性代数','X09':'统计推断','X14':'金融基础','X15':'期权与支付分解','X18':'市场微观结构','X22':'算法','X24':'Brain Teasers 与博弈'}

guide=[
'# 概率小单元学习与 Train Test 划分\n',
'从组合概率开始，依次学习条件概率与贝叶斯、分布、期望、递推与最优停止。每次只学一个小单元：先用 Train 学理论和方法，再用 Test 检查独立迁移。\n',
f"原五章目录有{summary['source_catalog_total']}条，当前按题目标题和已有方法记录初分：{summary['mainline_total']}条进入概率主线，{summary['deferred_total']}条留到算法、数论或其他章节。主线分成{summary['unit_count']}个学习单元，题库暂分Train {summary['train_total']}条、Test候选{summary['test_total']}条。原站目录仍完整保留。\n",
'## 学习主线\n',
'| 顺序 | 小单元 | 核心内容 | Train题库 | Test候选 |\n|---|---:|---|---:|---:|'
]
for code,name in domains.items():
    us=[u for u in units if u['unit_id'].startswith(code)]
    guide.append(f"| {name} | {len(us)} | {domain_topics[code]} | {sum(u['train_count'] for u in us)} | {sum(u['test_count'] for u in us)} |")
guide += [
'\n## 每个单元怎么学\n',
'每个单元默认安排3道Train和2道Test。第一轮按这个节奏约有280个练习名额；题库其余题用于补弱、加练和后续复测。基础概念单元或题源不足的单元会补充明确标注的原创练习。\n',
'| 阶段 | 老师做什么 | 学生做什么 |\n|---|---|---|\n| 理论 | 解释概念、输入输出、适用条件和一个直观例子 | 用自己的话说明这次在数什么 |\n| Train 1 | 完整示范一题，逐步说明为什么使用C、A、幂或乘法 | 跟着推导，指出每个因子的含义 |\n| Train 2 | 给一题相近方法但不同条件的题，按卡点提示 | 自己写主要步骤，卡住时接受提示 |\n| Train 3 | 给练习，提交后反馈并按需要补理论 | 独立尝试，之后可以订正 |\n| Test 1 | 给未展示过的题干，不提示方法 | 首次独立选择方法、说明假设并作答 |\n| Test 2 | 改场景或关键约束，检查能否迁移 | 独立处理新条件 |\n',
'Train中的错误属于学习过程。Test只记录第一次无提示作答；讲解错题后将它用于训练，下一轮换新题复测。两题都能独立解答并解释计数对象或模型条件，才算通过本单元的基础检查；后续混合复测继续检查保持情况。\n',
'题干用英文，理论和反馈用中文。每题先复述一句题意，再解释方法选择和关键公式。默认对一批题简洁反馈，点名追问时展开对应步骤。\n',
'## Train 和 Test 的边界\n',
'1. 同一个知识点在Train和Test中都可以出现；Test考的是能否识别并应用学过的方法。\n2. 已经给你展示、提示或讲解过的题归Train。旧版混合批次也算看过，不能改个编号作为Test。\n3. 同题只改数字、近重复标题和已知相同模板作为一组分配；当前去重基于标题和已知题型。出Test前还要对照完整题干检查重复。\n4. Test在首次作答前只给题干，不给方法标签、提示或答案。你若本来见过某题，告诉我后换新题。\n5. 出Test前核对完整题干、参考解、前置知识、边界条件和观察机制。未读原题的条目只是候选；无法取得原题时，明确标为同类练习。\n6. 每学完几个单元，再做混合Test，检查在不提示类别时能否选对方法。\n',
f"这五章共有211条已读完整题干；本次主线划分中，Train含{summary['read_train_stems']}条、Test候选含{summary['read_test_stems']}条，其余28条在后续内容。其余目录条目在出题前补齐题干或准备同类练习。这里的划分不表示已读到所有付费原题。\n",
'## 细分单元\n',
'| 单元 | 学什么 | 要回答的核心问题 | 前置 |\n|---|---|---|---|'
]
for u in units:
    guide.append(f"| {u['unit_id']} | {u['title']} | {u['question']} | {'、'.join(u['prerequisites']) or '无'} |")
guide += [
'\n## 从哪里开始\n',
'当前先学A01样本空间与等可能性，再学A02排列组合与角色分配、A03重复元素排列。它们直接对应此前分母、C与A、重复阶乘的疑问。\n',
'- [A01理论与Train](lessons/A01.md)\n- [按小单元列出的Train和Test候选](QUESTION_SETS.md)\n- [Train题号](sets/train.json)\n- [Test候选题号](sets/test.json)\n- [后续章节题号](sets/deferred.json)\n- [小单元学习进度](state/microcourse_progress.json)\n',
'之前1–20题的展示和作答记录保留：已经作答10题，第1题确认独立正确，第6题公式含义不清，其余8题需要复做。尚未作答的11–20题已归Train材料，可以在对应单元使用；不要求先把整批做完。\n',
]
(ROOT/'LEARNING_PLAN.md').write_text('\n'.join(guide))

index=[
'# 小单元 Train 和 Test 候选题索引\n',
'题干已读表示有原题阅读记录；其余是按标题和方法初分的候选，出题前核对完整题干。Test不含解答，正式出题前还要检查参考解、先修知识和已见模板。学习方法见[小单元计划](LEARNING_PLAN.md)。\n',
]
for u in units:
    rs=[r for r in assignments if r['unit']==u['unit_id']]
    index += [f"## {u['unit_id']} {u['title']}\n",f"Train {u['train_count']}条；Test候选{u['test_count']}条。\n"]
    if not rs:
        index.append('基础概念单元通过专门编写的练习补齐，不机械依赖题库标题。\n')
        continue
    index.append('| 划分 | 来源ID | 题目 | 题干 |\n|---|---:|---|---|')
    for r in sorted(rs,key=lambda x:(x['split']=='test',x['id'])):
        q=raw[r['id']]
        url=(q.get('original_public_urls') or [q['url']])[0]
        index.append(f"| {'Train' if r['split']=='train' else 'Test候选'} | {r['id']} | [{q['title']}]({url}) | {'已读' if r['source_read'] else '待核对'} |")
    index.append('')
index += ['## 留到后续章节\n','| 后续方向 | 来源ID | 题目 |\n|---|---:|---|']
for r in assignments:
    if r['split']=='deferred':
        q=raw[r['id']]
        index.append(f"| {later[r['unit']]} | {r['id']} | [{q['title']}]({q['url']}) |")
(ROOT/'QUESTION_SETS.md').write_text('\n'.join(index)+'\n')

(ROOT/'lessons').mkdir(exist_ok=True)
(ROOT/'tutor').mkdir(exist_ok=True)
train=[
 {'id':'A01-TR1','stage':'worked_example','prompt_en':'Two fair six-sided dice are rolled independently. Are (1,2) and (2,1) different elementary outcomes? How many equally likely elementary outcomes are there? What is the probability that the sum is 3?','shown_in_chat':False},
 {'id':'A01-TR2','stage':'guided_practice','prompt_en':'A bag contains three distinct balls: R1 and R2 are red, and B1 is blue. Two balls are drawn uniformly without replacement, and their order is ignored. List the possible unordered pairs. Are the two color patterns RR and RB equally likely? What is the probability of drawing exactly one blue ball?','shown_in_chat':False},
 {'id':'A01-TR3','stage':'independent_practice_with_feedback','prompt_en':'A fair six-sided die has face labels 1,1,2,2,2,3. Are the three distinct recorded values equally likely? What is the probability of recording 2?','shown_in_chat':False},
]
test=[
 {'id':'A01-TE1','prompt_en':'Three distinct keys A, B, and C are placed uniformly at random into three labelled boxes 1, 2, and 3, with exactly one key per box. What is the probability that key A is in box 1 and key B is not in box 2?','shown_in_chat':False},
 {'id':'A01-TE2','prompt_en':'An integer is selected uniformly at random from {1,2,...,12}. Only its remainder after division by 5 is recorded. Are the five possible remainders equally likely? What is the probability that the recorded remainder is 2?','shown_in_chat':False},
]
for name,items in [('train',train),('test',test)]:
    for item in items:item.pop('shown_in_chat',None)
    (ROOT/f'sets/A01_{name}.json').write_text(json.dumps({'unit':'A01','source_kind':'independently_authored_learning_exercises','split':name,'exposure_tracking':'state/microcourse_progress.json','items':items},ensure_ascii=False,indent=2)+'\n')
solutions={
 'A01-TR1':{'answer':'36 elementary outcomes; (1,2) and (2,1) differ; sum 3 has probability 2/36=1/18.','reason_zh':'骰子位置有区别，基本结果是有序点数对。和值不是等可能基本结果。'},
 'A01-TR2':{'answer':'Pairs {R1,R2},{R1,B1},{R2,B1}; RR has probability 1/3 and RB has probability 2/3; exactly one blue has probability 2/3.','reason_zh':'先区分实体球，再把实体结果合并为颜色事件，不能给颜色模式直接等权。'},
 'A01-TR3':{'answer':'P(1)=2/6,P(2)=3/6,P(3)=1/6; the recorded values are not equally likely.','reason_zh':'物理面等可能，合并后的点数取值不等可能。'},
 'A01-TE1':{'answer':'1/6','reason_zh':'六种等可能分配中，只有A在1、B在3、C在2符合。'},
 'A01-TE2':{'answer':'Remainder 2 has probability 3/12=1/4; the five remainders are not equally likely.','reason_zh':'余数2来自2、7、12。各余数的原像数量不同。'},
}
assert Fraction(sum(p[0]=='A' and p[1]!='B' for p in permutations('ABC')),6)==Fraction(1,6)
assert Fraction(sum(n%5==2 for n in range(1,13)),12)==Fraction(1,4)
(ROOT/'tutor/A01_reference.json').write_text(json.dumps({'unit':'A01','release_test_solutions':'only after the first independent learner submission','solutions':solutions},ensure_ascii=False,indent=2)+'\n')
lesson=r'''# A01 样本空间与等可能性

这一单元只解决一个问题：什么才是可以直接用“有利结果数除以总结果数”的基本结果。

## 核心理论

先描述随机实验，再确定基本结果。只有这些基本结果等可能时，才能直接使用：

\[
P(E)=\frac{\text{符合事件E的基本结果数}}{\text{全部基本结果数}}.
\]

两个骰子的位置不同，基本结果是有序点数对。同色球也可能是不同的实体球。多个基本结果合并后形成的和值、颜色模式或点数，不一定还等可能。

本单元先列结果；A02再系统比较 \(C_n^k\)、\(A_n^k\) 与 \(n^k\)。每次使用公式时都要说清对象、顺序和能否重复。

## Train 1 完整示范

Two fair six-sided dice are rolled independently. Are (1,2) and (2,1) different elementary outcomes? How many equally likely elementary outcomes are there? What is the probability that the sum is 3?

两个骰子的位置区分开来，所以 \((1,2)\) 和 \((2,1)\) 是不同基本结果。每个位置有6种选择，基本结果数为 \(6\times6=36\)。和值为3的结果只有这两对，因此概率为 \(2/36=1/18\)。

这里的36是在数掷骰结果，不是在数和值的可能取值。

## Train 2 一起做

A bag contains three distinct balls: R1 and R2 are red, and B1 is blue. Two balls are drawn uniformly without replacement, and their order is ignored. List the possible unordered pairs. Are the two color patterns RR and RB equally likely? What is the probability of drawing exactly one blue ball?

先列实体球对，再按颜色归类。想一想：两个红球同色，是否就能把它们当成同一个抽样对象？这里由老师按你的卡点给提示。

## Train 3 自己尝试

A fair six-sided die has face labels 1,1,2,2,2,3. Are the three distinct recorded values equally likely? What is the probability of recording 2?

提交思路后再反馈。尝试时先说等可能的是物理面还是记录的点数。

## Test 安排

本单元另备两道未在聊天中展示的独立题。完成Train后再出Test，不预先给方法或答案。若你认识某道Test题，换一道新的。

测试时分别检查：是否找对等可能基本结果，是否把目标事件数完整，以及概率是否算对。后续复测使用新题。
'''
(ROOT/'lessons/A01.md').write_text(lesson)

progress={'version':summary['version'],'current_unit':'A01','current_stage':'train_lesson_ready','lesson':'lessons/A01.md','core_train_file':'sets/A01_train.json','core_test_file':'sets/A01_test.json','test_prompts_shown_in_chat':False,'formal_test_attempts':[],'prior_catalog_attempts':10,'prior_confirmed_correct':1,'units':[{'unit_id':u['unit_id'],'status':'not_assessed','train_attempts':[],'test_attempts':[],'historical_evidence':[{'legacy_question':1,'catalog_id':3660,'answer':'20/216','correct':True}] if u['unit_id']=='A02' else []} for u in units]}
micro_progress_path=ROOT/'state/microcourse_progress.json'
if not micro_progress_path.exists():
    micro_progress_path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n')

readme=ROOT/'README.md'
text=readme.read_text()
needle='## 从这里开始\n\n'
assert needle in text
if '[概率小单元与Train Test计划](LEARNING_PLAN.md)' not in text:
    text=text.replace(needle,needle+'- **[概率小单元与Train Test计划](LEARNING_PLAN.md)**：当前学习入口，56个小单元；Train边教边学，Test独立迁移。\n- **[按单元查看题目划分](QUESTION_SETS.md)**：Train、Test候选和后续章节分别列出。\n',1)
readme.write_text(text)
cp=ROOT/'CURRICULUM.md';text=cp.read_text()
if '[56个小单元与Train Test学习计划](LEARNING_PLAN.md)' not in text:
    text=text.replace('# 24章合并学习目录\n','# 24章合并学习目录\n\n当前前五章采用[56个小单元与Train Test学习计划](LEARNING_PLAN.md)。下表保留完整课程和来源目录计数。\n',1)
cp.write_text(text)
wp=ROOT/'WEEK_PLAN.md';text=wp.read_text()
if '2026-10-29起，以[小单元与Train Test计划]' not in text:
    text=text.replace('# 本周复习计划：2026-10-28 至 2026-11-01\n','# 本周复习计划：2026-10-28 至 2026-11-01\n\n2026-10-29起，以[小单元与Train Test计划](LEARNING_PLAN.md)作为当前学习安排：先完成概率主线的小单元，再进入下一大章。下面的五天日历保留作参考；10/28的578题是原冲刺目标，现按理论带教和独立测试进度推进。\n',1)
wp.write_text(text)

mp=ROOT/'MEMORY.md'
memory=f'''# 本项目的持续学习记忆

## 当前学习目标和入口

用户把绿皮书与QuantVault结合学习。2026-10-29最新要求：按小知识单元学习，明确划分Train和Test；Train边教理论边做题，Test独立作答。当前入口LEARNING_PLAN.md，单元定义data/learning_units.json，进度state/microcourse_progress.json。

主线顺序固定为组合概率、条件概率与贝叶斯、分布、期望、递推与最优停止。每次只推进一个小单元。当前A01样本空间与等可能性，接着A02排列组合与角色分配、A03重复排列。不能根据网站宽泛标签混入数论证明或二分查找。

## 讲解方式

题干英文；理论、方法和批改用中文。每题先简短复述输入输出，再说明数的对象、顺序是否重要、是否允许重复，以及每个C、A、幂、乘法或阶乘因子的意义。先给直观场景，再推导。默认对整批简洁反馈；用户追问某一步时再展开，避免只对一道题超长讲解而漏掉其余题。扑克牌等术语需要解释。

每单元默认Train 1完整示范、Train 2共同推导、Train 3自己练习并接受反馈，再做两道Test。Test首次提交前不提示方法或答案；错题讲解后用于Train，复测换新题。两个Test能独立完成且说明关键假设，才算通过本单元基础检查，不据此推断所有变式掌握。

## 题库与划分范围

原前五章目录1155条。当前按标题、标签和已有方法记录初分为概率主线{summary['mainline_total']}条，Train {summary['train_total']}、Test候选{summary['test_total']}；另{summary['deferred_total']}条留后续章节。共56小单元，首轮按3 Train加2 Test节奏安排，约280练习名额，其余补弱或复测。

原五章211条完整题干已读；主线Train含{summary['read_train_stems']}条已读题干、Test候选含{summary['read_test_stems']}条，其余28条归后续。标题归类与近重复分组是初分；出题前核对完整题干，尤其Test还要验证参考解、先修知识与用户已见题。不可声称读过未读付费原题；缺少原题时明确标注同类练习。

已展示、讲过、提示过的题都进Train，包括已作废的混合批次。用户旧15题预览中已见的硬币Bayes、两孩子、均匀和与积、不动点、均匀最大值、HH等待、三掷骰停止等模板亦纳入保守排除。只改数字的近重复题不跨Train/Test；同一知识点可以在两侧出现。Test用过后记录历史，复测换题。

## 已有作答和薄弱点

本轮实际作答仍只有最初1–10题。第1题枚举20/216正确；第6题公式13C3-41211/C552排版不清，只给条件式反馈，不确定判错；其余8题需要复做。当前没有正式Test成绩，也没有整章掌握证据。要求下一批或说“好”不等于独立掌握。

主要卡点是等可能样本空间、C与A、重复对象除阶乘、块内顺序、点数与花色、整副发牌与A牌位两种样本空间、期望人数与任意碰撞概率、容斥重叠和圆排列压块。第8题重复排列、第9题题干、第10题压块及容斥已追加解释，未新增独立作答。

当前有效旧批次11–20是probability_mainline_v2版本，已展示未作答，全部作为Train材料在相应小单元复用。旧混合版数论、开关、二分查找已作废并保留历史，不能恢复为当前题。20条已布置和10条已作答的旧记录保留在state/training-2026-10-28.json；578题是旧冲刺计划，现学习入口以小单元Train/Test为准。

## 旧知识背景与来源

曾列103个微积分及相关应用知识点；讲过协方差后的QR、PCA、SVD、Cholesky、正交矩阵与行列式，金融方程88–103的输入输出，以及绿皮书BrainTeasers九类37题。列过或讲过都不能标记掌握。

全站资料范围仍以SCOPE.md为准：动态目录3385条，公开完整题干476条、站方解答474条。24章原目录、绿皮书150题组与23条理论记录保留。不要加入书PDF、整站解答复制、账户信息或无关个人记忆。
'''
if '2026-10-29最新要求' not in mp.read_text():
    mp.write_text(memory)

ap=ROOT/'AGENTS.md';text=ap.read_text()
if 'Current active workflow (2026-10-29)' not in text:
    text+='\nCurrent active workflow (2026-10-29): use LEARNING_PLAN.md, data/learning_units.json and state/microcourse_progress.json. Teach one coherent micro-unit at a time: theory, fully worked Train 1, guided Train 2, independent practice Train 3 with feedback, then two fresh Test items without hints before the first learner submission. Earlier exposed questions and near-number-only variants belong to Train. Full-stem and answer validation are required before a title-routed test candidate is issued. Keep first test attempts, corrected practice and historical exposure separate; do not resume the old fixed-ten queue automatically.\n'
ap.write_text(text)
pp=ROOT/'state/progress.json';p=json.loads(pp.read_text())
if not p.get('active_course',{}).get('progress_file')=='state/microcourse_progress.json':
    p.update({'updated_at':'2026-10-29','phase':'micro_unit_train_test_learning','current_chapter':1,'active_course':{'file':'LEARNING_PLAN.md','progress_file':'state/microcourse_progress.json','unit_count':56,'current_unit':'A01','stage':'train_lesson_ready','mainline_catalog_count':summary['mainline_total'],'train_catalog_count':summary['train_total'],'test_candidate_count':summary['test_total'],'deferred_count':summary['deferred_total']},'next_action':'Start A01 theory and Train 1, then guided Train 2 and independent Train 3. Release the two A01 Test stems only after training, with no advance hints or solutions. Preserve prior ten attempts; no formal Test has been taken.'})
    p['active_training']['status']='historical_reference_replaced_by_micro_unit_workflow'
    p['current_focus']={'unit':'A01','theme':'样本空间与等可能性','stage':'train_ready','test_stage':'reserved_not_shown_in_chat'}
    p['learner_mastery_verified']=False
    pp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')

files=['tools/build_microcourse_split.py','tools/build_microcourse_guides.py','data/learning_units.json','data/microcourse_assignments.json','data/microcourse_split_summary.json','data/microcourse_family_routes.json','sets/train.json','sets/test.json','sets/deferred.json','LEARNING_PLAN.md','QUESTION_SETS.md','lessons/A01.md','sets/A01_train.json','sets/A01_test.json','tutor/A01_reference.json','state/microcourse_progress.json','README.md','CURRICULUM.md','WEEK_PLAN.md','MEMORY.md','AGENTS.md','state/progress.json']
(ROOT.parent/'microcourse_publish_paths.json').write_text(json.dumps(files))
print(json.dumps({'files':len(files),'total_bytes':sum((ROOT/f).stat().st_size for f in files),'unit_count':len(units),'catalog_split':[summary['train_total'],summary['test_total'],summary['deferred_total']],'A01_materials':{'train':len(train),'test':len(test)},'learner_answers_unchanged':10},ensure_ascii=False))
