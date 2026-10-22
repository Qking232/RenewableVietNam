import sys
sys.path.append('G:/My Drive/7. AI/Auto Post v2')
import super_productivity_tool as sp

client = sp.SuperProductivityClient()
oi = client.get_task('Oi-5LhP4thHuCNQpNmoBy')
print('Oi subtasks:')
all_oi_done = True
for sid in oi.get('subTaskIds', []):
    st = client.get_task(sid)
    print(f"  [{sid}] Done={st.get('isDone')} | {st.get('title')}")
    if not st.get('isDone'):
        all_oi_done = False
print('All Oi subtasks done?', all_oi_done)

ligc = client.get_task('lIgc_dMLxsRkWw9nOO3x9')
print('lIgc parent:', ligc.get('parentId'))
parent = client.get_task(ligc.get('parentId')) if ligc.get('parentId') else None
print('Parent task:', parent.get('title') if parent else None, 'Done=', parent.get('isDone') if parent else None)
