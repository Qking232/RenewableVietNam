import sys
sys.path.append('G:/My Drive/7. AI/Auto Post v2')
import super_productivity_tool as sp

client = sp.SuperProductivityClient()
parent_ids = [
    '9_o1sFIGX_YkzgEZ9MxdF',
    '2A3jGzUb6Lc1BzQyY3s3N',
    'pHP0UasbMdH4ruNbvjQJk',
    'I0YL7XrZ4H7AwFW2Qku-b'
]

for pid in parent_ids:
    t = client.get_task(pid)
    print(f"=== [{t['id']}] {t.get('title')} ===")
    print(f"  Created: {t.get('created')}")
    print(f"  Subtasks ({len(t.get('subTaskIds', []))}):")
    for sid in t.get('subTaskIds', []):
        st = client.get_task(sid)
        print(f"    - [{st['id']}] Done={st.get('isDone')} | {st.get('title')}")
